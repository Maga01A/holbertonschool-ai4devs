# Legacy Code Interpreter - Module Explanations

## 1. Migration Engine (migration_core.py)
Köhn? sistemd?n m?lumatlarin PostgreSQL-? köçürülm?sini t?min ed?n ?sas modul. Data scrubbing v? tip çevrilm?l?ri burada aparilir.

## 2. Security & Encryption (security_vault.py)
MD5-d?n Argon2-y? keçid v? sifr?l?nmis m?lumatlarin desifr? edilm?si üçün istifad? olunur.

## 3. Database Layer (db_connector.py)
Legacy DB2 v? müasir PostgreSQL veril?nl?r bazalari il? ?laq?ni idar? edir. Distributed locking mexanizmini d?st?kl?yir.

## 4. Logging & Monitoring (audit_logger.py)
Sistem x?talarini v? miqrasiya audit loqlarini m?rk?zl?sdirilmis JSON formatinda saxlayir.
