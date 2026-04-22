# Data Model - Smart Task Prioritizer

Bu bölmədə tətbiqin MVP versiyası üçün istifadə olunan əsas verilənlər strukturu təsvir edilmişdir.

## Entity 1: Task (Tapşırıq)
Tapşırıqların əsas xüsusiyyətlərini və prioritet dərəcəsini saxlayır.

| Attribute | Type | Description |
| :--- | :--- | :--- |
| id | UUID | Tapşırıq üçün unikal identifikasiya kodu |
| title | String | Tapşırığın adı/başlığı |
| deadline | Date | Tapşırığın son icra tarixi |
| effort | Integer | Sərf olunacaq zəhmət (1-5 arası) |
| priorityScore | Float | Alqoritm tərəfindən hesablanmış vaciblik balı |
| status | Enum | 'todo', 'doing' və ya 'done' |

## Entity 2: Category (Kateqoriya)
Tapşırıqları qruplaşdırmaq üçün istifadə olunur.

| Attribute | Type | Description |
| :--- | :--- | :--- |
| id | UUID | Kateqoriya üçün unikal kod |
| name | String | Kateqoriya adı (məs: İş, Şəxsi, Təhsil) |
| colorCode | String | UI-da görünəcək rəng kodu (Hex formatında) |

## Entity 3: UserSettings (İstifadəçi Ayarları)
İstifadəçinin tətbiq daxilindəki fərdi seçimlərini saxlayır.

| Attribute | Type | Description |
| :--- | :--- | :--- |
| id | UUID | Ayarlar üçün unikal kod |
| theme | String | 'light' (açıq) və ya 'dark' (tünd) rejim seçimi |
| taskLimit | Integer | Aktiv saxlanıla biləcək maksimum tapşırıq sayı |