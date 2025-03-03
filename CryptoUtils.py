from cryptography.fernet import Fernet
import os


class CryptoUtils:
    def __init__(self):
        # Генерация ключа для шифрования (если его нет)
        self.key_file = "encryption_key.key"
        self.data_file = "encrypted_data.txt"
        self.key = self.load_or_generate_key()
        print(f"Ключ: {self.key}")

        # Создаём объект для шифрования
        self.cipher = Fernet(self.key)

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

    def save_encrypted_data(self, data):
        """Шифрует данные и сохраняет их в файл."""
        encrypted_data = self.encrypt_data(data)
        try:
            with open(self.data_file, "wb") as file:
                file.write(encrypted_data)
            print(f"Данные успешно сохранены в файл {self.data_file}")
        except Exception as e:
            print(f"Ошибка при сохранении данных: {e}")
            raise

    def load_encrypted_data(self):
        """Загружает и расшифровывает данные из файла."""
        try:
            with open(self.data_file, "rb") as file:
                encrypted_data = file.read()
            return self.decrypt_data(encrypted_data)
        except Exception as e:
            print(f"Ошибка при загрузке данных: {e}")
            raise


# Функция для автоматического заполнения полей при открытии интерфейса
def load_and_fill_data(self):
    """Загружает и расшифровывает данные, заполняет поля на интерфейсе."""
    # Создаём объект CryptoUtils для работы с данными
    crypto_utils = CryptoUtils()

    try:
        # Загружаем расшифрованные данные
        decrypted_data = crypto_utils.load_encrypted_data()

        # Разбиваем расшифрованные данные на отдельные части
        pressure, sugar = self.parse_data(decrypted_data)

        # Заполняем текстовые поля
        self.findChild(QLineEdit, "input_pressure").setText(pressure)
        self.findChild(QLineEdit, "input_sugar").setText(sugar)

        print("Данные успешно загружены и заполнены в поля.")

    except Exception as e:
        print(f"Ошибка при загрузке и заполнении данных: {e}")


def parse_data(self, decrypted_data):
    """Разбирает расшифрованные данные на составляющие: давление и сахар."""
    # Пример того, как можно разобрать строку (если данные хранятся в формате: 'Давление: <значение>, Уровень сахара: <значение>')
    try:
        parts = decrypted_data.split(", ")
        pressure = parts[0].split(": ")[1] if len(parts) > 0 else ""
        sugar = parts[1].split(": ")[1] if len(parts) > 1 else ""
        return pressure, sugar
    except Exception as e:
        print(f"Ошибка при разборе данных: {e}")
        return "", ""
