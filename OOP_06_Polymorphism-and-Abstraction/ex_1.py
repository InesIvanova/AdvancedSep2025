class Robot(object):
    def __init__(self, name):
        self.name = name

    @staticmethod
    def sensors_amount():
        return 1

    def __len__(self):
        return len(self.name)

    def __add__(self, other):
        return self.__len__() + other.__len__()

    def __sub__(self, other):
        return self.__len__() - other.__len__()

    def __eq__(self, other):
        return self.name == other.name

r = Robot("asdf")
r2 = Robot("asdf")
print(r < r2)
print(r.__add__(r2))
print(r == r2)
print(len(r))

class MedicalRobot(Robot):
    @staticmethod
    def sensors_amount():
        return 6


class ChefRobot(Robot):
    @staticmethod
    def sensors_amount():
        return 4


class WarRobot(Robot):
    @staticmethod
    def sensors_amount():
        return 12


class FuturistRobot(Robot):
    @staticmethod
    def sensors_amount():
        return 30


class SimplePhoneRobot(Robot):
    pass


def number_of_robot_sensors(robot):
    print(robot.sensors_amount())


basic_robot = Robot('Robo')
da_vinci = MedicalRobot('Da Vinci')
moley = ChefRobot('Moley')
griffin = WarRobot('Griffin')
spr = SimplePhoneRobot('Spring')

number_of_robot_sensors(basic_robot)
number_of_robot_sensors(da_vinci)
number_of_robot_sensors(moley)
number_of_robot_sensors(griffin)
number_of_robot_sensors(spr)


a = {"1": 1, "2": 2, "3": 3}
a["1"] = 100
print(a)