import sys
from PyQt6.QtWidgets import QApplication, QWidget, QPushButton
from PyQt6.QtGui import QGuiApplication, QPainter, QColor


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

        # Вычисляем ширину блока (10% от ширины экрана)
        self.block_width = int(screen_width * 0.05)
        self.block_height = 10000  # Блок занимает всю высоту окна

        # Создаем кнопки без текста
        self.button1 = QPushButton(self)
        self.button2 = QPushButton(self)

        # Делаем кнопки квадратными с фиксированным размером
        screen_w = int(screen_width * 0.05)
        button_size = screen_w * 0.5
        button_padding = button_size / 2  # Размер кнопки
        self.button1.setFixedSize(button_size, button_size)
        self.button2.setFixedSize(button_size, button_size)

        # Устанавливаем позиции кнопок
        self.button1.setGeometry(button_padding, 30, button_size, button_size)  # Кнопка 1 в левом верхнем углу
        self.button2.setGeometry(button_padding, 200, button_size, button_size)  # Кнопка 2 чуть ниже первой

        # Устанавливаем начальный цвет фона окна (цвет, который будет выбран первой кнопкой)
        self.bg_color = QColor(200, 255, 200)  # Очень светлый зелёный
        self.setStyleSheet("background-color: rgb(200, 255, 200);")

        # Устанавливаем цвет левого блока (спокойный бежевый)
        self.block_color = QColor(245, 245, 220)  # Бежевый цвет
        self.button1.clicked.connect(self.change_background_color_green)
        self.button2.clicked.connect(self.change_background_color_blue)

    def change_background_color_green(self):
        # Меняем цвет фона на светло-зелёный
        self.bg_color = QColor(200, 255, 200)  # Очень светлый зелёный
        self.setStyleSheet(f"background-color: rgb({self.bg_color.red()}, {self.bg_color.green()}, {self.bg_color.blue()});")

    def change_background_color_blue(self):
        # Меняем цвет фона на светло-синий
        self.bg_color = QColor(173, 216, 230)  # Светло-синий
        self.setStyleSheet(f"background-color: rgb({self.bg_color.red()}, {self.bg_color.green()}, {self.bg_color.blue()});")

    def paintEvent(self, event):
        painter = QPainter(self)

        # Устанавливаем цвет заливки блока (бежевый)
        painter.setBrush(self.block_color)

        # Убираем обводку (не рисуем её)
        painter.setPen(QColor(0, 0, 0, 0))  # Устанавливаем прозрачную обводку

        # Рисуем блок без обводки
        painter.drawRect(0, 0, self.block_width, self.block_height)


if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = MyWindow()
    window.show()
    sys.exit(app.exec())
