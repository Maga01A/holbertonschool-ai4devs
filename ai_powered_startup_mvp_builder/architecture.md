# System Architecture - EcoRide

## High-Level Diagram Description
EcoRide MVP sistemi mikroservis arxitekturasina ?saslanan modulyar strukturda qurulacaq:

1. **Frontend Layer**: React Native (iOS/Android) v? Admin Dashboard (React.js).
2. **API Gateway**: Bütün sorgulari idar? ed?n v? müvafiq servisl?r? yönl?ndir?n m?rk?zi giris.
3. **Core Services**:
   - **Matching Service**: S?rnisin v? sürücül?ri esl?sdir?n alqoritm.
   - **Sustainability Engine**: Karbon hesablamalari v? hesabatlari idar? ed?n servis.
   - **User & Auth Service**: Istifad?çi profill?ri v? t?hlük?sizlik.
4. **Data Layer**:
   - **PostgreSQL (PostGIS)**: Cografi koordinatlar v? ?sas m?lumatlar üçün.
   - **Redis**: Real-time sürücü izl?m? (location tracking) üçün.
5. **External Integrations**: Stripe (Öd?nis) v? Google Maps API (X?rit?).
