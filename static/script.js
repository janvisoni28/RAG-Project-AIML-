async function sendQuery() {
    const queryInput = document.getElementById("query");
    const chatBox = document.getElementById("chat-box");

    const query = queryInput.value.trim();
    if (!query) return;

    chatBox.innerHTML += `<div class="user"><b>You:</b> ${query}</div>`;

    const response = await fetch("/ask", {
        method: "POST",
        headers: {
            "Content-Type": "application/json"
        },
        body: JSON.stringify({ query })
    });

    const data = await response.json();

    chatBox.innerHTML += `
        <div class="bot">
            <b>Answer:</b> ${data.answer} <br>
            <b>Status:</b> ${data.status} <br>
            <b>Faithfulness Score:</b> ${data.faithfulness_score}
        </div>
    `;

    queryInput.value = "";
    chatBox.scrollTop = chatBox.scrollHeight;
}