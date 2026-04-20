# Risk Assessment – Legacy Banking Transaction System

Bu sənəd COBOL sisteminin modern Java Spring arxitekturasına keçidi zamanı qarşılaşa biləcəyimiz əsas riskləri və onların ağırlıq dərəcəsini təsvir edir.

| Risk Description | Severity | Impact Notes |
| :--- | :--- | :--- |
| **Hardcoded Business Rules** | High | Limits like 5000.00 are hardcoded. Changing them requires re-compiling legacy code, leading to operational delays. |
| **Lack of Automated Regression Tests** | High | No automated test suite exists for the COBOL logic. Any change in the Java implementation risks breaking edge-case business rules. |
| **Knowledge Silos & Retirement** | High | The original COBOL developers have retired. Understanding undocumented side-effects of the code depends heavily on AI interpretation. |
| **Data Inconsistency during Sync** | Medium | During the Strangler Fig migration, keeping the DB2 (Legacy) and PostgreSQL (Modern) databases in sync may cause temporary balance mismatches. |
| **Monolithic Coupling** | Medium | Logic and Data Access are tightly mixed. Refactoring into microservices is difficult without breaking the internal program flow. |
| **Legacy Decimal Precision Errors** | Medium | COBOL's `PIC 9(10)V99` and Java's `BigDecimal` handle rounding differently. Small discrepancies can accumulate over millions of transactions. |
| **Insufficient Logging** | Low | The current `LOG-TRANSACTION` routine provides minimal data, making it hard to debug failed migrations in real-time. |

## Mitigation Strategy
- **High Severity Risks:** Prioritized for immediate refactoring and 100% unit test coverage in the new Java environment.
- **Medium Severity Risks:** Handled through phased migration (Strangler Fig Pattern) and continuous data validation scripts.