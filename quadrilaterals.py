from math import sqrt
from abc import ABC, abstractmethod


class Quadrilateral:
    num_of_sides = 4  # Статическое поле

    def __init__(self, a=1.0, b=1.0, c=1.0, d=1.0):
        self.a = a  # Динамические поля
        self.b = b
        self.c = c
        self.d = d
        print(f"Quadrilateral создан с сторонами: {self.a}, {self.b}, {self.c}, {self.d}")

    @classmethod
    def copy_constructor(cls, other):
        return cls(other.a, other.b, other.c, other.d)

    def __del__(self):
        print("Quadrilateral уничтожен")

    # Геттеры
    def get_a(self):
        return self.a

    def get_b(self):
        return self.b

    def get_c(self):
        return self.c

    def get_d(self):
        return self.d

    # Сеттеры
    def set_a(self, value):
        self.a = value

    def set_b(self, value):
        self.b = value

    def set_c(self, value):
        self.c = value

    def set_d(self, value):
        self.d = value

    # Перегруженные методы для установки сторон
    def set_sides(self, a, b, c, d):
        self.a, self.b, self.c, self.d = a, b, c, d
        print(f"Стороны обновлены до: {self.a}, {self.b}, {self.c}, {self.d}")

    def set_sides_overload(self, a, b):
        self.a, self.b = a, b
        self.c, self.d = a, b
        print(f"Только две стороны обновлены до: {self.a}, {self.b}, {self.c}, {self.d}")

    # Константный метод (по соглашению не изменяет состояние объекта)
    def get_num_of_sides(self):
        return Quadrilateral.num_of_sides

    # Private метод
    def __private_method(self):
        print("Это приватный метод Quadrilateral")

    # Метод, вызывающий приватный метод
    def call_private_method(self):
        self.__private_method()

    def calculate_area(self):
        # Используем формулу Брахмагупты для циклического четырёхугольника
        s = (self.a + self.b + self.c + self.d) / 2
        try:
            area_square = (s - self.a) * (s - self.b) * (s - self.c) * (s - self.d)
            if area_square < 0:
                raise ValueError("Некорректные стороны для вычисления площади циклического четырёхугольника.")
            area = sqrt(area_square)
            print(f"Площадь Quadrilateral: {area}")
            return area
        except ValueError as e:
            print(f"Ошибка при вычислении площади: {e}")
            return None

    def calculate_perimeter(self):
        perimeter = self.a + self.b + self.c + self.d
        print(f"Периметр: {perimeter}")
        return perimeter

    def print_info(self):
        print(f"Quadrilateral с сторонами: {self.a}, {self.b}, {self.c}, {self.d}")


class Rectangle(Quadrilateral):
    static_field = "Я статическое поле Rectangle"

    def __init__(self, width=1.0, height=1.0):
        super().__init__(a=width, b=height, c=width, d=height)
        self.height = height  # Дополнительное динамическое поле
        print(f"Rectangle создан с шириной {width} и высотой {self.height}")

    def calculate_area(self):
        area = self.a * self.b
        print(f"Площадь Rectangle: {area}")
        return area

    def print_info(self):
        print(f"Rectangle с шириной: {self.a} и высотой: {self.b}")

    # Дополнительный метод специфичный для Rectangle
    def is_square(self):
        return self.a == self.b


class Square(Rectangle):
    static_count = 0  # Статическое поле для подсчёта количества квадратов

    def __init__(self, side=1.0):
        super().__init__(width=side, height=side)
        Square.static_count += 1
        print(f"Square создан со стороной {side}. Всего квадратов: {Square.static_count}")

    def calculate_area(self):
        area = self.a ** 2
        print(f"Площадь Square: {area}")
        return area

    def print_info(self):
        print(f"Square со стороной: {self.a}")

    @classmethod
    def get_square_count(cls):
        return cls.static_count


class _Rhombus(Quadrilateral):
    static_field_rhombus = "Я статическое поле Rhombus"

    def __init__(self, side=1.0, diagonal1=1.0, diagonal2=1.0):
        super().__init__(a=side, b=side, c=side, d=side)
        self.diagonal1 = diagonal1  # Дополнительные динамические поля
        self.diagonal2 = diagonal2
        print(f"Rhombus создан с сторонами {self.a} и диагоналями {self.diagonal1}, {self.diagonal2}")

    def calculate_area(self):
        area = (self.diagonal1 * self.diagonal2) / 2
        print(f"Площадь Rhombus: {area}")
        return area

    def print_info(self):
        print(f"Rhombus со сторонами: {self.a} и диагоналями: {self.diagonal1}, {self.diagonal2}")


