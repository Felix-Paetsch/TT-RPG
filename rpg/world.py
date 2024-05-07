from .kernel import Extensible

class World(Extensible):
    def __init__(self):
        super().__init__()

    def serealize(self):
        return self.serealize_plugins()

    def deserealize(self, obj):
        return self.deserealize_plugins(obj)