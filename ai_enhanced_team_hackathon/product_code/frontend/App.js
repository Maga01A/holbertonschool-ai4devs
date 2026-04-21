import React, { useState } from 'react';

function EcoRideApp() {
    const [saved, setSaved] = useState(0);

    const handleCalculate = () => {
        // Mocking API call logic
        setSaved(2.45);
    };

    return (
        <div style={{ padding: '20px', fontFamily: 'Arial', color: '#2d5a27' }}>
            <h1>?? EcoRide Dashboard</h1>
            <div style={{ border: '1px solid #ccc', padding: '15px', borderRadius: '10px' }}>
                <p>Enter Distance (km): <input type="number" /></p>
                <p>Vehicle: 
                    <select>
                        <option value="ev">Electric Vehicle</option>
                        <option value="hybrid">Hybrid</option>
                    </select>
                </p>
                <button onClick={handleCalculate} style={{ backgroundColor: '#10b981', color: 'white', border: 'none', padding: '10px 20px', borderRadius: '5px' }}>
                    Calculate Impact
                </button>
            </div>
            {saved > 0 && <h2 style={{ marginTop: '20px' }}>You saved {saved}kg of CO2! ??</h2>}
        </div>
    );
}

export default EcoRideApp;
