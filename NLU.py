class Checker:
    def __init__(self):
        pass

    def check(self, victim, q_options):
        try:
            int(victim)
            if int(victim) <= q_options:
                return True
            else:
                return False
        except ValueError:
            return False
