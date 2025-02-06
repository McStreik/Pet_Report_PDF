Генератор PDF-отчетов о продажах

 Описание

Этот проект представляет собой инструмент для автоматической генерации PDF-отчетов на основе данных из CSV-файла. Отчет включает основные метрики (общую выручку, среднюю выручку, топ продуктов) и графики для визуализации данных.

Технологии

- Python — язык программирования.
- Pandas — для обработки данных.
- Matplotlib/Seaborn — для создания графиков.
- FPDF2 — для создания PDF-документов.

 Установка

1. Установите Python: Убедитесь, что у вас установлена версия Python 3.9–3.11. Скачать можно [здесь](https://www.python.org/downloads/).

2. Создайте виртуальное окружение:
  
   python -m venv venv

3. Активируйте виртуальное окружение:
Для Windows:
venv\Scripts\activate

Для Linux/macOS:
source venv/bin/activate

4. Установите зависимости:
pip install numpy pandas matplotlib seaborn fpdf2

5. Подготовте файл:
sales.csv  с колонами product и amount.
Пример структуры:
product,amount
Product A,100
Product B,200
Product C,150

6. Запустите скрипт:
python report_PDF.py


