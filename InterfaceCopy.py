import sys
from PyQt6.QtWidgets import QApplication, QWidget, QPushButton, QLabel, QLineEdit
from PyQt6.QtGui import QGuiApplication


class MyWindow(QWidget):
    def __init__(self):
        super().__init__()

        # Получаем информацию о размере экрана
        self.screen = QGuiApplication.primaryScreen()
        self.screen_geometry = self.screen.geometry()
        self.screen_width = self.screen_geometry.width()
        self.screen_height = self.screen_geometry.height()

        # Устанавливаем минимальный размер окна
        self.min_width = int(self.screen_width * 0.3)
        self.min_height = int(self.screen_height * 0.6)
        self.setMinimumSize(self.min_width, self.min_height)
        self.setWindowTitle("Окно с минимальным размером 30% от экрана")
        self.setGeometry(100, 100, self.min_width, self.min_height)

        # Создаем кнопки для переключения
        self.create_buttons()

        # Создаем разделы
        self.create_sections()

        # Изначально показываем раздел 1
        self.section1.show()
        self.section2.hide()

    def create_buttons(self):
        """Создаёт кнопки для переключения разделов."""
        button_size = int(self.screen_width * 0.05 * 0.5)
        button_padding = button_size / 2  # Размер кнопки
        self.button1 = QPushButton(self)
        self.button2 = QPushButton(self)

        self.button1.setFixedSize(button_size, button_size)
        self.button2.setFixedSize(button_size, button_size)

        # Устанавливаем позиции кнопок
        self.button1.setGeometry(button_padding, 30, button_size, button_size)
        self.button2.setGeometry(button_padding, 200, button_size, button_size)

        # Связываем кнопки с функциями
        self.button1.clicked.connect(self.show_section1)
        self.button2.clicked.connect(self.show_section2)

    def create_sections(self):
        """Создаёт два раздела приложения."""
        # Раздел 1
        self.section1 = self.create_section("rgb(200, 255, 200)", 150, 30, self.min_width - 180, self.min_height - 60)
        self.add_patient_data_section(self.section1)

        # Раздел 2
        self.section2 = self.create_section("rgb(173, 216, 230)", 150, 30, self.min_width - 180, self.min_height - 60)
        self.add_exercise_section(self.section2)

    def create_section(self, background_color, x, y, width, height):
        """Создаёт раздел с заданными параметрами."""
        section = QWidget(self)
        section.setGeometry(x, y, width, height)
        section.setStyleSheet(f"background-color: {background_color}; border-radius: 15px;")
        return section

    def add_patient_data_section(self, section):
        """Добавляет элементы в раздел данных пациента."""
        label1 = QLabel("Данные пациента", section)
        label1.move(20, 20)
        label1.setStyleSheet("font-size: 30px; font-family: 'Roboto', sans-serif; font-weight: bold;")

        label_input = QLabel("Имя:", section)
        label_input.move(20, 100)
        label_input.setStyleSheet("font-size: 18px; font-family: 'Roboto', sans-serif;")

        input_field = QLineEdit(section)
        input_field.move(150, 100)
        input_field.setFixedWidth(int(self.screen_width * 0.1))
        input_field.setStyleSheet("background-color: white;")

    def add_exercise_section(self, section):
        """Добавляет элементы в раздел учета упражнений."""
        label2 = QLabel("Учет упражнений", section)
        label2.move(20, 20)
        label2.setStyleSheet("font-size: 30px; font-family: 'Roboto', sans-serif; font-weight: bold;")

    def show_section1(self):
        """Показывает первый раздел и скрывает второй."""
        self.section1.show()
        self.section2.hide()

    def show_section2(self):
        """Показывает второй раздел и скрывает первый."""
        self.section1.hide()
        self.section2.show()


if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = MyWindow()
    window.show()
    sys.exit(app.exec())
