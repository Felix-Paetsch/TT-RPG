from ...kernel.plugin import Plugin
from ... import World
from .player_class import Player

class PlayerPlugin(Plugin):
    def __init__(self):
        super().__init__("player")

    def serealize_self(self):
        return dict()

    def deserealize_self(self, obj):
        pass

    def initialize_self(self):
        world = self.extends

        world.Player = lambda *args: create_player(world, *args)
        world.players = []
        world.add_player    = lambda player : add_player(world, player)
        world.remove_player = lambda player_name : remove_player(world, player_name)
        world.get_players   = lambda : get_players(world)
        world.player        = lambda name : player(world, name)

### Methods to add onto World
def create_player(world, *args):
    p = Player(*args)
    world.add_player(p)
    return p

def add_player(world, player):
    if world.player(player.name):
        raise Exception("Playername already exists!")

    world.players.append(player)

def remove_player(world, player_name):
    world.players = [
        player for player in world.players 
        if player.name.lower() != player_name.lower()
    ]

def get_players(world):
    return world.players

def player(world, name):
    for player in world.players:
        if player.name.lower() == name.lower():
            return player
    return None