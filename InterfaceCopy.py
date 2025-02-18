import sys
from PyQt6.QtWidgets import QApplication, QWidget, QVBoxLayout, QHBoxLayout, QFrame, QLabel
from PyQt6.QtCore import Qt

class MyWindow(QWidget):
    def __init__(self):
        super().__init__()

        self.setWindowTitle("Окно с боковой панелью")
        self.setGeometry(100, 100, 800, 600)  # Размер окна

        # Создаем основной горизонтальный макет
        main_layout = QHBoxLayout(self)

        # Создаем панель, занимающую 20% ширины окна
        panel = QFrame(self)
        panel.setStyleSheet("background-color: lightgray;")
        panel.setFixedWidth(self.width() * 0.2)  # 20% ширины окна

        # Создаем основной виджет
        main_content = QWidget(self)
        main_content.setStyleSheet("background-color: white;")

        # Добавляем панель и основной виджет в основной макет
        main_layout.addWidget(panel)
        main_layout.addWidget(main_content)

        # Устанавливаем основной макет для окна
        self.setLayout(main_layout)

    def resizeEvent(self, event):
        # Обновляем ширину панели при изменении размера окна
        self.layout().itemAt(0).widget().setFixedWidth(self.width() * 0.2)
        super().resizeEvent(event)

if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = MyWindow()
    window.show()
    sys.exit(app.exec())
