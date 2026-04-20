# AI Explanations – Legacy Banking System (COBOL)

## 1. Section: VALIDATE-ACCOUNT (SQL Interface)
- **Plain English**: Bu bölmə verilənlər bazasından (DB2) daxil olan hesab nömrəsinə uyğun məlumatları axtarır və hesabın "Active" (A) olub-olmadığını yoxlayır.
- **Pattern**: `EXEC SQL` daxilində sətir-sətir (prosedural) axtarış və `SQLCODE` yoxlanışı.
- **Issues**: SQL inyeksiyasına qarşı zəiflik (parametr təmizlənməsi görünmür) və yalnız ilk tapılan sətirlə kifayətlənmə.
- **Improvements**: Müasir ORM (Hibernate) istifadə edərək `Optional<Account>` və ya Exception-driven logic tətbiq edilməlidir.

## 2. Section: CHECK-WITHDRAWAL-LIMITS
- **Plain English**: Bu hissə həm hesab balansının yetərli olub-olmadığını, həm də çıxarılan məbləğin 5000.00 limitini keçib-keçmədiyini yoxlayır.
- **Pattern**: Hardcoded rəqəmsal limit (5000.00) birbaşa kodun içinə yazılıb.
- **Issues**: Limit dəyişdirilməli olsa, proqramı yenidən compile etmək lazımdır. Balans yoxlanışı zamanı "pending" (gözləyən) tranzaksiyalar nəzərə alınmır.
- **Improvements**: Limitlər verilənlər bazasından və ya konfiqurasiya servisindən (Spring Cloud Config) oxunmalıdır.

## 3. Section: EVALUATE WS-TXN-TYPE (Main Switch)
- **Plain English**: Tranzaksiyanın növünə (Withdrawal, Deposit, Transfer) görə proqramı fərqli məntiqlərə yönləndirən ana mərkəzdir.
- **Pattern**: COBOL-un `EVALUATE` (Switch-Case) strukturu.
- **Issues**: Yeni bir tranzaksiya növü əlavə edildikdə bütün bu mərkəzi blokun kodunu dəyişmək lazım gəlir (Open-Closed Principle pozulur).
- **Improvements**: **Strategy Pattern** istifadə edilərək hər tranzaksiya növü öz sinfinə (class) ayrılmalıdır.

## 4. Section: MAIN-PROCESS Flow Control
- **Plain English**: Proqramın işə düşmə, icra və təmizlənmə mərhələlərini idarə edən yüksək səviyyəli axındır.
- **Pattern**: Monolitik procedural axın.
- **Issues**: Əgər `INITIALIZE` və ya `PROCESS` zamanı xəta baş verərsə, proqram dərhal dayanır (Stop Run), bu da digər paralel proseslərə təsir edə bilər.
- **Improvements**: `Try-Catch-Finally` blokları və xüsusi `TransactionManager` istifadə edilməlidir.