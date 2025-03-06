import sys
from PyQt6.QtWidgets import QApplication, QWidget, QVBoxLayout, QHBoxLayout, QLabel, QComboBox, QLineEdit, QPushButton, QListWidget, QMessageBox

class ExerciseApp(QWidget):
    def __init__(self):
        super().__init__()

        self.setWindowTitle("Учет упражнений")
        self.setGeometry(100, 100, 400, 300)

        # Список упражнений
        self.exercises = ["Отжимания", "Приседания", "Подтягивания", "Бег", "Тренировка на пресс"]

        # Инициализация интерфейса
        self.initUI()

    def initUI(self):
        # Основной вертикальный layout
        main_layout = QVBoxLayout()

        # Заголовок и описание выбора упражнения
        self.label = QLabel("Выберите упражнение:")
        main_layout.addWidget(self.label)

        # Комбобокс для выбора упражнения
        self.exercise_combo = QComboBox()
        self.exercise_combo.addItems(self.exercises)
        main_layout.addWidget(self.exercise_combo)

        # Поле для ввода данных
        self.data_label = QLabel("Введите данные для упражнения:")
        main_layout.addWidget(self.data_label)

        self.data_entry = QLineEdit()
        main_layout.addWidget(self.data_entry)

        # Кнопка для сохранения данных
        self.save_button = QPushButton("Сохранить")
        self.save_button.clicked.connect(self.save_data)
        main_layout.addWidget(self.save_button)

        # Список для отображения сохраненных карточек
        self.card_listbox = QListWidget()
        main_layout.addWidget(self.card_listbox)

        # Устанавливаем основной layout
        self.setLayout(main_layout)

    def save_data(self):
        exercise = self.exercise_combo.currentText()
        data = self.data_entry.text()

        if not data:
            QMessageBox.warning(self, "Ошибка", "Пожалуйста, введите данные для упражнения.")
            return

        # Создание карточки и добавление в список
        card = f"{exercise}: {data}"
        self.card_listbox.addItem(card)

        # Очистка поля ввода
        self.data_entry.clear()


if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = ExerciseApp()
    window.show()
    sys.exit(app.exec())
