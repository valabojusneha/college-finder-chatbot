function startVoice() {
    let recognition = new (window.SpeechRecognition || window.webkitSpeechRecognition)();

    recognition.lang = "en-US";

    recognition.start();

    recognition.onresult = function(event) {
        let text = event.results[0][0].transcript;
        document.getElementById("chatInput").value = text;
    };

    recognition.onerror = function(event) {
        alert("Voice error: " + event.error);
    };
}