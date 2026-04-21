# Systematic AI-Assisted Bug Hunting Methodology

Bu s?n?d süni intellektin gücünd?n istifad? ed?r?k proqram t?minatindaki x?talari askar etm?k, analiz etm?k v? düz?ltm?k üçün strukturlasdirilmis bir ç?rçiv? t?qdim edir.

---

## 1. Step-by-Step Bug Hunting Process

### Phase 1: Contextual Intake
AI-a kodun yalniz x?tali hiss?sini deyil, onun n? etm?li oldugunu (Business Logic) izah edin.
- **Action**: Kodu, asililiqlari v? gözl?nil?n n?tic?ni t?qdim edin.

### Phase 2: Multi-Dimensional Audit
AI-dan kodu dörd f?rqli bucaqdan analiz etm?sini ist?yin:
1.  **Static Analysis**: Sintaksis v? tip x?talari.
2.  **Logic Flow**: K?nar hallar (edge cases) v? m?ntiqi bosluqlar.
3.  **Security Audit**: OWASP Top 10 v? m?lumat sizmasi riskl?ri.
4.  **Resource Management**: Yaddas sizmasi v? performans darbogazlari.

### Phase 3: Root Cause Verification
AI-in t?klif etdiyi x?tani manual olaraq t?sdiql?yin.
- **Action**: AI-dan h?min x?tani t?krarlamaq üçün bir "Reproduction Script" (PoC) yazmasini ist?yin.

### Phase 4: Iterative Patching
Düz?lisi t?tbiq edin v? AI-a h?min düz?lisin yeni bir x?ta yaradib-yaratmadigini yoxlatdirin (Regression check).

---

## 2. Effective Prompting Templates

### For Security Bugs
> "Analyze the following [LANGUAGE] code for security vulnerabilities. Specifically look for Injection, Broken Access Control, and Sensitive Data Exposure. Provide a severity score (1-10) for each finding. Code: [CODE]"

### For Logic & Edge Cases
> "This function [FUNCTION NAME] is intended to [PURPOSE]. Trace all possible execution paths and identify edge cases where this logic might fail (e.g., null inputs, empty collections, extreme values). Code: [CODE]"

### For Concurrency Issues
> "Review this code for race conditions, deadlocks, and thread-safety issues. Identify shared mutable states and suggest appropriate synchronization primitives. Code: [CODE]"

---

## 3. Bug Analysis Checklist
- [ ] AI-a kodun m?qs?di izah edilibmi?
- [ ] X?tanin harada oldugu (Location) d?qiq mü?yy?n edilibmi?
- [ ] Kök s?b?b (Root Cause) anlanilibmi?
- [ ] T?klif olunan h?ll mövcud arxitekturaya uygundurmu?
- [ ] Düz?lisd?n sonra unit testl?r isl?yirmi?

---

## 4. Bug Prioritization Framework

| Priority | Impact | Action |
| :--- | :--- | :--- |
| **P0 (Critical)** | Data loss, Security breach, System crash | Immediate fix, stop other tasks. |
| **P1 (High)** | Major feature broken, Performance lag | Fix in the current sprint. |
| **P2 (Medium)** | Minor bug, UX inconsistency | Schedule for next sprint. |
| **P3 (Low)** | Code smell, Documentation error | Fix when resources are available. |

---

## 5. Team Collaboration & Knowledge Sharing
1. **Shared AI Log**: Komanda daxilind? AI-in askar etdiyi maraqli x?talari v? ugurlu promptlari m?rk?zi bir i_debug_log.md faylinda saxlayin.
2. **Reviewing AI Fixes**: AI-in t?klif etdiyi bütün düz?lisl?r mütl?q basqa bir proqramçi t?r?find?n (Peer Review) yoxlanilmalidir.
3. **Prompt Library**: Layih?y? xas olan xüsusi promptlari (m?s?l?n, "Check for our custom auth rules") s?n?dl?sdirin.

---

## 6. Real Example from Experience
- **Scenario**: Python-da balans yenil?m? funksiyasi.
- **Issue**: Race condition (iki thread eyni vaxtda pul çixarirdi).
- **AI Solution**: 	hreading.Lock() istifad?si.
- **Manual Adjustment**: Kilidl?m?nin (locking) performans t?sirini azaltmaq üçün kritik bölm?nin (critical section) minimuma endirilm?si.
