# Data Model - EcoRide MVP

## 1. User Entity
Istifad?çil?rin (S?rnisin v? Sürücü) m?lumatlarini saxlayir.
- id: UUID (Primary Key)
- 
ame: String
- email: String (Unique)
- ole: Enum (Rider, Driver, Admin)
- eco_points_balance: Integer

## 2. Vehicle Entity
Sürücül?r? m?xsus avtomobil m?lumatlari.
- id: UUID (Primary Key)
- driver_id: UUID (Foreign Key -> User.id)
- 	ype: Enum (EV, Hybrid, Standard)
- make_model: String
- emission_factor: Float (kq CO2 / km)

## 3. Ride Entity
S?f?r v? karbon q?na?ti m?lumatlari.
- id: UUID (Primary Key)
- ider_id: UUID (Foreign Key -> User.id)
- driver_id: UUID (Foreign Key -> User.id)
- pickup_location: Geometry (Point)
- dropoff_location: Geometry (Point)
- carbon_saved: Float
- status: Enum (Requested, Ongoing, Completed, Cancelled)
