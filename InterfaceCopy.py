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
        button_padding = button_size/2 # Размер кнопки
        self.button1.setFixedSize(button_size, button_size)
        self.button2.setFixedSize(button_size, button_size)

        # Устанавливаем позиции кнопок
        self.button1.setGeometry(button_padding, 30, button_size, button_size)  # Кнопка 1 в левом верхнем углу
        self.button2.setGeometry(button_padding, 200, button_size, button_size)  # Кнопка 2 чуть ниже первой

    def paintEvent(self, event):
        painter = QPainter(self)

        # Устанавливаем цвет заливки блока (зеленый с прозрачностью)
        painter.setBrush(QColor(0, 255, 0, 55))

        # Убираем обводку (не рисуем её)
        painter.setPen(QColor(0, 0, 0, 0))  # Устанавливаем прозрачную обводку

        # Рисуем блок без обводки
        painter.drawRect(0, 0, self.block_width, self.block_height)


if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = MyWindow()
    window.show()
    sys.exit(app.exec())
