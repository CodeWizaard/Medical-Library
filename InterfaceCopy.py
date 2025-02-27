import sys
from PyQt6.QtWidgets import QApplication, QWidget, QPushButton, QLabel, QLineEdit
from PyQt6.QtGui import QGuiApplication, QColor


class MyWindow(QWidget):
    def __init__(self):
        super().__init__()

        # Получаем информацию о размере экрана
        screen = QGuiApplication.primaryScreen()
        screen_geometry = screen.geometry()
        screen_width = screen_geometry.width()
        screen_height = screen_geometry.height()

        # Вычисляем 30% от ширины и высоты экрана
        min_width = int(screen_width * 0.3)
        min_height = int(screen_height * 0.6)

        # Устанавливаем минимальный размер окна
        self.setMinimumSize(min_width, min_height)

        self.setWindowTitle("Окно с минимальным размером 30% от экрана")
        self.setGeometry(100, 100, min_width, min_height)  # Устанавливаем начальный размер окна

        # Создаем кнопки для переключения
        self.button1 = QPushButton(self)
        self.button2 = QPushButton(self)

        # Делаем кнопки квадратными с фиксированным размером
        screen_w = int(screen_width * 0.05)
        button_size = screen_w * 0.5
        button_padding = button_size / 2  # Размер кнопки
        self.button1.setFixedSize(button_size, button_size)
        self.button2.setFixedSize(button_size, button_size)

        # Устанавливаем позиции кнопок
        self.button1.setGeometry(button_padding, 30, button_size, button_size)
        self.button2.setGeometry(button_padding, 200, button_size, button_size)

        # Связываем кнопки с функциями
        self.button1.clicked.connect(self.show_section1)
        self.button2.clicked.connect(self.show_section2)

        # Создаем два раздела
        self.section1 = QWidget(self)
        self.section1.setGeometry(150, 30, min_width - 180, min_height - 60)
        self.section1.setStyleSheet("background-color: rgb(200, 255, 200); border-radius: 15px;")  # Светло-зеленый с закруглениями
        label1 = QLabel("Данные пациента", self.section1)  # Заголовок для первого раздела
        label1.move(20, 20)
        label1.setStyleSheet("font-size: 30px; font-family: 'Roboto', sans-serif; font-weight: bold;")  # Новый шрифт Roboto

        # Добавляем QLabel и QLineEdit на первый виджет
        label_input = QLabel("Введите имя:", self.section1)
        label_input.move(20, 100)
        label_input.setStyleSheet("font-size: 18px; font-family: 'Roboto', sans-serif;")

        input_field = QLineEdit(self.section1)
        input_field.move(150, 100)
        input_field.setFixedWidth(min_width - 200)
        input_field.setStyleSheet("background-color: white;")  # Белый фон для поля ввода

        self.section2 = QWidget(self)
        self.section2.setGeometry(150, 30, min_width - 180, min_height - 60)
        self.section2.setStyleSheet("background-color: rgb(173, 216, 230); border-radius: 15px;")  # Светло-синий с закруглениями
        label2 = QLabel("Учет упражнений", self.section2)  # Заголовок для второго раздела
        label2.move(20, 20)
        label2.setStyleSheet("font-size: 30px; font-family: 'Roboto', sans-serif; font-weight: bold;")  # Новый шрифт Roboto

        # Изначально показываем раздел 1
        self.section1.show()
        self.section2.hide()

    def show_section1(self):
        self.section1.show()
        self.section2.hide()

    def show_section2(self):
        self.section1.hide()
        self.section2.show()


if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = MyWindow()
    window.show()
    sys.exit(app.exec())
