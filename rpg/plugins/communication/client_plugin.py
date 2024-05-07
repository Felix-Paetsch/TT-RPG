from ...kernel.plugin import Plugin
from ... import World

class ClientPlugin(Plugin):
    def __init__(self):
        super().__init__("client")

    def serealize_self(self):
        return dict()

    def deserealize_self(self, obj):
        pass

    def initialize_self(self):
        # World should have no other plugin!!
        world = self.extends
        world.__class__ = MethodBufferRoot

class MethodBufferRoot():
    def __getattr__(self, item):
        return MethodBuffer([item])

class MethodBuffer():
    def __init__(self, call_chain):
        self.call_chain = call_chain

    def __getattr__(self, item):
        return MethodBuffer(self.call_chain + [item])

    def __call__(self, *args, **kwargs):
        return f'Called world.{ ".".join(self.call_chain) } with args { args } and kwargs { kwargs }'