document.getElementById("submit").addEventListener('click', async (e) => {
    e.preventDefault();
    const input = document.getElementById("input").value;
    const errorMessage = document.getElementById("error");
    const resultMessage = document.getElementById("result");

    errorMessage.textContent = ""
    if (!input){
        errorMessage.textContent = "Enter input";
        return;
    }

    try{
        const response = await fetch('http://localhost:8000/api/v1/predict', {
            method:"POST",
            headers:{'Content-Type':'application/json'},
            body:JSON.stringify({text:input}),
        });

        if (!response.ok){
            errorMessage.textContent = `${response.status}, Error`;
            return;
        }
        const data = await response.json();

        if (data.is_phishing){
            resultMessage.textContent = `This is likely to be phishing. Risk level: ${data.risk_level}. Confidence score: ${data.confidence_score}`;
            resultMessage.className = 'high';
        }
        else {
            resultMessage.textContent = `Safe. Risk level: ${data.risk_level}. Confidence score: ${data.confidence_score}`
            resultMessage.className = 'safe';
        }
    } catch (err){
        console.error(err);
        resultMessage.textContent = "Could not reach Docker."
    }
});
