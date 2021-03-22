from Components.Behaviors.Quack.Quack import Quack


class DuckManuk:
    quack_behavior = Quack()

    def perform_quack(self):
        self.quack_behavior.quack()
