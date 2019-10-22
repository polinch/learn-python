import csv
import os


class CarBase(object):
    def __init__(self, brand, photo_file_name, carrying):
        self.car_type = None
        self.photo_file_name = photo_file_name
        self.brand = brand
        self.carrying = carrying

    def get_photo_file_ext(self):
        try:
            ext = os.path.splitext(self.photo_file_name)[1]
        except IndexError:
            ext = ""
        return ext


class Car(CarBase):
    def __init__(self, brand, photo_file_name, carrying, passenger_seats_count):
        super().__init__(brand, photo_file_name, carrying)
        self.car_type = "car"
        self.passenger_seats_count = passenger_seats_count


class Truck(CarBase):
    def __init__(self, brand, photo_file_name, carrying, body_whl):
        super().__init__(brand, photo_file_name, carrying)
        self.car_type = "truck"
        if body_whl is not '':
            temp = body_whl.split('x')
            self.body_length = float(temp[0])
            self.body_width = float(temp[1])
            self.body_height = float(temp[2])
        else:
            self.body_length = 0
            self.body_width = 0
            self.body_height = 0

    def get_body_volume(self):
        return self.body_height * self.body_length * self.body_width


class SpecMachine(CarBase):
    def __init__(self, brand, photo_file_name, carrying, extra):
        super().__init__(brand, photo_file_name, carrying)
        self.car_type = "spec_machine"
        self.extra = extra


def get_car_list(csv_filename):
    car_list = []
    with open(csv_filename) as csv_fd:
        reader = csv.reader(csv_fd, delimiter=';')
        next(reader)  # пропускаем заголовок
        for row in reader:
            if row:
                try:
                    if row[0] == 'car':
                        car_list.append(Car(row[1], row[3], float(row[5]), int(row[2])))
                    elif row[0] == 'truck':
                        car_list.append(Truck(row[1], row[3], float(row[5]), row[4]))
                    elif row[0] == 'spec_machine':
                        car_list.append(SpecMachine(row[1], row[3], float(row[5]), row[6]))
                except IndexError:
                    pass

    return car_list

