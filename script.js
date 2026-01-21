const chatBox = document.getElementById("chatBox");

let firstMessage = true;
function sendMessage() {
    let input = document.getElementById("userInput").value;

    if (input === "") return;
    if (firstMessage) {
        document.body.classList.add("chat-active");
        firstMessage = false;
    }

    document.getElementById("chatBox").innerHTML +=
        "<p><b>You:</b> " + input + "</p>";
    chatBox.scrollTop = chatBox.scrollHeight;

    fetch("https://<username>-llm-chatbot-backend.hf.space/chat", {
        method: "POST",
        headers: {
            "Content-Type": "application/json"
        },
        body: JSON.stringify({ message: input })
    })
    .then(response => response.json())
    .then(data => {
        document.getElementById("chatBox").innerHTML +=
            "<p><b>Bot:</b> " + data.reply + "</p>";
    });

    document.getElementById("userInput").value = "";
    document.getElementById("userInput").blur();

}
function clearChat() {
    document.getElementById("chatBox").innerHTML = "";
    document.body.classList.remove("chat-active");
    firstMessage = true;

    // fetch("http://localhost:5000/reset", { method: "POST" });
}
