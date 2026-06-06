function sendMessage() {
    let input = document.getElementById("chatInput").value;

    let chatBox = document.getElementById("chatBox");

    chatBox.innerHTML += `<p class="user">You: ${input}</p>`;

    fetch("/chat", {
        method: "POST",
        headers: {
            "Content-Type": "application/json"
        },
        body: JSON.stringify({ message: input })
    })
    .then(res => res.json())
    .then(data => {

        let reply = data.reply;

        // If reply is array (colleges)
        if (Array.isArray(reply)) {
            let text = "";

            reply.forEach(c => {
                text += `${c.name} - ${c.branch} - ${c.location}<br>`;
            });

            chatBox.innerHTML += `<p class="bot">Bot:<br>${text}</p>`;
        } 
        else {
            chatBox.innerHTML += `<p class="bot">Bot: ${reply}</p>`;
        }

        chatBox.scrollTop = chatBox.scrollHeight;
    });

    document.getElementById("chatInput").value = "";
}