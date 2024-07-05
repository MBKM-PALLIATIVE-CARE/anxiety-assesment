function calculateScore() {
    const form = document.getElementById('anxietyForm');
    const formData = new FormData(form);
    
    let totalA = 0;
    let totalD = 0;

    for (let [key, value] of formData.entries()) {
        const score = parseInt(value);
        
        if (key === 'q1' || key === 'q3' || key === 'q5' || key === 'q7' || key === 'q9' || key === 'q11' || key === 'q13') {
            totalA += score;
        } else {
            totalD += score;
        }
    }

    let scoreCategory = '';
    const totalScore = totalA + totalD;
    if (totalScore <= 7) {
        scoreCategory = 'Normal';
    } else if (totalScore <= 10) {
        scoreCategory = 'Borderline Abnormal';
    } else {
        scoreCategory = 'Abnormal';
    }

    const resultDiv = document.getElementById('result');
    resultDiv.innerHTML = `
        <h2>Hasil Penilaian</h2>
        <p>Jumlah Total A: ${totalA}</p>
        <p>Jumlah Total D: ${totalD}</p>
        <p>Kategori Skor: ${scoreCategory}</p>
    `;
}
