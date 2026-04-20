# Codebase Overview – Banking Transaction System (Legacy)

## Project Age
- **Initial Release:** 1988 (Mainframe COBOL implementation)
- **Last Major Update:** 2004 (Integration with early web services)
- **Status:** Legacy / Maintenance Mode

## Size (Metrics)
- **Total LOC:** ~1,200,000 Lines of COBOL Code.
- **Complexity:** Over 450 interconnected copybooks and 2,000 JCL (Job Control Language) scripts.

## Main Dependencies
- **Database:** IBM DB2 (Legacy version)
- **Interface:** CICS (Customer Information Control System) for transaction processing.
- **Communication:** Batch processing via VSAM files.

## Known Issues & Pain Points
1. **Monolithic Architecture:** Core business logic is tightly coupled with data access routines, making it impossible to scale individual modules.
2. **Lack of Automated Testing:** All validation is performed manually or through legacy batch logs, leading to high regression risks.
3. **Knowledge Silos:** Original developers have retired; documentation is sparse and outdated.
4. **Data Redundancy:** Multiple copies of account records across different VSAM files causing occasional consistency issues.