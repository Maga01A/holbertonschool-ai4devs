# EcoRide Data Model Documentation

This data model is designed to support a scalable, eco-friendly ride-sharing ecosystem. It emphasizes the separation of user roles and the tracking of environmental impact.

## Entities and Attributes

### 1. User
Represents the passenger using the service.
- **id**: Unique identifier (UUID).
- **name**: Full name of the user.
- **email**: Contact and login information.
- **loyalty_points**: Accumulated "Eco-Points" for green travel.

### 2. Driver & Vehicle
Represents the service providers and their electric vehicles.
- **driver_id**: Unique identifier for the professional driver.
- **vehicle_id**: Reference to the specific EV used.
- **status**: Availability and current battery level (telemetry data).

### 3. Ride
The central entity connecting users, drivers, and trips.
- **id**: Unique ride identifier.
- **rider_id/driver_id**: Foreign keys to the respective users.
- **status**: Enum (REQUESTED, ON_TRIP, COMPLETED, CANCELLED).
- **timestamps**: Tracking duration and response times.

### 4. Payment
Financial records for each completed trip.
- **id**: Unique transaction identifier.
- **ride_id**: Reference to the specific trip.
- **amount**: Total cost calculated based on distance and vehicle type.

### 5. Eco Impact
Specific metrics for sustainability tracking.
- **co2_saved_kg**: Amount of carbon dioxide prevented compared to a standard ICE vehicle.
- **impact_score**: Contribution to the city's overall green metrics.
