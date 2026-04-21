const express = require('express');
const app = express();
app.use(express.json());

// API Endpoint to calculate carbon savings
app.post('/api/calculate-impact', (req, res) => {
    const { distance, vehicleType } = req.body;
    
    // Average emission factors (g CO2 per km)
    const emissions = {
        'standard': 120,
        'hybrid': 70,
        'ev': 0
    };

    if (!distance || !vehicleType) {
        return res.status(400).json({ error: 'Missing distance or vehicle type' });
    }

    const standardEmissions = distance * emissions['standard'];
    const actualEmissions = distance * (emissions[vehicleType] || emissions['standard']);
    const carbonSaved = (standardEmissions - actualEmissions) / 1000; // in kg

    res.json({
        distance: distance,
        vehicleType: vehicleType,
        carbonSavedKg: carbonSaved.toFixed(2),
        ecoPoints: Math.floor(carbonSaved * 10)
    });
});

const PORT = process.env.PORT || 3000;
app.listen(PORT, () => console.log('EcoRide Backend running on port ' + PORT));
