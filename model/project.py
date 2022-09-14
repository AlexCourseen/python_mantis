from sys import maxsize


class Project:

    def __init__(self, projectName=None, description=None, id=None):
        self.projectName = projectName
        self.description = description
        self.id = id

    # переопределение функции вывода на косоль - repr
    def __repr__(self):
        return "%s:%s:%s" % (self.id, self.projectName, self.description)

    # переопределение стандартной функции - eq, где other - объект с которым сранивать текущий объект self
    def __eq__(self, other):
        return (self.id is None or other.id is None or self.id == other.id) \
               and self.projectName == other.projectName and self.description == other.description

    def id_or_max(self):
        if self.id:
            return int(self.id)
        else:
            return maxsize