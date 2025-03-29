
const axios = require('axios');

async function getPrediction(inputData) {
  try {
    const res = await axios.post('http://localhost:8000/predict', {
      data: inputData  // Array of 10 floats
    });
    console.log("Prediction:", res.data.prediction);
    return res.data.prediction;
  } catch (error) {
    console.error("Error getting prediction:", error.message);
    return null;
  }
}

getPrediction([0.1, 0.5, -0.3, 0.2, 0.8, 0.4, -0.1, 0.9, 0.7, -0.5]);
