# Technical Specification - EcoRide

## System Components
- **Authentication Service**: Manages user registration, profiles for riders and drivers, and handles secure JWT-based session management.
- **Ride Matching Service**: Core engine responsible for pairing riders with available electric vehicles based on proximity and eco-efficiency.
- **Payment Service**: Processes financial transactions and manages the sustainable travel loyalty points system.

## Data Models
- **User**: id, name, email, role, eco_points
- **Ride**: id, rider_id, driver_id, status, co2_saved
- **Payment**: id, ride_id, amount, status

## API Endpoints
- **POST /auth/register**: Parameters (username, email, password, role) - Registers a new account.
- **POST /rides/search**: Parameters (pickup_lat, pickup_lng, destination_lat, destination_lng) - Returns nearby available EVs.
- **POST /rides/book**: Parameters (ride_id, vehicle_id) - Confirms the booking between rider and driver.
- **POST /payment/charge**: Parameters (ride_id, amount, payment_method) - Executes the trip transaction.
