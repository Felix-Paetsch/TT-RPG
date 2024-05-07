from .extensible import Extensible

class Plugin(Extensible):
    def __init__(self, name):
        super().__init__()

        self.name    = name
        self.extends = None
        self.version = "0.0"
        self.required_plugins = [] # Plugins this plugin or it's parent needs

    def get_info():
        # TODO
        return {
            "name": name,
            "can_extend": []
        }

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

    def initialize(self):
        for p in self.required_plugins:
            if not self.if_plugin(p):
                raise Exception(f"Required plugin '{ p }' not present.")

        super.initialize()

    def if_plugin(self, plugin_name, propagation = 1):
        if plugin_name in self.plugins:
            return True

        if propagation == 0:
            return False

        return self.extends.if_plugin(plugin_name, propagation - 1)

    def require_plugin(self):
        self.required_plugins.append(self)

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