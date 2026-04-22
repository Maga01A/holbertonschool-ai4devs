# Architecture Plan - EcoRide System

## Tech Stack
- **Frontend**: React (Web) / React Native (Mobile)
- **Backend**: Node.js il? Express framework-�.
- **AI Engine**: Python (Flask/FastAPI) - Karbon hesablamalari v? marsrut optimallasdirilmasi ���n.
- **Database**: PostgreSQL (Relational data) + Redis (Real-time tracking).

## System Components
1. **Client Apps**: S?rnisin v? s�r�c� interfeysl?ri.
2. **API Gateway**: T?hl�k?sizlik v? sorgularin y�nl?ndirilm?si.
3. **Matching & Routing Service**: Real-time yerl?sm? m?lumatlarina ?sas?n esl?sm?.
4. **Sustainability # Architecture Plan - EcoRide System

## High-Level System Diagram

```text
+-----------------------+      +-----------------------+
|   Client Apps (UI)    |      |    External APIs      |
| - Rider Application   |      | - Google Maps Routing |
| - Driver Application  |      | - Payment Gateways    |
+-----------------------+      +-----------------------+
            ^                              ^
            | (REST / WebSockets)          |
            v                              v
+------------------------------------------------------+
|                    API Gateway                       |
|           (Security, Rate Limiting, Auth)            |
+------------------------------------------------------+
            ^                              ^
            |                              |
            v                              v
+-----------------------+      +-----------------------+
|  Matching & Routing   |      | Sustainability Engine |
|      (Node.js)        |      |    (Python/Flask)     |
| - Real-time Location  |      | - Carbon Calculation  |
| - Driver Assignment   |      | - Eco-Points Logic    |
+-----------------------+      +-----------------------+
            ^                              ^
            |                              |
            v                              v
+-----------------------+      +-----------------------+
|   Relational Data     |      |   In-Memory Cache     |
|    (PostgreSQL)       |      |       (Redis)         |
| - Users & Vehicles    |      | - Live Driver GeoData |
| - Ride History        |      | - Session States      |
+-----------------------+      +-----------------------+Analytics Service**: H?r s?f?rin karbon ayaq izini hesablayan AI modulu.
5. **Notification Service**: S?f?r statusu v? m�kafatlar bar?d? bildirisl?r.
