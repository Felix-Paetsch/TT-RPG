from rpg import World
from rpg.plugins.player import PlayerPlugin
from rpg.plugins.communication import ClientPlugin

"""
world = World()
world.plugin(PlayerPlugin())
world.initialize()

Luna = world.Player("Luna", "female")
print(Luna.get_name())

"""

world  = World()
world.plugin(ClientPlugin())
world.initialize()

print(world.Player.wha("Luna", "female"))