from Components.Behaviors.Fly.FlyWithWings import FlyWithWings
from Components.Behaviors.Quack.Quack import Quack
from Components.Behaviors.Swim.Swim import Swim
from Components.Duck import Duck


class MallardDuck(Duck):
    quack_behavior = Quack()
    fly_behavior = FlyWithWings()
    swim_behavior = Swim()
