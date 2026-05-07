document.getElementById('foodInput').addEventListener('change', async (e) => {
    const file = e.target.files[0];
    if (!file) return;

    const resultCard = document.getElementById('resultCard');
    resultCard.classList.remove('hidden');
    document.getElementById('foodName').innerText = "Analyzing...";

    const formData = new FormData();
    formData.append('file', file);

    const response = await fetch('/upload', { method: 'POST', body: formData });
    const data = await response.json();

    // Fill the card with results
    document.getElementById('foodName').innerText = data.name;
    document.getElementById('kcal').innerText = data.kcal;
    document.getElementById('protein').innerText = data.protein;
    document.getElementById('healthScore').innerText = data.health_score;
});
