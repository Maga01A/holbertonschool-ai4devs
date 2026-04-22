# Risk Assessment

| Risk | Severity | Notes |
| :--- | :--- | :--- |
| Hardcoded database credentials | High | Found in legacy db_config.ini files. Poses an immediate security vulnerability and data breach risk if the source code is exposed. |
| Missing automated unit tests | High | Core transaction modules have 0% test coverage. High probability of breaking critical edge-case business rules during the migration to modern architecture. |
| Database synchronization inconsistency | High | Dual-writing to DB2 and PostgreSQL during the migration phase lacks distributed transactional locking, risking permanent balance mismatches and data corruption. |
| Deprecated encryption usage | Medium | Relies on outdated MD5 hashing functions for user passwords. Vulnerable to collision attacks; urgently needs an upgrade to secure algorithms like BCrypt. |
| Tight monolithic coupling | Medium | Business logic and database queries are deeply intertwined in the same legacy files, making microservice extraction and API creation highly complex and time-consuming. |
| Lack of structured logging | Low | Current routines output unstructured text to standard output instead of centralized JSON logs, significantly increasing debugging time during production failures. |
