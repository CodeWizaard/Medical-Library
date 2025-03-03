import sys
import os
from cryptography.fernet import Fernet
from PyQt6.QtWidgets import QApplication, QWidget, QPushButton, QLabel, QLineEdit, QVBoxLayout
from PyQt6.QtGui import QGuiApplication


class MyWindow(QWidget):
    def __init__(self):
        super().__init__()

        try:
            # Генерация ключа для шифрования (если его нет)
            self.key_file = "encryption_key.key"
            self.data_file = "encrypted_data.txt"
            self.key = self.load_or_generate_key()
            print(f"Ключ: {self.key}")

            # Создаём объект для шифрования
            self.cipher = Fernet(self.key)

            # Инициализация GUI
            self.setGeometry(100, 100, 400, 300)
            self.setWindowTitle("Шифрование данных")

            self.button_save = QPushButton("Сохранить", self)
            self.button_save.setGeometry(150, 200, 100, 40)
            self.button_save.clicked.connect(self.save_data)

            self.input_pressure = QLineEdit(self)
            self.input_pressure.setGeometry(50, 50, 300, 30)
            self.input_sugar = QLineEdit(self)
            self.input_sugar.setGeometry(50, 100, 300, 30)

            # Загружаем данные при запуске
            self.load_saved_data()

            self.show()

        except Exception as e:
            print(f"Ошибка при инициализации: {e}")

    def load_or_generate_key(self):
        """Загружает ключ, если он существует, иначе генерирует новый."""
        try:
            if os.path.exists(self.key_file):
                with open(self.key_file, "rb") as key_file:
                    return key_file.read()
            else:
                key = Fernet.generate_key()
                with open(self.key_file, "wb") as key_file:
                    key_file.write(key)
                return key
        except Exception as e:
            print(f"Ошибка при загрузке/генерации ключа: {e}")
            raise

    def encrypt_data(self, data):
        """Шифрует данные с использованием ключа."""
        try:
            return self.cipher.encrypt(data.encode())
        except Exception as e:
            print(f"Ошибка при шифровании данных: {e}")
            raise

    def decrypt_data(self, data):
        """Расшифровывает данные с использованием ключа."""
        try:
            return self.cipher.decrypt(data).decode()
        except Exception as e:
            print(f"Ошибка при расшифровке данных: {e}")
            raise

    def save_data(self):
        """Сохраняет данные (шифрует перед сохранением)."""
        try:
            pressure = self.input_pressure.text()
            sugar = self.input_sugar.text()

            if not pressure and not sugar:
                print("Нет данных для сохранения.")
                return

            # Формируем строку данных для сохранения
            data = f"Давление: {pressure if pressure else 'Не указано'}\nУровень сахара: {sugar if sugar else 'Не указано'}"

            # Шифруем данные
            encrypted_data = self.encrypt_data(data)

            # Сохраняем зашифрованные данные в файл
            with open(self.data_file, "wb") as file:
                file.write(encrypted_data)
            print("Данные сохранены.")
        except Exception as e:
            print(f"Ошибка при сохранении данных: {e}")

    def load_saved_data(self):
        """Загружает и расшифровывает данные из файла, если они есть."""
        try:
            if os.path.exists(self.data_file):
                with open(self.data_file, "rb") as file:
                    encrypted_data = file.read()
                    decrypted_data = self.decrypt_data(encrypted_data)
                    print("Загруженные данные:", decrypted_data)

                    # Разбиваем данные по строкам и показываем их в текстовых полях
                    lines = decrypted_data.split('\n')
                    if len(lines) > 0:
                        self.input_pressure.setText(lines[0].split(":")[1].strip())
                    if len(lines) > 1:
                        self.input_sugar.setText(lines[1].split(":")[1].strip())

            else:
                print("Сохраненные данные не найдены.")
        except Exception as e:
            print(f"Ошибка при загрузке данных: {e}")
            return None


if __name__ == "__main__":
    try:
        app = QApplication(sys.argv)
        window = MyWindow()
        sys.exit(app.exec())
    except Exception as e:
        print(f"Ошибка при запуске приложения: {e}")
