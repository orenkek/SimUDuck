from Components.Interfaces.QuackBehavior import QuackBehavior
from Components.Interfaces.FlyBehavior import FlyBehavior


class Duck:
    quack_behavior = None
    fly_behavior = None
    swim_behavior = None

    def perform_quack(self):
        self.quack_behavior.quack()

    def perform_fly(self):
        self.fly_behavior.fly()

    def display(self):
        print('DISPLAY')