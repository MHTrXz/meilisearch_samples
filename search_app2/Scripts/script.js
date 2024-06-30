document.getElementById('search-button').addEventListener('click', () => {
    const query = document.getElementById('search-input').value;
    search(query);
});

async function search(query) {
    const response = await fetch(`http://localhost:3000/search?q=${query}`, {
        method: 'GET',
        headers: {
            'Content-Type': 'application/json'
        },
    });

    const data = await response.json();
    displayResults(data);
}

function displayResults(results) {
    const resultsDiv = document.getElementById('results');
    resultsDiv.innerHTML = '';
    console.log(results);
    if (results.length === 0) {
        resultsDiv.innerHTML = '<p>نتیجه‌ای یافت نشد.</p>';
        return;
    }

    results.forEach(result => {
        const resultItem = document.createElement('div');
        resultItem.classList.add('result-item');
        resultItem.innerHTML = `
            <h3>${result.title}</h3>
            <p>Genre: ${result.genres[0]}</p>
        `;
        resultsDiv.appendChild(resultItem);
    });
}
