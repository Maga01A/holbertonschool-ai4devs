# EcoRide Data Model Documentation

This data model is designed to support a scalable, eco-friendly ride-sharing ecosystem. Each entity represents a core component of the microservices architecture.

## Entities and Attributes

### 1. User
Represents the rider/passenger who requests transportation.
- **user_id**: Unique identifier (Primary Key).
- **full_name**: The user's legal name.
- **email**: Unique email address for authentication.
- **loyalty_points**: Accumulated points for using green transport.

### 2. Driver
Represents the service provider operating the electric vehicle.
- **driver_id**: Unique identifier (Primary Key).
- **license_number**: Driver's professional license details.
- **rating**: Average user feedback score.

### 3. Vehicle
Represents the specific electric vehicle (EV) used in the fleet.
- **vehicle_id**: Unique identifier for the vehicle.
- **model**: The EV model and year.
- **battery_level**: Real-time telemetry data of the vehicle's charge.
- **status**: Current availability (Available, Maintenance, In-Use).

### 4. Ride
The central transactional entity connecting riders and drivers.
- **ride_id**: Unique trip identifier (Primary Key).
- **rider_id**: Foreign Key reference to the User.
- **driver_id**: Foreign Key reference to the Driver.
- **vehicle_id**: Foreign Key reference to the Vehicle used.
- **status**: Current state (PENDING, ACTIVE, COMPLETED, CANCELLED).
- **created_at**: Timestamp of the ride request.

### 5. Payment
Handles the financial transaction associated with a completed ride.
- **payment_id**: Unique transaction identifier.
- **ride_id**: Foreign Key reference to the Ride.
- **amount**: Final fare calculated for the trip.
- **status**: State of the payment (PENDING, PAID, REFUNDED).

### 6. Eco Impact
Tracks the environmental contribution of every trip.
- **impact_id**: Unique record identifier.
- **ride_id**: Foreign Key reference to the Ride.
- **co2_saved_kg**: Amount of CO2 prevented by using an EV.
- **distance_km**: Total distance traveled during the session.
