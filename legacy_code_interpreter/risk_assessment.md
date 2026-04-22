# Risk Assessment Report - Legacy Migration Project

Bu hesabat köhn? sistemin (legacy system) modernizasiyasi zamani askar edilmis texniki v? t?hlük?sizlik riskl?rini ?ks etdirir.

| Risk Title | Description | Severity | Mitigation Notes |
| :--- | :--- | :--- | :--- |
| **Hardcoded Credentials** | Veril?nl?r bazasi giris m?lumatlari db_config.ini faylinda açiq s?kild? saxlanilir. | **High** | T?cili olaraq Environment Variables v? ya Secret Manager istifad?sin? keçilm?lidir. |
| **Missing Automated Tests** | ?sas maliyy? tranzaksiya modullari üçün heç bir avtomatlasdirilmis test mövcud deyil. | **High** | Miqrasiya baslamazdan ?vv?l ?n azi 80% coverage t?min ed?n unit testl?r yazilmalidir. |
| **Data Sync Inconsistency** | DB2 v? PostgreSQL-? eyni vaxtda yazilis zamani tranzaksional kilidl?m? (locking) yoxdur. | **High** | Distributed transaction management v? ya SAGA pattern t?tbiq edilm?lidir. |
| **Deprecated Encryption** | Istifad?çi sifr?l?ri üçün artiq t?hlük?siz hesab olunmayan MD5 alqoritmi istifad? olunur. | **Medium** | Bütün sifr?l?r BCrypt v? ya Argon2 alqoritmi il? yenid?n hash olunmalidir. |
| **Tight Coupling** | Biznes m?ntiqi v? SQL sorgulari bir-birin? d?rind?n baglidir (Monolith). | **Medium** | Kodun refaktorinqi v? API qatinin ayrilmasi üçün xidm?t (Service) pattern-i t?tbiq olunmalidir. |
| **Lack of Structured Logging** | Loqlar m?rk?zl?sdirilm?mis v? qeyri-struktur s?kild? standart output-a çixarilir. | **Low** | JSON formatinda m?rk?zl?sdirilmis loqlama sistemi (m?s. ELK stack) qurulmalidir. |

## Risk Xülas?si
Askar edilmis riskl?rin 50%-i **Yüks?k (High)** ciddilik d?r?c?sin? malikdir. Bu riskl?r aradan qaldirilmadan miqrasiya prosesinin növb?ti m?rh?l?sin? keçid m?lumat itkisin? v? ya t?hlük?sizlik k?sirl?rin? s?b?b ola bil?r.
