from event import Event


class Study(Event):
    study_id = "skill_level"

    def __init__(self, skill_level, describe_study, *args, **kwargs):
        self.skill_level = skill_level
        self.describe_study = describe_study

        super().__init__(*args, **kwargs)

    def process_study(self):
        return [self.skill_level, self.describe_study, Study.study_id]
