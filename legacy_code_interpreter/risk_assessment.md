# Risk Assessment Report - Legacy Migration Project

| Risk Title | Description | Severity | Impact & Mitigation Notes |
| :--- | :--- | :--- | :--- |
| **Hardcoded Credentials** | Database passwords and API keys are stored in plaintext within db_config.ini. | **High** | **Impact:** Unauthorized data access or full DB compromise if source code is leaked. **Mitigation:** Move to ENV variables or Vault. |
| **Missing Automated Tests** | Core financial modules lack unit tests. | **High** | **Impact:** High risk of regression errors during migration, leading to incorrect balance calculations. **Mitigation:** Implement Jest/PyTest suites. |
| **Data Sync Inconsistency** | No distributed locking between DB2 and PostgreSQL. | **High** | **Impact:** Partial updates can lead to "ghost" transactions where money is deducted but not credited. **Mitigation:** Use 2-Phase Commit or Sagas. |
| **Deprecated Encryption** | Use of MD5 for user passwords. | **Medium** | **Impact:** Susceptibility to rainbow table attacks. Compromised accounts can lead to identity theft. **Mitigation:** Re-hash using Argon2. |
| **Tight Monolithic Coupling** | Business logic is hardcoded into SQL queries. | **Medium** | **Impact:** Makes it nearly impossible to scale specific features independently or switch databases. **Mitigation:** Abstract logic into Service Layers. |
| **Lack of Structured Logging** | Logs are unstructured strings in stdout. | **Low** | **Impact:** Increased Mean Time to Recovery (MTTR); incident response is delayed because errors aren't searchable. **Mitigation:** Use Winston/Loguru for JSON logging. |
