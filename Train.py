import sys
from PyQt6.QtWidgets import QApplication, QWidget, QVBoxLayout, QHBoxLayout, QLabel, QComboBox, QLineEdit, QPushButton, QListWidget, QMessageBox
from CryptoUtilsTrain import CryptoUtils

class ExerciseApp(QWidget):
    def __init__(self):
        super().__init__()

        self.setWindowTitle("Учет упражнений")
        self.setGeometry(100, 100, 400, 300)

        # Список упражнений
        self.exercises = ["Отжимания", "Приседания", "Подтягивания", "Бег", "Тренировка на пресс"]

        # Инициализация интерфейса
        self.initUI()

        # Создание объекта для работы с шифрованием
        self.crypto_utils = CryptoUtils()

        # Загрузка зашифрованных данных
        self.load_data()

    def initUI(self):
        # Основной вертикальный layout
        main_layout = QVBoxLayout()

        # Заголовок и описание выбора упражнения
        self.label = QLabel("Выберите упражнение:")
        self.label.setStyleSheet("font-size: 18px; font-family: 'Roboto', sans-serif;")
        main_layout.addWidget(self.label)

        # Комбобокс для выбора упражнения
        self.exercise_combo = QComboBox()
        self.exercise_combo.addItems(self.exercises)
        main_layout.addWidget(self.exercise_combo)

        # Поле для ввода данных
        self.data_label = QLabel("Введите данные для упражнения:")
        self.data_label.setStyleSheet("font-size: 18px; font-family: 'Roboto', sans-serif;")
        main_layout.addWidget(self.data_label)

        self.data_entry = QLineEdit()
        self.data_entry.setStyleSheet(
            "font-size: 18px; font-family: 'Roboto', sans-serif; background-color: #f1f1f1; border: 1px solid #ccc; border-radius: 5px; padding: 10px;"
        )
        main_layout.addWidget(self.data_entry)

        # Кнопка для сохранения данных
        self.save_button = QPushButton("Сохранить")
        self.save_button.setStyleSheet(
            "font-size: 18px; font-family: 'Roboto', sans-serif; background-color: #4CAF50; color: white; border-radius: 10px; padding: 10px 20px;"
        )
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

        # Шифрование данных и сохранение в файл
        self.save_encrypted_data(card)

        # Очистка поля ввода
        self.data_entry.clear()

    def save_encrypted_data(self, data):
        """Шифрует данные и сохраняет их в файл."""
        try:
            self.crypto_utils.save_encrypted_data(data)
        except Exception as e:
            print(f"Ошибка при сохранении зашифрованных данных: {e}")

    def load_data(self):
        """Загружает и расшифровывает данные из файла, отображает в списке."""
        try:
            decrypted_data = self.crypto_utils.load_encrypted_data()
            self.card_listbox.addItem(decrypted_data)
        except Exception as e:
            print(f"Ошибка при загрузке и расшифровке данных: {e}")


if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = ExerciseApp()
    window.show()
    sys.exit(app.exec())
