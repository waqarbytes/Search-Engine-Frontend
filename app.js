document.getElementById('search-form').addEventListener('submit', function (e) {
    e.preventDefault();
    const searchTerm = document.getElementById('search-term').value;

    fetch(`/search?q=${searchTerm}`)
        .then(response => response.json())
        .then(data => {
            const resultsSection = document.getElementById('results-section');
            resultsSection.innerHTML = '';

            data.results.forEach(result => {
                const resultCard = document.createElement('div');
                resultCard.className = 'result-card';
                resultCard.innerHTML = `
            <h3>${result.title}</h3>
            <p>${result.description}</p>
            <a href="${result.link}" target="_blank">View More</a>`;
                resultsSection.appendChild(resultCard);
            });
        });
});
