/**
 * Python Playground - 主要 JavaScript 檔案
 */

let autoRefreshInterval = null;
let isAutoRefresh = false;
let focusedEditor = null;

// 追蹤每個組別的互動模式狀態
const interactiveState = {
    1: { active: false, pollInterval: null },
    2: { active: false, pollInterval: null },
    3: { active: false, pollInterval: null },
    4: { active: false, pollInterval: null },
    5: { active: false, pollInterval: null },
    6: { active: false, pollInterval: null }
};

// ===== 一般執行模式 =====

function runCode(groupId) {
    const codeEditor = document.getElementById(`code-${groupId}`);
    const inputArea = document.getElementById(`input-${groupId}`);
    const outputArea = document.getElementById(`output-${groupId}`);
    const statusBar = document.getElementById(`status-${groupId}`);
    const runBtn = document.getElementById(`run-btn-${groupId}`);

    const code = codeEditor.value;
    const userInput = inputArea ? inputArea.value : '';

    if (!code.trim()) {
        outputArea.textContent = '[提示] 請先輸入程式碼！';
        return;
    }

    runBtn.textContent = '執行中...';
    runBtn.disabled = true;
    outputArea.textContent = '正在執行程式碼...';

    fetch(`/python_playground/run/${groupId}`, {
        method: 'POST',
        headers: { 'Content-Type': 'application/json' },
        body: JSON.stringify({ code: code, user_input: userInput })
    })
    .then(response => response.json())
    .then(data => {
        outputArea.textContent = data.output || '（無輸出）';
        statusBar.textContent = `最後執行: ${data.last_run}`;
        runBtn.textContent = '執行';
        runBtn.disabled = false;
    })
    .catch(error => {
        outputArea.textContent = `[錯誤] ${error.message}`;
        runBtn.textContent = '執行';
        runBtn.disabled = false;
    });
}

// ===== 互動模式 =====

function toggleInteractive(groupId) {
    const state = interactiveState[groupId];

    if (state.active) {
        stopInteractive(groupId);
    } else {
        startInteractive(groupId);
    }
}

function startInteractive(groupId) {
    const codeEditor = document.getElementById(`code-${groupId}`);
    const outputArea = document.getElementById(`output-${groupId}`);
    const interactiveBtn = document.getElementById(`interactive-btn-${groupId}`);
    const runBtn = document.getElementById(`run-btn-${groupId}`);
    const batchInput = document.getElementById(`batch-input-${groupId}`);
    const interactiveInput = document.getElementById(`interactive-input-${groupId}`);
    const interactiveStatus = document.getElementById(`interactive-status-${groupId}`);

    const code = codeEditor.value;

    if (!code.trim()) {
        outputArea.textContent = '[提示] 請先輸入程式碼！';
        return;
    }

    outputArea.textContent = '啟動互動模式中...';
    interactiveBtn.disabled = true;

    fetch(`/python_playground/interactive/start/${groupId}`, {
        method: 'POST',
        headers: { 'Content-Type': 'application/json' },
        body: JSON.stringify({ code: code })
    })
    .then(response => response.json())
    .then(data => {
        if (data.success) {
            interactiveState[groupId].active = true;

            // 更新 UI
            interactiveBtn.textContent = '停止互動';
            interactiveBtn.classList.add('active');
            interactiveBtn.disabled = false;
            runBtn.disabled = true;
            batchInput.style.display = 'none';
            interactiveInput.style.display = 'block';
            interactiveStatus.textContent = '互動中';
            interactiveStatus.classList.add('running');

            // 顯示初始輸出
            outputArea.textContent = data.output || '';

            // 開始輪詢輸出
            interactiveState[groupId].pollInterval = setInterval(() => {
                pollInteractiveOutput(groupId);
            }, 500);

            // 自動聚焦輸入框
            document.getElementById(`interactive-text-${groupId}`).focus();
        } else {
            outputArea.textContent = `[錯誤] ${data.error}`;
            interactiveBtn.disabled = false;
        }
    })
    .catch(error => {
        outputArea.textContent = `[錯誤] ${error.message}`;
        interactiveBtn.disabled = false;
    });
}

function stopInteractive(groupId) {
    const interactiveBtn = document.getElementById(`interactive-btn-${groupId}`);
    const runBtn = document.getElementById(`run-btn-${groupId}`);
    const batchInput = document.getElementById(`batch-input-${groupId}`);
    const interactiveInput = document.getElementById(`interactive-input-${groupId}`);
    const interactiveStatus = document.getElementById(`interactive-status-${groupId}`);
    const outputArea = document.getElementById(`output-${groupId}`);

    // 停止輪詢
    if (interactiveState[groupId].pollInterval) {
        clearInterval(interactiveState[groupId].pollInterval);
        interactiveState[groupId].pollInterval = null;
    }

    fetch(`/python_playground/interactive/stop/${groupId}`, {
        method: 'POST'
    })
    .then(response => response.json())
    .then(data => {
        interactiveState[groupId].active = false;

        // 更新 UI
        interactiveBtn.textContent = '互動模式';
        interactiveBtn.classList.remove('active');
        runBtn.disabled = false;
        batchInput.style.display = 'block';
        interactiveInput.style.display = 'none';
        interactiveStatus.textContent = '';
        interactiveStatus.classList.remove('running');

        if (data.output) {
            outputArea.textContent = data.output;
        }
    });
}

