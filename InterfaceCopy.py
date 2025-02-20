import sys
from PyQt6.QtWidgets import QApplication, QWidget
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
