async function getMessage() {

    try {
        const response = await fetch("http://localhost:8000/api/message");

        const data = await response.json();

        document.getElementById("result").innerText = data.message;

    } catch (error) {
        console.error(error);

        document.getElementById("result").innerText =
            "Failed to connect to backend";
    }
}