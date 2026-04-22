# Legacy Code Interpreter Documentation

## System Architecture
Sistem köhn? monolit kod bazalarini müasir mikroxidm?t arxitekturasina çevirm?k üçün n?z?rd? tutulub.

### Major Modules:
1.  **Core Interpreter**: Legacy skriptl?ri analiz edir v? onlari müasir obyekt yönümlü koda (OOP) map edir.
2.  **Migration Pipeline**: M?lumatlarin DB2-d?n PostgreSQL-? ETL (Extract, Transform, Load) prosesini idar? edir.
3.  **Security Bridge**: Köhn? z?if sifr?l?m? metodlarini (MD5/SHA1) müasir Argon2/AES-256 standartlarina yüks?ldir.
4.  **Audit & Log**: H?r bir ?m?liyyatin JSON formatinda m?rk?zl?sdirilmis auditini aparir.
