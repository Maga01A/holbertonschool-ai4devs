# Technical Specification - EcoRide Platform

## System Components

- **Authentication & User Service**: Manages user registration, profiles (Rider/Driver), and secure session handling using JWT.
- **Ride Matching Service**: The core engine that pairs riders with available electric vehicles (EVs) based on proximity, carbon-saving potential, and route optimization.
- **Payment & Rewards Service**: Handles financial transactions via secure gateways and manages the 'Eco-Points' loyalty system for sustainable travel.
- **Sustainability Analytics Service**: Asynchronously calculates CO2 savings for every completed trip and updates user impact dashboards.

## Data Models

- **User**:
  - id (UUID): Unique identifier.
  - 
ame (String): Full name.
  - email (String): Unique email address.
  - ole (Enum): RIDER, DRIVER, or ADMIN.
  - eco_points (Integer): Total loyalty points earned.

- **Ride**:
  - id (UUID): Unique identifier.
  - ider_id (UUID): Reference to the User (Rider).
  - driver_id (UUID): Reference to the User (Driver).
  - status (Enum): REQUESTED, ON_TRIP, COMPLETED, CANCELLED.
  - co2_saved (Decimal): Kilograms of CO2 saved during the trip.

- **Payment**:
  - id (UUID): Unique identifier.
  - ide_id (UUID): Reference to the Ride.
  - mount (Decimal): Total cost of the ride.
  - status (Enum): PENDING, SUCCESSFUL, FAILED.

## API Endpoints

### 1. User Registration
- **Endpoint**: POST /api/v1/auth/register
- **Parameters**: 
ame, email, password, ole
- **Description**: Creates a new user account.

### 2. Search for Eco-Rides
- **Endpoint**: POST /api/v1/rides/search
- **Parameters**: pickup_location (lat/lng), destination (lat/lng)
- **Description**: Returns a list of nearby available electric vehicles and estimated CO2 savings.

### 3. Book a Ride
- **Endpoint**: POST /api/v1/rides/book
- **Parameters**: ider_id, ehicle_id, oute_id
- **Description**: Confirms the booking and notifies the driver.

### 4. Process Payment
- **Endpoint**: POST /api/v1/payments/charge
- **Parameters**: ide_id, payment_method_token, mount
- **Description**: Executes the financial transaction and triggers eco-point calculation.
