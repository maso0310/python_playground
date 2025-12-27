/**
 * Python Playground - 主要 JavaScript 檔案
 */

// 執行程式碼
function runCode(groupId) {
    const codeEditor = document.getElementById(`code-${groupId}`);
    const outputArea = document.getElementById(`output-${groupId}`);
    const statusBar = document.getElementById(`status-${groupId}`);
    const runBtn = document.querySelector(`#group-${groupId} .btn-run`);

    const code = codeEditor.value;

    if (!code.trim()) {
        outputArea.textContent = '[提示] 請先輸入程式碼！';
        return;
    }

    // 顯示執行中狀態
    runBtn.textContent = '執行中...';
    runBtn.disabled = true;
    runBtn.classList.add('running');
    outputArea.textContent = '正在執行程式碼...';

    fetch(`/python_playground/run/${groupId}`, {
        method: 'POST',
        headers: {
            'Content-Type': 'application/json'
        },
        body: JSON.stringify({ code: code })
    })
    .then(response => response.json())
    .then(data => {
        outputArea.textContent = data.output || '（無輸出）';
        statusBar.textContent = `最後執行: ${data.last_run}`;

        // 恢復按鈕狀態
        runBtn.textContent = '執行';
        runBtn.disabled = false;
        runBtn.classList.remove('running');
    })
    .catch(error => {
        outputArea.textContent = `[錯誤] 無法連接伺服器: ${error.message}`;
        runBtn.textContent = '執行';
        runBtn.disabled = false;
        runBtn.classList.remove('running');
    });
}

// 清除組別的程式碼和輸出
function clearGroup(groupId) {
    if (!confirm(`確定要清除第 ${groupId} 組的程式碼和執行結果嗎？`)) {
        return;
    }

    const codeEditor = document.getElementById(`code-${groupId}`);
    const outputArea = document.getElementById(`output-${groupId}`);
    const statusBar = document.getElementById(`status-${groupId}`);

    fetch(`/python_playground/clear/${groupId}`, {
        method: 'POST'
    })
    .then(response => response.json())
    .then(data => {
        codeEditor.value = '';
        outputArea.textContent = '';
        statusBar.textContent = '尚未執行';
    })
    .catch(error => {
        alert(`清除失敗: ${error.message}`);
    });
}

// 監聽 Ctrl+Enter 快捷鍵執行程式碼
document.addEventListener('keydown', function(event) {
    if (event.ctrlKey && event.key === 'Enter') {
        // 找到目前 focus 的編輯器
        const activeElement = document.activeElement;
        if (activeElement && activeElement.classList.contains('code-editor')) {
            const groupId = activeElement.id.replace('code-', '');
            runCode(parseInt(groupId));
        }
    }
});

// Tab 鍵支援（在編輯器中插入 4 個空格）
document.querySelectorAll('.code-editor').forEach(editor => {
    editor.addEventListener('keydown', function(event) {
        if (event.key === 'Tab') {
            event.preventDefault();
            const start = this.selectionStart;
            const end = this.selectionEnd;

            // 插入 4 個空格
            this.value = this.value.substring(0, start) + '    ' + this.value.substring(end);
            this.selectionStart = this.selectionEnd = start + 4;
        }
    });
});

// 自動儲存（每 30 秒）
setInterval(function() {
    for (let groupId = 1; groupId <= 6; groupId++) {
        const codeEditor = document.getElementById(`code-${groupId}`);
        if (codeEditor && codeEditor.value.trim()) {
            fetch(`/python_playground/save/${groupId}`, {
                method: 'POST',
                headers: {
                    'Content-Type': 'application/json'
                },
                body: JSON.stringify({ code: codeEditor.value })
            });
        }
    }
}, 30000);

// 頁面載入完成後的初始化
document.addEventListener('DOMContentLoaded', function() {
    console.log('Python Playground 已載入');

    // 為每個編輯器添加行號提示
    document.querySelectorAll('.code-editor').forEach(editor => {
        editor.setAttribute('spellcheck', 'false');
    });
});
