import sys
from PyQt6.QtWidgets import QApplication, QWidget, QPushButton, QVBoxLayout, QFrame
from PyQt6.QtCore import Qt

class MyWindow(QWidget):
    def __init__(self):
        super().__init__()

        self.setWindowTitle("Интерфейс с кнопками")
        self.setGeometry(100, 100, 400, 300)  # Размер окна

        # Устанавливаем белый фон окна
        self.setStyleSheet("background-color: white;")

        # Создаем вертикальный layout для основного окна
        main_layout = QVBoxLayout(self)

        # Создаем контейнер для блока кнопок
        button_block = QFrame(self)
        button_block.setStyleSheet("background-color: beige;")  # Бежевый цвет для блока
        button_block.setFixedWidth(100)  # Фиксированная ширина блока

        # Создаем вертикальный layout для кнопок
        layout = QVBoxLayout(button_block)

        # Создаем две кнопки
        button1 = QPushButton(self)
        button1.setStyleSheet("background-color: lightblue;")
        button1.setFixedSize(50, 50)  # Задаем размер кнопки

        button2 = QPushButton(self)
        button2.setStyleSheet("background-color: lightgreen;")
        button2.setFixedSize(50, 50)  # Задаем размер кнопки

        # Добавляем кнопки в вертикальный контейнер
        layout.addWidget(button1)
        layout.addSpacing(20)  # Отступ между кнопками
        layout.addWidget(button2)

        # Устанавливаем расположение элементов
        button_block.setLayout(layout)

        # Добавляем блок с кнопками в основной layout
        main_layout.addWidget(button_block)
        main_layout.addStretch(1)  # Заполняем оставшееся пространство

        # Устанавливаем основной layout для окна
        self.setLayout(main_layout)

if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = MyWindow()
    window.show()
    sys.exit(app.exec())
