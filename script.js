// Initialize data
let steps = 1000;
let calories = steps * 0.04;
let heartRate = 70;
let oxygenLevel = 98;
let temperature = 98.6;
let waterIntake = 0;
let waterGoal = 4;
let moodStatus = "Relaxed";
let dialysisNeeded = false;
let dialysisFrequency = "N/A";
let inflammationDetected = false;
let inflammationArea = "N/A";

// Chart data
const stepsData = [];
const heartRateData = [];
const oxygenData = [];

// Automatically update the date
function updateDate() {
    const dateElement = document.getElementById("currentDate");
    const currentDate = new Date().toLocaleDateString();
    dateElement.textContent = `Date: ${currentDate}`;
}

// Create charts
const stepsChartCtx = document.getElementById('stepsChart').getContext('2d');
const heartRateChartCtx = document.getElementById('heartRateChart').getContext('2d');
const oxygenChartCtx = document.getElementById('oxygenChart').getContext('2d');

const stepsChart = new Chart(stepsChartCtx, {
    type: 'line',
    data: {
        labels: [],
        datasets: [{
            label: 'Daily Steps',
            data: stepsData,
            borderColor: 'rgba(255, 65, 108, 1)',
            backgroundColor: 'rgba(255, 65, 108, 0.2)',
            borderWidth: 2,
            fill: true,
            tension: 0.1
        }]
    },
    options: {
        responsive: true,
        scales: {
            x: {
                title: {
                    display: true,
                    text: 'Time (minutes)'
                },
                ticks: {
                    autoSkip: true,
                    maxTicksLimit: 10,
                }
            },
            y: {
                title: {
                    display: true,
                    text: 'Steps'
                }
            }
        }
    }
});

const heartRateChart = new Chart(heartRateChartCtx, {
    type: 'line',
    data: {
        labels: [],
        datasets: [{
            label: 'Heart Rate',
            data: heartRateData,
            borderColor: 'rgba(0, 225, 255, 1)',
            backgroundColor: 'rgba(0, 225, 255, 0.2)',
            borderWidth: 2,
            fill: true,
            tension: 0.1
        }]
    },
    options: {
        responsive: true,
        scales: {
            x: {
                title: {
                    display: true,
                    text: 'Time (minutes)'
                },
                ticks: {
                    autoSkip: true,
                    maxTicksLimit: 10,
                }
            },
            y: {
                title: {
                    display: true,
                    text: 'Heart Rate (bpm)'
                }
            }
        }
    }
});

const oxygenChart = new Chart(oxygenChartCtx, {
    type: 'line',
    data: {
        labels: [],
        datasets: [{
            label: 'Oxygen Level',
            data: oxygenData,
            borderColor: 'rgba(0, 225, 0, 1)',
            backgroundColor: 'rgba(0, 225, 0, 0.2)',
            borderWidth: 2,
            fill: true,
            tension: 0.1
        }]
    },
    options: {
        responsive: true,
        scales: {
            x: {
                title: {
                    display: true,
                    text: 'Time (minutes)'
                },
                ticks: {
                    autoSkip: true,
                    maxTicksLimit: 10,
                }
            },
            y: {
                title: {
                    display: true,
                    text: 'Oxygen Level (%)'
                }
            }
        }
    }
});

// Increment steps every 5 seconds
setInterval(() => {
    steps += Math.floor(Math.random() * 10) + 1;
    calories = steps * 0.04;
    document.getElementById("steps").textContent = steps;
    document.getElementById("calories").textContent = calories.toFixed(2);

    if (stepsData.length > 24) stepsData.shift();
    stepsData.push(steps);
    stepsChart.data.labels.push(new Date().toLocaleTimeString());
    stepsChart.update();
}, 5000);

// Update heart rate every 5 seconds
setInterval(() => {
    heartRate = Math.floor(Math.random() * (120 - 60 + 1)) + 60;
    document.getElementById("heartRate").textContent = heartRate;

    if (heartRate > 120) {
        document.getElementById("heartRateStatus").textContent = "Please sit and relax.";
    } else if (heartRate < 60) {
        document.getElementById("heartRateStatus").textContent = "Visit a doctor immediately.";
    } else {
        document.getElementById("heartRateStatus").textContent = "";
    }

    if (heartRateData.length > 24) heartRateData.shift();
    heartRateData.push(heartRate);
    heartRateChart.data.labels.push(new Date().toLocaleTimeString());
    heartRateChart.update();
}, 5000);

// Update oxygen level every minute
setInterval(() => {
    oxygenLevel = Math.floor(Math.random() * (100 - 90 + 1)) + 90;
    document.getElementById("oxygenLevel").textContent = oxygenLevel;

    if (oxygenData.length > 24) oxygenData.shift();
    oxygenData.push(oxygenLevel);
    oxygenChart.data.labels.push(new Date().toLocaleTimeString());
    oxygenChart.update();
}, 60000);

// Water intake increment every 10 minutes
setInterval(() => {
    if (waterIntake < waterGoal) {
        waterIntake += 0.25;
        document.getElementById("waterIntake").textContent = waterIntake.toFixed(2);
        if (waterIntake >= waterGoal) {
            waterIntake = 0; // Reset water intake
            document.getElementById("waterReminder").textContent = "You've reached your water goal!";
        }
    }
}, 600000); // Every 10 minutes


// Initialize the date
updateDate();
