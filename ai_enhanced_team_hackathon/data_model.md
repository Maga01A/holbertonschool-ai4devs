# Data Model - EcoRide MVP

## Entity 1: User
İstifadəçi profillərini və eko-xalları idarə edir.
- id: UUID (Primary Key)
- username: String
- email: String (Unique)
- user_type: Enum (RIDER, DRIVER, ADMIN)
- eco_points_balance: Integer

## Entity 2: Vehicle
Nəqliyyat vasitələrinin texniki və emissiya məlumatları.
- id: UUID (Primary Key)
- owner_id: UUID (Foreign Key -> User.id)
- model_name: String
- vehicle_type: Enum (EV, HYBRID, CONVENTIONAL)
- emission_rate: Float (CO2 grams per km)

## Entity 3: RideSession
Hər bir səfərin detalları və ekoloji təsiri.
- id: UUID (Primary Key)
- rider_id: UUID (Foreign Key -> User.id)
- driver_id: UUID (Foreign Key -> User.id)
- distance_km: Float
- carbon_saved: Float (Calculated amount)