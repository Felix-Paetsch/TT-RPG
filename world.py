class World:
    _instance = None
    _is_initialized = False

    def __new__(cls):
        if cls._instance is None:
            cls._instance = super(World, cls).__new__(cls)
        return cls._instance
    
    def __init__(self):
        if self._is_initialized:
            return

        self._is_initialized = True
        self.players = []

    def add_player(self, player):
        if self.player(player.name):
            raise Exception("Playername already exists!")

        self.players.append(player)

    def remove_player(self, player_name):
        self.players = [
            player for player in self.players 
            if player.name.lower() != player_name.lower()
        ]

    def get_players(self):
        return self.players

    def player(self, name):
        for player in self.players:
            if player.name.lower() == name.lower():
                return player
        return None
    