import unittest

def calculate_carbon_saved(distance, vehicle_type):
    emissions = {'standard': 0.12, 'hybrid': 0.07, 'ev': 0.00}
    standard_co2 = distance * emissions['standard']
    actual_co2 = distance * emissions.get(vehicle_type, 0.12)
    return round(standard_co2 - actual_co2, 2)

class TestEcoRideMVP(unittest.TestCase):
    # Backend Logic Tests
    def test_ev_savings(self): self.assertEqual(calculate_carbon_saved(10, 'ev'), 1.2)
    def test_hybrid_savings(self): self.assertEqual(calculate_carbon_saved(10, 'hybrid'), 0.5)
    def test_standard_savings(self): self.assertEqual(calculate_carbon_saved(10, 'standard'), 0.0)
    def test_long_distance(self): self.assertEqual(calculate_carbon_saved(100, 'ev'), 12.0)
    def test_zero_distance(self): self.assertEqual(calculate_carbon_saved(0, 'ev'), 0.0)
    def test_unknown_vehicle(self): self.assertEqual(calculate_carbon_saved(10, 'truck'), 0.0)
    
    # Boundary Tests
    def test_negative_distance(self): self.assertEqual(calculate_carbon_saved(-10, 'ev'), -1.2)
    def test_large_distance(self): self.assertEqual(calculate_carbon_saved(10000, 'ev'), 1200.0)
    
    # Integration & UI Logic Mock Tests
    def test_eco_points_calc(self): 
        saved = calculate_carbon_saved(10, 'ev')
        self.assertEqual(int(saved * 100), 120)
    def test_response_format(self):
        result = {"distance": 10, "carbon": calculate_carbon_saved(10, 'ev')}
        self.assertIn('carbon', result)

if __name__ == '__main__':
    unittest.main()
