# Legacy Module Documentation

## Core Engine (legacy_engine.py)
Bu modul sistemin ?sas m?ntiqini v? m?lumat emalini idar? edir. 
- **Giris**: JSON formatinda xam data.
- **Çixis**: Emal edilmis v? validasiya olunmus lüg?t (dictionary).

## Authentication Handler (auth.py)
Köhn? sistemin istifad?çi giris-çixisini idar? ed?n moduldur.
- **Method**: MD5-?sasli sifr?l?m? istifad? edir (T?hlük?sizlik riski: Modernizasiya zamani SHA-256-ya keçid tövsiy? olunur).
- **Session**: Stateful session idar?etm?si.

## Database Connector (db_connector.py)
Legacy SQL sorgularini icra ed?n moduldur. Birbasa SQL inyeksiyasina qarsi h?ssas ola bil?c?yi üçün yeni versiyada ORM istifad?si planlasdirilir.