def main_menu():
    quadrilaterals = []
    rectangles = []
    squares = []
    rhombuses = []

    while True:
        print("\n--- Главное меню ---")
        print("1. Создать Quadrilateral")
        print("2. Создать Rectangle")
        print("3. Создать Square")
        print("4. Создать Rhombus")
        print("5. Печать всех объектов")
        print("6. Вычислить периметр объекта")
        print("7. Вычислить площадь объекта")
        print("8. Вызвать приватный метод Quadrilateral")
        print("9. Выход")

        choice = input("Выберите опцию: ")

        if choice == '1':
            try:
                a = float(input("Введите сторону a: "))
                b = float(input("Введите сторону b: "))
                c = float(input("Введите сторону c: "))
                d = float(input("Введите сторону d: "))
                quad = Quadrilateral(a, b, c, d)
                quadrilaterals.append(quad)
            except ValueError:
                print("Некорректный ввод. Пожалуйста, введите числовые значения.")

        elif choice == '2':
            try:
                width = float(input("Введите ширину Rectangle: "))
                height = float(input("Введите высоту Rectangle: "))
                rect = Rectangle(width, height)
                rectangles.append(rect)
            except ValueError:
                print("Некорректный ввод. Пожалуйста, введите числовые значения.")

        elif choice == '3':
            try:
                side = float(input("Введите сторону Square: "))
                sq = Square(side)
                squares.append(sq)
            except ValueError:
                print("Некорректный ввод. Пожалуйста, введите числовые значения.")

        elif choice == '4':
            try:
                side = float(input("Введите сторону Rhombus: "))
                diag1 = float(input("Введите диагональ 1: "))
                diag2 = float(input("Введите диагональ 2: "))
                rhomb = _Rhombus(side, diag1, diag2)
                rhombuses.append(rhomb)
            except ValueError:
                print("Некорректный ввод. Пожалуйста, введите числовые значения.")

        elif choice == '5':
            print("\n--- Quadrilaterals ---")
            if quadrilaterals:
                for i, q in enumerate(quadrilaterals, 1):
                    print(f"{i}. ", end="")
                    q.print_info()
            else:
                print("Нет объектов Quadrilateral")

            print("\n--- Rectangles ---")
            if rectangles:
                for i, r in enumerate(rectangles, 1):
                    print(f"{i}. ", end="")
                    r.print_info()
            else:
                print("Нет объектов Rectangle")

            print("\n--- Squares ---")
            if squares:
                for i, s in enumerate(squares, 1):
                    print(f"{i}. ", end="")
                    s.print_info()
            else:
                print("Нет объектов Square")

            print("\n--- Rhombuses ---")
            if rhombuses:
                for i, rh in enumerate(rhombuses, 1):
                    print(f"{i}. ", end="")
                    rh.print_info()
            else:
                print("Нет объектов Rhombus")

        elif choice == '6':
            obj_type = input("Выберите тип объекта (Quadrilateral/Rectangle/Square/Rhombus): ").strip().lower()
            index = input("Введите номер объекта: ").strip()
            if not index.isdigit() or int(index) < 1:
                print("Некорректный номер объекта.")
                continue
            index = int(index) - 1
            try:
                if obj_type == 'quadrilateral':
                    chosen_obj = quadrilaterals[index]
                elif obj_type == 'rectangle':
                    chosen_obj = rectangles[index]
                elif obj_type == 'square':
                    chosen_obj = squares[index]
                elif obj_type == 'rhombus':
                    chosen_obj = rhombuses[index]
                else:
                    print("Неизвестный тип объекта")
                    continue
                chosen_obj.calculate_perimeter()
            except IndexError:
                print("Некорректный индекс")
            except Exception as e:
                print(f"Ошибка: {e}")

        elif choice == '7':
            obj_type = input("Выберите тип объекта (Quadrilateral/Rectangle/Square/Rhombus): ").strip().lower()
            index = input("Введите номер объекта: ").strip()
            if not index.isdigit() or int(index) < 1:
                print("Некорректный номер объекта.")
                continue
            index = int(index) - 1
            try:
                if obj_type == 'quadrilateral':
                    chosen_obj = quadrilaterals[index]
                elif obj_type == 'rectangle':
                    chosen_obj = rectangles[index]
                elif obj_type == 'square':
                    chosen_obj = squares[index]
                elif obj_type == 'rhombus':
                    chosen_obj = rhombuses[index]
                else:
                    print("Неизвестный тип объекта")
                    continue
                area = chosen_obj.calculate_area()
                if area is not None:
                    print(f"Вычисленная площадь: {area}")
            except IndexError:
                print("Некорректный индекс")
            except Exception as e:
                print(f"Ошибка: {e}")

        elif choice == '8':
            if not quadrilaterals:
                print("Нет объектов Quadrilateral")
                continue
            try:
                index = int(input("Введите номер Quadrilateral: ")) - 1
                quadrilaterals[index].call_private_method()
            except ValueError:
                print("Некорректный ввод. Пожалуйста, введите числовое значение.")
            except IndexError:
                print("Некорректный индекс")
            except Exception as e:
                print(f"Ошибка: {e}")

        elif choice == '9':
            print("Выход из программы")
            break

        else:
            print("Неверный выбор. Попробуйте снова.")


if __name__ == "__main__":
    main_menu()
