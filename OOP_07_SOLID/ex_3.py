from abc import abstractmethod, ABC



class BaseToy(ABC):
    @staticmethod
    def make_sound():
        pass


class RubberDuck(BaseToy):
    @staticmethod
    def make_sound():
        return "Squeek"


class RobotDuck(BaseToy):
    HEIGHT = 50

    def __init__(self):
        self.height = 0

    @staticmethod
    def quack():
        return 'Robotic quacking'

    @staticmethod
    def walk():
        return 'Robotic walking'

    def fly(self):
        """can only fly to specific height but
        when it reaches it starts landing automatically"""
        if self.height == RobotDuck.HEIGHT:
            self.land()
        else:
            self.height += 1

    def land(self):
        self.height = 0




