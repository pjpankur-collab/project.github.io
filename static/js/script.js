document.getElementById('foodInput').addEventListener('change', async (e) => {
    const file = e.target.files[0];
    if (!file) return;

    const resultCard = document.getElementById('resultCard');
    resultCard.classList.remove('hidden');
    
    // UI Loading state
    document.getElementById('foodName').innerText = "Analyzing...";

    const formData = new FormData();
    formData.append('file', file);

    try {
        const response = await fetch('/upload', {
            method: 'POST',
            body: formData
        });
        const data = await response.json();

        // Update UI with "AI" results
        document.getElementById('foodName').innerText = data.name;
        document.getElementById('foodDesc').innerText = data.description;
        document.getElementById('healthScore').innerText = data.health_score;
        document.getElementById('kcal').innerText = data.kcal;
        document.getElementById('protein').innerText = data.protein;
        document.getElementById('carbs').innerText = data.carbs;
        document.getElementById('fat').innerText = data.fat;

    } catch (error) {
        console.error("Error uploading image:", error);
        alert("Failed to analyze meal.");
    }
});

