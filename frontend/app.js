console.log("BUTTON CLICKED"); // DEBUG
async function generate() {
    const text = document.getElementById("inputText").value;

    console.log("Sending request..."); // DEBUG

    try {
        const res = await fetch("http://localhost:3000/generate", {
            method: "POST",
            headers: {
                "Content-Type": "application/json"
            },
            body: JSON.stringify({ text })
        });

        const data = await res.json();

        console.log("Response:", data); // DEBUG

        document.getElementById("summary").innerText = data.summary;

        const flashDiv = document.getElementById("flashcards");
        flashDiv.innerHTML = "";

        data.flashcards.forEach(card => {
            const div = document.createElement("div");
            div.innerText = `${card.question} - ${card.answer}`;
            flashDiv.appendChild(div);
        });

    } catch (err) {
        console.error("ERROR:", err);
    }
}
