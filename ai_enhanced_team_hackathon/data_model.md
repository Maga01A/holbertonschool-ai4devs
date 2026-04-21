# Data Model - EcoRide MVP

## 1. User Entity
Istifad?çi profill?rini v? eko-xallari idar? edir.
- id: UUID (PK)
- username: String
- email: String (Unique)
- user_type: Enum (RIDER, DRIVER, ADMIN)
- eco_points_balance: Integer

## 2. Vehicle Entity
N?qliyyat vasit?l?rinin texniki v? emissiya m?lumatlari.
- id: UUID (PK)
- owner_id: UUID (FK -> User.id)
- model_name: String
- ehicle_type: Enum (EV, HYBRID, CONVENTIONAL)
- emission_rate: Float (CO2 grams per km)

## 3. RideSession Entity
H?r bir s?f?rin detallari v? ekoloji t?siri.
- id: UUID (PK)
- ider_id: UUID (FK -> User.id)
- driver_id: UUID (FK -> User.id)
- distance_km: Float
- carbon_saved: Float (Calculated by AI engine)
- 	imestamp: DateTime
