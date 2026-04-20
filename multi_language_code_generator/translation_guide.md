# Translation Guide: Order Processor (Python, JS, Go)

Bu b?l?dçi eyni biznes m?ntiqinin müxt?lif proqramlasdirma dill?ri arasinda dasinmasi zamani yaranan ?sas f?rql?ri v? idiomlari izah edir.

## Python ? JavaScript (Node.js)
- **Idiomatic Differences**: Python-da snake_case (process_order) standart oldugu halda, JavaScript-d? camelCase (processOrder) istifad? olunur.
- **Data Structures**: Python lüg?tl?ri (dicts) birbasa JS obyektl?rin? (objects) çevrilir.
- **Exporting**: Python-da if __name__ == "__main__": blokundan istifad? olunsa da, JS-d? dig?r fayllarin (testl?rin) girisi üçün module.exports t?l?b olunur.

## Python ? Go
- **Typing**: Python dinamik tipli dildir, lakin Go-da h?r bir d?yis?n v? funksiya üçün ciddi tip t?yini (strict typing) t?l?b olunur.
- **Structs**: Python-un lütf?n qaytardigi lüg?t (dict), Go-da JSON tag-l?ri olan xüsusi bir struct (OrderResponse) t?r?find?n qarsilanmalidir.
- **Control Flow**: Python-un ternary operatoru (A if condition else B) Go-da yoxdur; burada mütl?q if-else blokundan istifad? edilm?lidir.

## Common Pitfalls (Ümumi T?l?l?r)
- **Zero Values**: Go-da inisializasiya olunmamis d?yis?nl?r avtomatik "zero value" alir (m?s?l?n, float üçün 0.0), Python-da is? None v? ya x?ta il? qarsilasa bil?rsiniz.
- **Asynchronicity**: JS v? ya Python-da asinxron ?m?liyyatlar (async/await) Go-daki goroutines m?ntiqind?n f?rqli isl?yir.
