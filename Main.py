import tkinter as tk
from tkinter import filedialog, messagebox
import pandas as pd
import matplotlib.pyplot as plt


# Главный класс приложения
class HealthApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Ведение здоровья пациента")

        self.data = pd.DataFrame(
            columns=["Дата", "Давление", "Сахар", "Упражнение", "Продолжительность", "Комментарии"])

        self.create_widgets()

    def create_widgets(self):
        # Поля для ввода данных
        self.date_label = tk.Label(self.root, text="Дата")
        self.date_label.grid(row=0, column=0)
        self.date_entry = tk.Entry(self.root)
        self.date_entry.grid(row=0, column=1)

        self.pressure_label = tk.Label(self.root, text="Давление")
        self.pressure_label.grid(row=1, column=0)
        self.pressure_entry = tk.Entry(self.root)
        self.pressure_entry.grid(row=1, column=1)

        self.sugar_label = tk.Label(self.root, text="Сахар в крови")
        self.sugar_label.grid(row=2, column=0)
        self.sugar_entry = tk.Entry(self.root)
        self.sugar_entry.grid(row=2, column=1)

        self.exercise_label = tk.Label(self.root, text="Упражнение")
        self.exercise_label.grid(row=3, column=0)
        self.exercise_entry = tk.Entry(self.root)
        self.exercise_entry.grid(row=3, column=1)

        self.duration_label = tk.Label(self.root, text="Продолжительность (мин)")
        self.duration_label.grid(row=4, column=0)
        self.duration_entry = tk.Entry(self.root)
        self.duration_entry.grid(row=4, column=1)

        self.comment_label = tk.Label(self.root, text="Комментарии")
        self.comment_label.grid(row=5, column=0)
        self.comment_entry = tk.Entry(self.root)
        self.comment_entry.grid(row=5, column=1)

        # Кнопка для добавления данных
        self.add_button = tk.Button(self.root, text="Добавить данные", command=self.add_data)
        self.add_button.grid(row=6, column=0, columnspan=2)

        # Кнопка для загрузки CSV
        self.load_button = tk.Button(self.root, text="Загрузить данные из CSV", command=self.load_data)
        self.load_button.grid(row=7, column=0, columnspan=2)

        # Кнопка для анализа данных
        self.analyze_button = tk.Button(self.root, text="Анализировать данные", command=self.analyze_data)
        self.analyze_button.grid(row=8, column=0, columnspan=2)

    def add_data(self):
        # Добавляем данные в DataFrame
        new_data = {
            "Дата": self.date_entry.get(),
            "Давление": self.pressure_entry.get(),
            "Сахар": self.sugar_entry.get(),
            "Упражнение": self.exercise_entry.get(),
            "Продолжительность": self.duration_entry.get(),
            "Комментарии": self.comment_entry.get()
        }

        self.data = self.data.append(new_data, ignore_index=True)

        # Очистка полей ввода
        self.date_entry.delete(0, tk.END)
        self.pressure_entry.delete(0, tk.END)
        self.sugar_entry.delete(0, tk.END)
        self.exercise_entry.delete(0, tk.END)
        self.duration_entry.delete(0, tk.END)
        self.comment_entry.delete(0, tk.END)

    def load_data(self):
        # Загрузка данных из CSV
        file_path = filedialog.askopenfilename(filetypes=[("CSV files", "*.csv")])
        if file_path:
            try:
                new_data = pd.read_csv(file_path)
                self.data = pd.concat([self.data, new_data], ignore_index=True)
                messagebox.showinfo("Успех", "Данные успешно загружены")
            except Exception as e:
                messagebox.showerror("Ошибка", f"Не удалось загрузить данные: {e}")

    def analyze_data(self):
        # Анализ данных и вывод графиков
        if not self.data.empty:
            fig, ax = plt.subplots()
            ax.plot(self.data["Дата"], self.data["Давление"], label="Давление")
            ax.plot(self.data["Дата"], self.data["Сахар"], label="Сахар")
            ax.set_xlabel('Дата')
            ax.set_ylabel('Значения')
            ax.legend()
            plt.xticks(rotation=45)
            plt.tight_layout()
            plt.show()
        else:
            messagebox.showwarning("Предупреждение", "Нет данных для анализа")


# Создание окна
root = tk.Tk()
app = HealthApp(root)
root.mainloop()
