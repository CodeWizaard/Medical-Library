from datetime import datetime

class Exercise:
    def __init__(self, exercise_type, duration, frequency_per_week, comment="", date=None):
        """
        Инициализация нового упражнения
        :param exercise_type: Тип упражнения (например, бег, плавание и т.д.)
        :param duration: Продолжительность упражнения в минутах
        :param frequency_per_week: Количество раз в неделю
        :param comment: Комментарий пользователя
        :param date: Дата выполнения упражнения. Если не указана, будет использована текущая дата.
        """
        self.exercise_type = exercise_type
        self.duration = duration
        self.frequency_per_week = frequency_per_week
        self.comment = comment

        # Преобразуем строку в объект datetime, если дата была передана как строка
        if isinstance(date, str):
            self.date = datetime.strptime(date, "%Y-%m-%d %H:%M:%S")  # Преобразуем строку в datetime
        else:
            self.date = date if date else datetime.now()  # Если date не строка, используем текущую дату

    def get_exercise_info(self):
        """
        Получить информацию об упражнении в виде словаря.
        :return: Словарь с информацией об упражнении.
        """
        return {
            "exercise_type": self.exercise_type,
            "duration": self.duration,
            "frequency_per_week": self.frequency_per_week,
            "comment": self.comment,
            "date": self.date.strftime("%Y-%m-%d %H:%M:%S")  # Форматируем дату
        }

    def update_exercise(self, exercise_type=None, duration=None, frequency_per_week=None, comment=None, date=None):
        """
        Обновить информацию о упражнении.
        :param exercise_type: Новый тип упражнения
        :param duration: Новая продолжительность
        :param frequency_per_week: Новая частота выполнения в неделю
        :param comment: Новый комментарий
        :param date: Новая дата выполнения упражнения
        """
        if exercise_type:
            self.exercise_type = exercise_type
        if duration:
            self.duration = duration
        if frequency_per_week:
            self.frequency_per_week = frequency_per_week
        if comment:
            self.comment = comment
        if date:
            # Если дата передана как строка, преобразуем её в datetime
            self.date = datetime.strptime(date, "%Y-%m-%d %H:%M:%S") if isinstance(date, str) else date

# Класс для хранения и управления медицинскими показателями
class HealthMetrics:
    def __init__(self, blood_pressure=None, blood_sugar=None, temperature=None):
        """
        Инициализация медицинских данных пользователя
        :param blood_pressure: Давление (систолическое/диастолическое)
        :param blood_sugar: Уровень сахара в крови
        :param temperature: Температура тела
        """
        self.blood_pressure = blood_pressure  # Давление
        self.blood_sugar = blood_sugar  # Уровень сахара в крови
        self.temperature = temperature  # Температура тела

    def get_metrics(self):
        """
        Получить все медицинские данные в виде словаря.
        :return: Словарь с медицинскими показателями
        """
        return {
            "blood_pressure": self.blood_pressure,  # Давление
            "blood_sugar": self.blood_sugar,  # Уровень сахара в крови
            "temperature": self.temperature  # Температура
        }

    def update_metrics(self, blood_pressure=None, blood_sugar=None, temperature=None):
        """
        Обновить медицинские данные.
        :param blood_pressure: Новое давление
        :param blood_sugar: Новый уровень сахара в крови
        :param temperature: Новая температура
        """
        if blood_pressure:
            self.blood_pressure = blood_pressure
        if blood_sugar:
            self.blood_sugar = blood_sugar
        if temperature:
            self.temperature = temperature


