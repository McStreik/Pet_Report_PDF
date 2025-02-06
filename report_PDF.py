import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
from fpdf import FPDF
import os


# Функция для чтения данных из CSV-файла
def load_data(file_path):
    try:
        df = pd.read_csv(file_path)
        print("Данные успешно загружены.")
        return df
    except Exception as e:
        print(f"Оштбка при загрузке данных: {e}")
        return None


# Функция анализа данных
def analyze_data(df):
    if df is None or df.empty:
        print("Нет данных для анализа.")
        return {}

    # Основные метрики
    total_sales = df["amount"].sum()
    average_sales = df["amount"].mean()
    top_products = (
        df.groupby("product")["amount"].sum().sort_values(ascending=False).head(5)
    )

    return {
        "total_sales": total_sales,
        "average_sales": average_sales,
        "top_products": top_products,
    }


# Функция для создания графиков
def create_charts(data, output_dir="charts"):
    import os

    os.makedirs(output_dir, exist_ok=True)

    # График топ продуктов
    plt.figure(figsize=(8, 4))
    sns.barplot(
        x=data["top_products"].values, y=data["top_products"].index, palette="viridis"
    )
    plt.title("Топ 5 продуктов по продажам")
    plt.xlabel("Объем продаж")
    plt.ylabel("Продукт")
    plt.tight_layout()
    plt.savefig(f"{output_dir}/top_products.png")
    plt.close()

    # Гистограмма распределения продаж

    plt.figure(figsize=(8, 4))
    sns.histplot(df["amount"], bins=20, kde=True, color="skyblue")
    plt.title("Распределение продаж")
    plt.xlabel("Объем продаж")
    plt.ylabel("Количество")
    plt.tight_layout()
    plt.savefig(f"{output_dir}/sales_distribution.png")
    plt.close()

    print("Графики успешно созданы.")


# Генерация PDF-отчета при помощи библиотеки fpdf
def generate_pdf(data, charts_dir="charts", output_file="report.pdf"):
    pdf = FPDF()
    pdf.add_page()
    pdf.set_auto_page_break(auto=True, margin=15)

    # Установка шрифта, поддерживающего Unicode
    pdf.add_font("DejaVu", "", "DejaVuSans.ttf", uni=True)  # Скачай шрифт DejaVuSans.ttf
    pdf.set_font("DejaVu", size=12)

    # Заголовок
    pdf.cell(0, 10, "Отчет о продажах", ln=True, align="C")
    pdf.ln(10)

    # Метрики
    pdf.cell(0, 10, f"Общая выручка: {data['total_sales']:.2f}", ln=True)
    pdf.cell(0, 10, f"Средняя выручка: {data['average_sales']:.2f}", ln=True)
    pdf.ln(10)

    # Таблица топ продуктов
    pdf.cell(50, 10, "Топ 5 продуктов:", ln=True)
    for product, amount in data["top_products"].items():
        pdf.cell(0, 10, f"{product}: {amount:.2f}", ln=True)
    pdf.ln(10)

    # Добавление графиков
    pdf.image(f"{charts_dir}/top_products.png", x=10, y=None, w=180)
    pdf.ln(10)
    pdf.image(f"{charts_dir}/sales_distribution.png", x=10, y=None, w=180)

    # Сохранение PDF
    pdf.output(output_file)
    print(f"Отчет сохранен в файле {output_file}.")


# Основной скрипт
if __name__ == "__main__":
    # Путь к файлу с данными
    file_path = "sales.csv"

    # Загрузка данных
    df = load_data(file_path)
    if df is None:
        exit()

    # Анализ данных
    analysis_results = analyze_data(df)

    # Создание графиков
    create_charts(analysis_results)

    # Генерация PDF-отчета
    generate_pdf(analysis_results, output_file="sales_report.pdf")
