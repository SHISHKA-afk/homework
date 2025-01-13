class House:
    houses_history = []

    def __new__(cls, name, number_of_floors, *args, **kwargs):
        # Создаём новый объект
        obj = super().__new__(cls)

        # Добавляем название объекта в историю
        cls.houses_history.append(name)

        return obj

    def __init__(self, name, number_of_floors):
        self.name = name
        self.number_of_floors = number_of_floors

    def __del__(self):
        print(f"{self.name} снесён, но он останется в истории")

    def __str__(self):
        return f"Название: {self.name}, кол-во этажей: {self.number_of_floors}"

    def __eq__(self, other):
        if isinstance(other, House):
            return self.number_of_floors == other.number_of_floors
        return False

    def __add__(self, value):
        if isinstance(value, int) and value >= 0:
            new_floors = self.number_of_floors + value
            return House(self.name, new_floors)
        return NotImplemented

    def __iadd__(self, value):
        return self.__add__(value)

    def __radd__(self, value):
        return self.__add__(value)


# Пример использования
h1 = House('ЖК Эльбрус', 10)
print(House.houses_history)
h2 = House('ЖК Акация', 20)
print(House.houses_history)
h3 = House('ЖК Матрёшки', 20)
print(House.houses_history)

# Удаление объектов
del h2
del h3

print(House.houses_history)