from flask import Flask, request, jsonify

app = Flask(__name__)

@app.route('/api/impact', methods=['POST'])
def calculate_impact():
    data = request.json
    distance = data.get('distance', 0)
    vehicle_type = data.get('vehicle_type', 'standard')

    # Emissiya faktorlari (kq CO2 / km)
    emissions = {
        'standard': 0.12,
        'hybrid': 0.07,
        'ev': 0.00
    }

    standard_co2 = distance * emissions['standard']
    actual_co2 = distance * emissions.get(vehicle_type, 0.12)
    saved_co2 = standard_co2 - actual_co2

    return jsonify({
        "distance": distance,
        "vehicle_type": vehicle_type,
        "carbon_saved_kg": round(saved_co2, 2),
        "eco_points": int(saved_co2 * 100)
    })

if __name__ == '__main__':
    app.run(port=5000)