function sendInteractiveInput(groupId) {
    const inputField = document.getElementById(`interactive-text-${groupId}`);
    const outputArea = document.getElementById(`output-${groupId}`);
    const userInput = inputField.value;

    // 在輸出區顯示用戶輸入
    outputArea.textContent += userInput + '\n';

    fetch(`/python_playground/interactive/input/${groupId}`, {
        method: 'POST',
        headers: { 'Content-Type': 'application/json' },
        body: JSON.stringify({ input: userInput })
    })
    .then(response => response.json())
    .then(data => {
        if (data.output) {
            outputArea.textContent += data.output;
        }

        if (data.finished || !data.running) {
            // 程式已結束
            stopInteractive(groupId);
        }

        // 自動滾動到底部
        outputArea.scrollTop = outputArea.scrollHeight;
    });

    // 清空輸入框
    inputField.value = '';
    inputField.focus();
}

function handleInteractiveKeypress(event, groupId) {
    if (event.key === 'Enter') {
        sendInteractiveInput(groupId);
    }
}

function pollInteractiveOutput(groupId) {
    if (!interactiveState[groupId].active) return;

    fetch(`/python_playground/interactive/output/${groupId}`)
        .then(response => response.json())
        .then(data => {
            if (data.output) {
                const outputArea = document.getElementById(`output-${groupId}`);
                outputArea.textContent += data.output;
                outputArea.scrollTop = outputArea.scrollHeight;
            }

            if (!data.running) {
                stopInteractive(groupId);
            }
        });
}

// ===== 清除功能 =====

function clearGroup(groupId) {
    if (!confirm(`確定要清除第 ${groupId} 組的程式碼和執行結果嗎？`)) {
        return;
    }

    // 先停止互動模式
    if (interactiveState[groupId].active) {
        stopInteractive(groupId);
    }

    const codeEditor = document.getElementById(`code-${groupId}`);
    const inputArea = document.getElementById(`input-${groupId}`);
    const outputArea = document.getElementById(`output-${groupId}`);
    const statusBar = document.getElementById(`status-${groupId}`);

    fetch(`/python_playground/clear/${groupId}`, { method: 'POST' })
        .then(response => response.json())
        .then(data => {
            codeEditor.value = '';
            if (inputArea) inputArea.value = '';
            outputArea.textContent = '';
            statusBar.textContent = '尚未執行';
        });
}

// ===== 即時同步 =====

function refreshAllData() {
    fetch('/python_playground/get_all_data')
        .then(response => response.json())
        .then(data => {
            for (let groupId = 1; groupId <= 6; groupId++) {
                // 跳過正在互動的組別
                if (interactiveState[groupId].active) continue;

                const group = data[groupId];
                const codeEditor = document.getElementById(`code-${groupId}`);
                const inputArea = document.getElementById(`input-${groupId}`);
                const outputArea = document.getElementById(`output-${groupId}`);
                const taskArea = document.getElementById(`task-${groupId}`);
                const statusBar = document.getElementById(`status-${groupId}`);

                if (focusedEditor !== groupId) {
                    if (codeEditor) codeEditor.value = group.code || '';
                    if (inputArea) inputArea.value = group.user_input || '';
                }

                if (outputArea) outputArea.textContent = group.output || '';
                if (taskArea) taskArea.textContent = group.task || '無指派任務';
                if (statusBar) {
                    statusBar.textContent = group.last_run
                        ? `最後執行: ${group.last_run}`
                        : '尚未執行';
                }
            }
        });
}

function toggleAutoRefresh() {
    isAutoRefresh = !isAutoRefresh;
    const btn = document.getElementById('auto-refresh-btn');

    if (isAutoRefresh) {
        autoRefreshInterval = setInterval(refreshAllData, 2000);
        btn.textContent = '即時同步：開啟';
        btn.classList.add('btn-active');
        refreshAllData();
    } else {
        clearInterval(autoRefreshInterval);
        btn.textContent = '即時同步：關閉';
        btn.classList.remove('btn-active');
    }
}

// ===== 快捷鍵 =====

document.addEventListener('keydown', function(event) {
    if (event.ctrlKey && event.key === 'Enter') {
        const activeElement = document.activeElement;
        if (activeElement && activeElement.classList.contains('code-editor')) {
            const groupId = parseInt(activeElement.id.replace('code-', ''));
            if (!interactiveState[groupId].active) {
                runCode(groupId);
            }
        }
    }
});

// Tab 鍵支援
document.querySelectorAll('.code-editor').forEach(editor => {
    editor.addEventListener('keydown', function(event) {
        if (event.key === 'Tab') {
            event.preventDefault();
            const start = this.selectionStart;
            const end = this.selectionEnd;
            this.value = this.value.substring(0, start) + '    ' + this.value.substring(end);
            this.selectionStart = this.selectionEnd = start + 4;
        }
    });

    editor.addEventListener('focus', function() {
        focusedEditor = parseInt(this.id.replace('code-', ''));
    });

    editor.addEventListener('blur', function() {
        setTimeout(() => {
            if (focusedEditor === parseInt(this.id.replace('code-', ''))) {
                focusedEditor = null;
            }
        }, 500);
    });
});

// 自動儲存
setInterval(function() {
    for (let groupId = 1; groupId <= 6; groupId++) {
        if (interactiveState[groupId].active) continue;

        const codeEditor = document.getElementById(`code-${groupId}`);
        if (codeEditor && codeEditor.value.trim()) {
            fetch(`/python_playground/save/${groupId}`, {
                method: 'POST',
                headers: { 'Content-Type': 'application/json' },
                body: JSON.stringify({ code: codeEditor.value })
            });
        }
    }
}, 30000);

// 初始化
document.addEventListener('DOMContentLoaded', function() {
    document.querySelectorAll('.code-editor').forEach(editor => {
        editor.setAttribute('spellcheck', 'false');
    });
});
