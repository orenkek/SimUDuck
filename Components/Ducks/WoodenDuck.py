from Components.Behaviors.Fly.FlyNoWay import FlyNoWay
from Components.Behaviors.Quack.MuteQuack import MuteQuack
from Components.Behaviors.Swim.Sail import Sail
from Components.Duck import Duck


class WoodenDuck(Duck):
    quack_behavior = MuteQuack()
    fly_behavior = FlyNoWay()
    swim_behavior = Sail()
