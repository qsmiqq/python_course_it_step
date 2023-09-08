"""
Реализовать класс Material, который представляет однородный материал (вещество). Атрибуты класса name и density являются приватными. Метод get_material() должен возвращать строку, разделенную «;»

Output:
steel;7850.0
Создать класс Subject, который представляет объект, состоящий из однородного материала. Атрибуты класса: name, material, volume (объем) должны быть приватными. Реализовать методы класса get_mass() (приватный), который возвращает массу объекта (=density*volume) и get_subject(), который возвращает строку со всеми атрибутами (плюс масса (mass)), разделенную «;»

Output:
wire;steel;7850.0;0.03;235.5
Определите класс Runner (интерфейс для управления внутренними классами), где:

Создайте объект, представляющий стальную проволоку (steel_wire) объемом 0,03 м
Вывести содержимое объекта на консоль, используя метод get_subject().
Обновите материал проволоки на медь (copper) (плотность = 8500.0 и выведите его массу)
Output:
The wire mass is 255.0 kg
В этой задаче нет отношения наследования между сущностями (материал и предмет). Наследование возникает, когда одна сущность является частным случаем другой. Например, металл (или другое твердое вещество) и материал. Другими словами, металл является материалом. Предмет состоит из материала, а не является материалом. Поэтому предмет не может быть наследником от материала. Обратите внимание, что у конкретного материала плотность является константой, что нужно отразить при создании класса. Например, у стали плотность 7850.0 и никакая другая.
"""
class Material:
    def __init__(self, name, density):
        self.__name = name
        self.__density = density

    def get_name(self):
        return self.__name

    def set_name(self, a):
        self.__name = a

    def get_density(self):
        return self.__density

    def set_density(self, b):
        self.__density = b

    property(get_name, set_name)
    property(get_density, set_density)


mat = Material("steel", 7850.0)
print(f"{mat.get_name()};{mat.get_density()}")


class Subject(Material):
    def __init__(self, name, density, material, volume):
        super().__init__(name, density)
        self.__material = material
        self.__volume = volume

    def get_material(self):
        return self.__material

    def set_material(self, c):
        self.__material = c

    def get_volume(self):
        return self.__volume

    def set_volume(self, d):
        self.__volume = d

    def get_mass(self, density, volume):
        return density * volume

    def get_subject(self):
        print(f"{subj.get_material()};{subj.get_name()};{subj.get_density()};{subj.get_volume()};{subj.get_mass(7850, 0.03)}")

    property(get_material, set_material)
    property(get_volume, set_volume)


subj = Subject("steel", 7850.0, "wire", 0.03, )
subj.get_subject()


class Runner(Subject):
    def __init__(self, name, density, material, volume):
        super().__init__(name, density, material, volume)


inter = Runner("steel wire", 8500.0, "copper", 0.03)
print(f"The {inter.get_name()} mass is {inter.get_mass(8500.0, 0.03)} kg")

