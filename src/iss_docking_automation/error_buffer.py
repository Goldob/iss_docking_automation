class ErrorBuffer:
    def __init__(self):
        self._error = {}

    def handle_x_error(self, msg):
        self._error['x'] = msg.data

    def handle_y_error(self, msg):
        self._error['y'] = msg.data

    def handle_z_error(self, msg):
        self._error['z'] = msg.data

    def handle_yaw_error(self, msg):
        self._error['yaw'] = msg.data

    def handle_pitch_error(self, msg):
        self._error['pitch'] = msg.data

    def handle_roll_error(self, msg):
        self._error['roll'] = msg.data

    def is_initialized(self):
        return len(self._error) == 6

    def get_error(self):
        return self._error
