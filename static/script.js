
document.addEventListener("DOMContentLoaded", function () {
    document.getElementById("queryForm").addEventListener("submit", async function (event) {
        event.preventDefault();
        
        let query = document.getElementById("queryInput").value;
        if (!query) return;
        
        let response = await fetch("/query", {
            method: "POST",
            headers: {
                "Content-Type": "application/json"
            },
            body: JSON.stringify({ query: query })
        });

        let data = await response.json();
        let resultsDiv = document.getElementById("results");
        resultsDiv.innerHTML = "<h3>Top Results:</h3>";

        if (data.error) {
            resultsDiv.innerHTML += `<p style="color:red;">${data.error}</p>`;
        } else {
            data.forEach((item) => {
                resultsDiv.innerHTML += `<p><strong>Rank ${item.rank}:</strong> ${item.text}</p>`;
            });
        }
    });
});
