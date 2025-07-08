document.getElementById("check").addEventListener("click", async () => {
  const title = document.getElementById("title").value;
  const body = document.getElementById("body").value;
  const resultDiv = document.getElementById("result");
  const iconSpan = document.getElementById("icon");
  const textSpan = document.getElementById("text");

  resultDiv.className = 'hidden';

  try {
    const resp = await fetch("http://localhost:8000/predict", {
      method: "POST",
      headers: { "Content-Type": "application/json" },
      body: JSON.stringify({ title, body })
    });

    const json = await resp.json();
    const label = json.label;

    resultDiv.className = (label.startsWith("FAKE") ? "fake" : "real");
    resultDiv.innerHTML = `
      <div style="text-align: center; font-size: 2em;">
        <span id="icon">${label.startsWith("FAKE") ? "❌" : "✔️"}</span>
      </div>
      <div style="text-align: center; font-size: 1.2em;">
        <span id="text">${label}</span>
      </div>
    `;
    resultDiv.classList.remove("hidden");
  } catch (e) {
    console.error("Error connecting to server:", e);
    resultDiv.className = "fake";
    resultDiv.innerHTML = `
      <div style="text-align: center; font-size: 2em;">
        <span id="icon">❌</span>
      </div>
      <div style="text-align: center; font-size: 1.2em;">
        <span id="text">Error connecting to server</span>
      </div>
    `;
    resultDiv.classList.remove("hidden");
  }
});