# Specification Review and Refinement - EcoRide Platform

This document highlights the improvements made to the initial technical specifications to ensure clarity, technical precision, and consistency across the EcoRide ecosystem.

## 1. System Components
**Original**: Ride Matching Service pairs riders with available electric vehicles.  
**Refined**: **Eco-Matching Engine**: A low-latency service that utilizes a geospatial indexing algorithm (e.g., H3 or S2) to pair riders with EVs based on battery level, proximity, and carbon-reduction KPIs.

**Original**: Payment & Rewards Service handles financial transactions and loyalty points.  
**Refined**: **Transaction & Loyalty Management Service**: A PCI-DSS compliant service that manages secure payment processing via Stripe/Braintree and handles the asynchronous distribution of 'Eco-Points' via an event-driven architecture.

## 2. Data Models
**Original**: **User**: id, name, email, role, eco_points  
**Refined**: **User Entity**:
- uuid: Primary Key (UUID v4)
- ull_name: String (Max 100 chars)
- email: String (Unique, Indexed)
- ole_id: Foreign Key to Roles table (RIDER, DRIVER, ADMIN)
- loyalty_tier: Enum (BRONZE, SILVER, GOLD) based on eco_points balance.

**Original**: **Ride**: id, driver_id, passenger_ids, status  
**Refined**: **Ride Session**:
- ide_id: Primary Key
- driver_uuid: Reference to Driver (Nullable before matching)
- ider_uuid: Reference to Rider
- status: Enum (PENDING_MATCH, EN_ROUTE, ACTIVE, COMPLETED, CANCELLED)
- 	elemetry_data: JSONB (Stores route pathing and real-time CO2 savings).

## 3. API Endpoints
**Original**: POST /api/v1/rides/search { pickup_location, destination }  
**Refined**: POST /api/v1/rides/discover 
- **Request Body**: { "origin": { "lat": Float, "lng": Float }, "destination": { "lat": Float, "lng": Float }, "preference": "fastest_eco" }
- **Response**: 200 OK with a list of available ehicle_objects including estimated co2_offset and rrival_eta.

**Original**: POST /api/v1/payments/charge { ride_id, amount }  
**Refined**: POST /api/v1/billing/process-transaction
- **Headers**: Idempotency-Key (To prevent double charging)
- **Request Body**: { "ride_id": UUID, "payment_method_id": String, "currency": "USD" }
- **Description**: Executes a secure charge and updates the ride status to 'PAID' upon successful gateway response.

## 4. User Stories
**Original**: As a rider, I want to see my CO2 savings so that I feel good about using the app.  
**Refined**: As a rider, I want a real-time sustainability dashboard showing my cumulative CO2 offset in kilograms, so that I can track my environmental impact and qualify for loyalty rewards.
