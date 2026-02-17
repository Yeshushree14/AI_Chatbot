let chart = null;

async function predictStock() {
    const ticker = document.getElementById('ticker').value.trim();
    const days = document.getElementById('days').value;
    
    if (!ticker) {
        showError('Please enter a stock ticker');
        return;
    }
    
    showLoading(true);
    hideError();
    hideResults();
    
    try {
        const response = await fetch('/predict', {
            method: 'POST',
            headers: {'Content-Type': 'application/json'},
            body: JSON.stringify({ticker, days})
        });
        
        const data = await response.json();
        
        if (!response.ok) {
            throw new Error(data.error || 'Prediction failed');
        }
        
        displayResults(data, ticker, days);
    } catch (error) {
        showError(error.message);
    } finally {
        showLoading(false);
    }
}

function displayResults(data, ticker, days) {
    document.getElementById('currentPrice').textContent = `$${data.current_price}`;
    document.getElementById('accuracy').textContent = `${data.accuracy}%`;
    
    const futureLabels = Array.from({length: parseInt(days)}, (_, i) => `Day +${i+1}`);
    const allLabels = [...data.dates, ...futureLabels];
    const allData = [...data.historical, ...Array(data.predictions.length).fill(null)];
    const predData = [...Array(data.historical.length).fill(null), ...data.predictions];
    
    if (chart) chart.destroy();
    
    const ctx = document.getElementById('chart').getContext('2d');
    chart = new Chart(ctx, {
        type: 'line',
        data: {
            labels: allLabels,
            datasets: [{
                label: 'Historical Price',
                data: allData,
                borderColor: '#667eea',
                backgroundColor: 'rgba(102, 126, 234, 0.1)',
                tension: 0.4
            }, {
                label: 'Predicted Price',
                data: predData,
                borderColor: '#f093fb',
                backgroundColor: 'rgba(240, 147, 251, 0.1)',
                borderDash: [5, 5],
                tension: 0.4
            }]
        },
        options: {
            responsive: true,
            plugins: {
                title: {
                    display: true,
                    text: `${ticker} Stock Price Prediction`
                }
            },
            scales: {
                y: {
                    beginAtZero: false
                }
            }
        }
    });
    
    document.getElementById('results').style.display = 'block';
}

function showLoading(show) {
    document.getElementById('loading').style.display = show ? 'block' : 'none';
}

function showError(message) {
    const errorDiv = document.getElementById('error');
    errorDiv.textContent = message;
    errorDiv.style.display = 'block';
}

function hideError() {
    document.getElementById('error').style.display = 'none';
}

function hideResults() {
    document.getElementById('results').style.display = 'none';
}

document.getElementById('ticker').addEventListener('keypress', (e) => {
    if (e.key === 'Enter') predictStock();
});

document.getElementById('days').addEventListener('keypress', (e) => {
    if (e.key === 'Enter') predictStock();
});
