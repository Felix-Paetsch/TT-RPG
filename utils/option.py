class Option:
    def __init__(self, thing):
        self.value = thing # Dict || None

    def get(self, attr):
        if self.value is None:
            return self

        return Option(self.value.get(attr, None))

    def resolve(self, default = None):
        if self.value is None:
            return default

        return self.value
        
            