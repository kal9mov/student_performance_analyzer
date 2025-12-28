# API Reference

## StudentAnalyzer

Класс `StudentAnalyzer` (в `src/analyzer.py`) отвечает за загрузку и обработку данных студентов.

### `load_data(filepath)`
Загружает данные из CSV файла.
- **Аргументы:** `filepath` (str) - путь к файлу.
- **Возвращает:** `True` если успешно, иначе `False`.

### `calculate_average_scores()`
Считает средний балл по каждому предмету для всего класса.
- **Возвращает:** `pandas.Series` со средними значениями.

### `identify_at_risk_students(threshold=60)`
Находит студентов, чей средний балл ниже порогового значения.
- **Аргументы:** `threshold` (float) - порог (по умолчанию 60).
- **Возвращает:** `pandas.DataFrame` со списком студентов.

---

## Visualizer

Модуль `src/visualizer.py` для визуализации данных.

### `plot_score_distribution(df, output_path)`
Строит гистограмму распределения средних оценок и сохраняет её в файл.
- **Аргументы:**
  - `df` (pandas.DataFrame): Данные студентов.
  - `output_path` (str): Путь для сохранения изображения (png).
