class Study(Event):

    def __init__(self, skill_level, describe_study, study_id, *args, **kwargs):
        self.skill_level = skill_level
        self.describe_study = describe_study
        self.study_id = study_id
        
        super().__init__(*args, **kwargs)

    def process_study(self):
        return [self.skill_level, self.describe_study, self.study_id]
