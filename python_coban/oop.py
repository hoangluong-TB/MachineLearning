class person:
    def __init__(self, person, family):
        self._person = person
        self.family = family
    @property
    def get(self):
        return self.family
student = person('hoang', ["luong", "quang", "hoang"])
print(student.get)
print(student.family)

