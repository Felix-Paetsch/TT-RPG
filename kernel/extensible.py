class Extensible:
    def __init__(self):
        self.plugins   = {}
        self.preloaded_plugins = []

    def serealize(self):
        raise Exception("Unimplemented!")

    def deserealize(self, obj):
        raise Exception("Unimplemented!")

    def serealize_self(self):
        raise Exception("Unimplemented!")

    def deserealize_self(self, obj):
        raise Exception("Unimplemented!")

    def initialize(self):
        raise

    def plugin(self, plugin, position = 0):
        self.preloaded_plugins.append(plugin)
        return self

    def if_plugin(plugin_name):
        raise