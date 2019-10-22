# Задачи
* [Реализация простого класса для чтения из файла](https://github.com/polinch/learn-python/blob/master/%D0%9F%D0%BE%D0%B3%D1%80%D1%83%D0%B6%D0%B5%D0%BD%D0%B8%D0%B5%20%D0%B2%20Python%20%D0%BE%D1%82%20Mail.ru/solution.py)  
Инициализатор класса принимает аргумент - путь до файла на диске. У класса есть метод read, возвращающий содержимое файла в виде строки. Внутри данного метода есть обработка исключения IOError, возникающего когда файла, с которым инициализирован класс, на самом деле нет на жестком диске.  
* [Классы и наследование](https://github.com/polinch/learn-python/blob/master/%D0%9F%D0%BE%D0%B3%D1%80%D1%83%D0%B6%D0%B5%D0%BD%D0%B8%D0%B5%20%D0%B2%20Python%20%D0%BE%D1%82%20Mail.ru/carsolution.py)  
Создана следующая иерархия классов:  
  * BaseCar  
  * Car(BaseCar)  
  * Truck(BaseCar)  
  * SpecMachine(BaseCar)  
* [Файл с магическими методами](https://github.com/polinch/learn-python/blob/master/%D0%9F%D0%BE%D0%B3%D1%80%D1%83%D0%B6%D0%B5%D0%BD%D0%B8%D0%B5%20%D0%B2%20Python%20%D0%BE%D1%82%20Mail.ru/magicfile.py)  
Создан интерфейс для работы с файлами. Класс инициализируется полным путем, поддерживает метод write. Объекты типа File поддерживают сложение; поддерживают протокол итерации, итерация проходит по строкам файла. При выводе файла с помощью функции print печатается полный путь до него, переданный при инициализации.  
* [Дескриптор с коммисией](https://github.com/polinch/learn-python/blob/master/%D0%9F%D0%BE%D0%B3%D1%80%D1%83%D0%B6%D0%B5%D0%BD%D0%B8%D0%B5%20%D0%B2%20Python%20%D0%BE%D1%82%20Mail.ru/descriptor.py)  
Дескриптор Value используется в классе Account. У аккаунта есть атрибут commission. Эта коммиссия вычитается при присваивании значений в amount.
