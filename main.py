from player import *

Player.adapt_class()

Felix = Player("Felix", "male", "chaotic neutral")
Felix.set_base_wisdom(50)
Felix.set_base_hp(40)
Felix.deplete_hp(2)
print(Felix.hp())


print(dir(Felix))