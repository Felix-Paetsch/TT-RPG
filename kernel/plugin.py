class Plugin(Extensible):
    def __init__(self, name):
        self.name    = name
        self.extends = None

    def serealize(self):
        return {
            "name": self.name,
            "sub_plugins": self.serealize_plugins(),
            "self": self.serealize_self()
        }
    
    def deserealize(self, obj):
        self.deserealize_self(obj["self"])
        self.deserealize_plugins(obj["sub_plugins"])

    def extends_on(self, extends):
        self.extends = extends

    def if_plugin(self, plugin_name, propagation):
        if plugin_name in self.plugins:
            return True

        if propagation == 0:
            return False

        return self.extends.if_plugin(plugin_name, propagation - 1)

    # >>> The following should be overwritten by plugin
    # >>>
    def serealize_self(self):
        # Default:
        ### return dict()
        raise Exception("Unimplemented!")

    def deserealize_self(self, obj):
        # Default:
        ### pass
        raise Exception("Unimplemented!")

    def initialize_self(self):
        # Default:
        ### pass
        raise Exception("Unimplemented!")
    # <<<
    # <<<