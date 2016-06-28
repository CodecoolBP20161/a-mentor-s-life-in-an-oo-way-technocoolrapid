class Event:

    def __init__(self, energy_level, description, event_id):
        self.energy_level = energy_level
        self.description = description
        self.event_id = event_id

        super().__init__()

    def process_event(self):
        return [self.energy_level, self.description, self.event_id]
