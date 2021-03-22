from Components.Behaviors.Fly.FlyWithWings import FlyWithWings
from Components.Behaviors.Quack.Quack import Quack
from Components.Behaviors.Swim.Swim import Swim
from Components.Duck import Duck


class RedheadDuck(Duck):
    fly_behavior = FlyWithWings()
    quack_behavior = Quack()
    swim_behavior = Swim()
