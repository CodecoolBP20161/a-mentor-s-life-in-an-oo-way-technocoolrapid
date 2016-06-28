from event import Event


class Athomosphere(Event):
    _id = "morale"

    def __init__(self, moral_change, moral_message, *args, **kwargs):
        self.moral_change = moral_change
        self.moral_message = moral_message

        super().__init__(*args, **kwargs)

    def process_atmosphere(self):
        return [self.moral_change, self.moral_message, Athomosphere._id]
