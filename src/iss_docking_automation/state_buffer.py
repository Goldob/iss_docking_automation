class StateBuffer:
    def __init__(self):
        self._state = {}

    def handle_x(self, msg):
        self._state['x'] = msg.data

    def handle_y(self, msg):
        self._state['y'] = msg.data

    def handle_z(self, msg):
        self._state['z'] = msg.data

    def handle_yaw(self, msg):
        self._state['yaw'] = msg.data

    def handle_pitch(self, msg):
        self._state['pitch'] = msg.data

    def handle_roll(self, msg):
        self._state['roll'] = msg.data

    def is_initialized(self):
        return len(self._state) == 6

    def get_state(self):
        return self._state
