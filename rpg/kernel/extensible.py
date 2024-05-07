class Extensible:
    def __init__(self):
        self.plugins   = {}         #   "name": Plugin
        self.preloaded_plugins = [] # (Plugin, position)[]

    # >>> Serialize everything that belongs to the Extensible, 
    # >>> Will be done in plugin.py, world.py
    def serealize(self):
        raise Exception("Unimplemented!")

    def deserealize(self, obj):
        raise Exception("Unimplemented!")
    # <<<
    # <<<

    # >>> Serialize the plugins of the Extensible
    # >>> This specifically excludes the plugin itself
    def serealize_plugins(self):
        return {
            key: value.serealize()
            for key, value in self.plugins.items()
        }

    def deserealize_plugins(self, obj):
        for key, value in obj.items():
            self.plugins[key].deserealize(value)
    # <<<
    # <<<

    def initialize_self(self):
        pass

    def initialize(self):
        # A bit redundant stuff, maybe write prettier later
        self.preloaded_plugins.sort(key=lambda x: x[1])
        for (plugin, pos) in self.preloaded_plugins:
            if pos < 0:
                plugin.initialize_self()

        self.initialize_self()
        
        for (plugin, pos) in self.preloaded_plugins:
            if pos >= 0:
                plugin.initialize_self()

    def plugin(self, plugin_instance, position = 0):
        self.preloaded_plugins.append((plugin_instance, position))
        plugin_instance.extends_on(self)
        return self

    def if_plugin(self, plugin_name, _):
        return plugin_name in self.plugins