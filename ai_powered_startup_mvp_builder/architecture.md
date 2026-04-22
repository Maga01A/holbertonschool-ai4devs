# System Architecture - Smart Task Prioritizer

Bu sənəd Smart Task Prioritizer tətbiqinin MVP mərhələsi üçün nəzərdə tutulmuş yüksək səviyyəli arxitekturasını təsvir edir.

## High-Level System Diagram
Tətbiqin komponentləri arasındakı qarşılıqlı əlaqə aşağıdakı diaqramda göstərilmişdir:

```mermaid
graph TD
    User((İstifadəçi)) -->|Daxil olur| UI[Frontend Layer: HTML/JS/CSS]
    UI -->|Məlumat göndərir| Engine[Priority Engine: JS Məntiqi]
    Engine -->|Hesablayır| Score[Priority Scoring Algorithm]
    UI -->|Yadda saxlayır/Yükləyir| Storage[Storage Layer: Browser LocalStorage]
    UI -->|Fayl yaradır| Export[Export Module: CSV Generator]