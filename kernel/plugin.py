class Plugin(Extensible):
    def __init__(self, name):
        self.name = name

    def serealize(self):
        raise
    
    def deserealize(self, obj):
        raise