class ParametricTrajectory:

    def __init__(self, initial_pos, acc, t1, t2):
        self._acc = acc
        self._t1 = t1
        self._t2 = t2
        self._initial_pos = initial_pos

    def acc(self, t):
        if t <= self._t1:
            return self._acc
        elif t <= self._t2:
            return - self._acc
        else:
            return 0

    def vel(self, t):
        if t <= self._t1:
            return self._acc * t
        elif t <= self._t2:
            dt = t - self._t1
            return self.vel(self._t1) - self._acc * dt
        else:
            return self.vel(self._t2)

    def pos(self, t):
        if t <= self._t1:
            return self._initial_pos + self._acc * t**2 / 2
        elif t <= self._t2:
            dt = t - self._t1
            return self.pos(self._t1) + self.vel(self._t1) * dt - self._acc * dt**2 / 2
        else:
            dt = t - self._t2
            return self.pos(self._t2) + self.vel(self._t2) * dt
