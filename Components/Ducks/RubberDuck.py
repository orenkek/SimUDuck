from Components.Behaviors.Fly.FlyNoWay import FlyNoWay
from Components.Behaviors.Quack.Squeak import Squeak
from Components.Behaviors.Swim.Sail import Sail
from Components.Duck import Duck


class RubberDuck(Duck):
    fly_behavior = FlyNoWay()
    quack_behavior = Squeak()
    swim_behavior = Sail()
