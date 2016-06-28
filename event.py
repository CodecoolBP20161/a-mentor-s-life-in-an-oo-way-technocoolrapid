class Event:
    event_id = "energy_level"

    def __init__(self, energy_level, description):
        self.energy_level = energy_level
        self.description = description

        super().__init__()

    def process_event(self):
        return [self.energy_level, self.description, Event.event_id]
