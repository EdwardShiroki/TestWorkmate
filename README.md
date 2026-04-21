# YouTube Metrics CLI

CLI-приложение читает один или несколько CSV-файлов с метриками видео и строит отчёт.

Доступный отчёт:
- `clickbait` - видео, где `ctr > 15` и `retention_rate < 40`.

В выводе таблица с колонками:
- `title`
- `ctr`
- `retention_rate`

Сортировка: по `ctr` по убыванию.

## Примеры запуска

```bash
python main.py --files stats1.csv --report clickbait
python main.py --files stats1.csv stats2.csv --report clickbait
```

## Скриншоты 
- test_out - с правильными аргументами
- invalid_file -  неправильное имя файла
- invalid_report - неправильный вид отчета