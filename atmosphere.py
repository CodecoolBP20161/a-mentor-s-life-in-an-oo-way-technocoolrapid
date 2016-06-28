class Athomosphere(Event):

    def __init__(self, moral_change, moral_message, _id, *args, **kwargs):
        self.moral_change = moral_change
        self.moral_message = moral_message
        self._id = _id

        super().__init__(*args, **kwargs)

    def process_atmosphere(self):
        return [self.moral_change, self.moral_message, self._id]