# Класс для хранения информации о пользователе и его данных
class User:
    def __init__(self, name, age, gender, contact_info=None, health_metrics=None, exercises=None):
        """
        Инициализация данных пользователя
        :param name: Имя пользователя
        :param age: Возраст пользователя
        :param gender: Пол пользователя
        :param contact_info: Контактная информация (email, телефон и т.д.)
        :param health_metrics: Объект класса HealthMetrics с медицинскими показателями
        :param exercises: Список упражнений пользователя (объекты класса Exercise)
        """
        self.name = name  # Имя пользователя
        self.age = age  # Возраст пользователя
        self.gender = gender  # Пол
        self.contact_info = contact_info if contact_info else {}  # Контактная информация
        self.health_metrics = health_metrics if health_metrics else HealthMetrics()  # Медицинские данные
        self.exercises = exercises if exercises else []  # Список физических упражнений

    def get_info(self):
        """
        Получить полную информацию о пользователе (включая данные о здоровье и упражнениях).
        :return: Словарь с полной информацией
        """
        return {
            "name": self.name,  # Имя
            "age": self.age,  # Возраст
            "gender": self.gender,  # Пол
            "contact_info": self.contact_info,  # Контактная информация
            "health_metrics": self.health_metrics.get_metrics(),  # Медицинские данные
            "exercises": [exercise.get_exercise_info() for exercise in self.exercises]  # Список упражнений
        }

    def update_info(self, name=None, age=None, gender=None, contact_info=None, health_metrics=None, exercises=None):
        """
        Обновить информацию о пользователе.
        :param name: Новое имя
        :param age: Новый возраст
        :param gender: Новый пол
        :param contact_info: Новая контактная информация
        :param health_metrics: Новые медицинские данные
        :param exercises: Новый список упражнений
        """
        if name:
            self.name = name
        if age:
            self.age = age
        if gender:
            self.gender = gender
        if contact_info:
            self.contact_info.update(contact_info)
        if health_metrics:
            self.health_metrics = health_metrics
        if exercises is not None:
            self.exercises = exercises  # Обновляем список упражнений

    def add_exercise(self, exercise_type, duration, frequency_per_week, comment="", date=None):
        """
        Добавить новое физическое упражнение в список.
        :param exercise_type: Тип упражнения
        :param duration: Продолжительность упражнения
        :param frequency_per_week: Частота выполнения в неделю
        :param comment: Комментарий пользователя
        :param date: Дата выполнения упражнения
        """
        new_exercise = Exercise(exercise_type, duration, frequency_per_week, comment, date)
        self.exercises.append(new_exercise)

    def update_exercise(self, index, exercise_type=None, duration=None, frequency_per_week=None, comment=None, date=None):
        """
        Обновить информацию о физическом упражнении по индексу.
        :param index: Индекс упражнения в списке
        :param exercise_type: Новый тип упражнения
        :param duration: Новая продолжительность
        :param frequency_per_week: Новая частота выполнения в неделю
        :param comment: Новый комментарий
        :param date: Новая дата выполнения
        """
        if 0 <= index < len(self.exercises):
            self.exercises[index].update_exercise(exercise_type, duration, frequency_per_week, comment, date)
        else:
            print("Exercise not found.")

    def get_exercises(self):
        """
        Получить список всех упражнений.
        :return: Список упражнений в виде словарей
        """
        return [exercise.get_exercise_info() for exercise in self.exercises]



# Создаем пользователя с медицинскими данными и упражнениями
user = User(
    name="Иван",
    age=30,
    gender="мужской",
    contact_info={"email": "ivan@example.com"},
    health_metrics=HealthMetrics(blood_pressure="120/80", blood_sugar="5.2", temperature="36.6"),
    exercises=[]
)

# Добавляем физическое упражнение с датой
user.add_exercise("Бег", 30, 3, "Утренняя пробежка для поддержания тонуса", date="2025-02-16 07:00:00")
user.add_exercise("Силовые тренировки", 60, 2, "Тренировка на все группы мышц")

# Получаем полную информацию о пользователе, включая упражнения с датами
print(user.get_info())

# Обновляем упражнение с изменением даты
user.update_exercise(0, duration=40, comment="Увеличена продолжительность пробежки", date="2025-02-17 07:00:00")
user.update_info(age=25)
# Проверим обновленные данные
print(user.get_info())
