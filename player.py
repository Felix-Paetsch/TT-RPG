from utils.load_obj import *
from world import *
from utils.option import Option

class Player:
    def __init__(self, name, sex, alignment):
        self.name = name
        self.sex  = sex
        self.alignment = alignment
        self.parameters = {
            # "param": int
        }
        self.resources  = {
            # "some_name": {
            #    "base":     int           # As computed via base stats
            #    "depleted": int           # How much is gone
            # }
        }

        World().add_player(self)

    # Stats
    def get_base_stat(self, stat):
        stat = stat.lower()
        return self.parameters.get(stat)

    def set_base_stat(self, stat, value):
        stat = stat.lower()
        self.parameters[stat] = value
        return value

    def get_stat(self, stat):
        stat = stat.lower()
        base = self.get_base_stat(stat)
        mult = self.get_stat_multiplyer(stat)

        if base is None or mult is None:
            return None

        return base*mult

    def get_stat_multiplyer(self, stat):
        stat = stat.lower()
        return 1

    # Resources
    def set_base_resource(self, resource, value):
        resource  = resource.lower()
        depletion = self.get_resource_depletion(resource)

        self.resources[resource] = {
            "base": value,
            "depleted": depletion
        }

    def get_base_resource(self, resource):
        resource = resource.lower()
        return Option(self.resources)  \
                    .get(resource)     \
                    .get("base")       \
                    .resolve()

    def get_max_resource(self, resource):
        # TODO
        resource = resource.lower()
        return self.get_base_resource(resource)

    def get_resource_depletion(self, resource):
        resource = resource.lower()
        return Option(self.resources)  \
                    .get(resource)      \
                    .get("depleted")    \
                    .resolve(0)

    def get_current_resource(self, resource):
        resource = resource.lower()
        
        return max(self.get_max_resource(resource) - self.get_resource_depletion(resource), 0)

    def set_resource_depletion(self, resource, depletion):
        resource = resource.lower()

        try:
            Option(self.resources)  \
                .get(resource)      \
                .resolve(None)["depleted"] = depletion
        except:
            raise Exception("Resource doesn't exist on player")

        return self.get_current_resource(resource)

    def deplete_resource(self, resource, amt):
        resource = resource.lower()
        return self.set_resource_depletion(
            resource,
            min(
                max(
                    self.get_resource_depletion(resource) + amt,
                    0
                ),
                self.get_max_resource(resource)
            )   
        )

    def restore_resource(self, resource, amt):
        return self.deplete_resource(resource, -amt)


    @classmethod
    def add_stat_methods(cls, stat):
        """
            Adding the methods
            - Player.base_<stat_name>
            - Player.<stat_name>
            - Player.set_<stat_name>
            - Player.<stat_name>_multiplyer
        """

        stat = stat.lower()
        # Base Stat
        setattr(cls, f'base_{stat}', lambda self: self.get_base_stat(stat))
        setattr(cls, stat, lambda self: self.get_stat(stat))
        setattr(cls, f'set_base_{stat}', lambda self, value : self.set_base_stat(stat, value))

        # Multiplyer
        setattr(cls, f'{stat}_multiplyer', lambda self: self.get_stat_multiplyer(stat))

    
    @classmethod
    def add_resource_methods(cls, resource):
        """
            Adding the methods
            - Player.max_<resource_name>
            - Player.set_base_<resource_name>
            - Player.<resource_name>
            - Player.restore_<resource_name>
            - Player.deplete_<resource_name>
        """

        resource = resource.lower()
        
        setattr(cls, f'base_{resource}', lambda self: self.get_base_resource(resource))
        setattr(cls, f'max_{resource}',  lambda self: self.get_max_resource(resource))
        setattr(cls, resource, lambda self: self.get_current_resource(resource))
        setattr(cls, f'set_base_{resource}',  lambda self, value : self.set_base_resource(resource, value))
        
        setattr(cls, f'deplete_{resource}', lambda self, amt: self.deplete_resource(resource, amt))
        setattr(cls, f'restore_{resource}', lambda self, amt: self.restore_resource(resource, amt))
        setattr(cls, f'cleanse_{resource}', lambda self: self.restore_resource(resource, float('inf')))

    @classmethod
    def adapt_class(
        cls, 
        stats_fp = "./game_settings/stats.json", 
        resources_fp = "./game_settings/resources.json"
    ):
        # Initialize Custom World Methods
        possible_stats = load_obj(stats_fp)
        for stat in possible_stats:
            Player.add_stat_methods(stat)

        resources = load_obj(resources_fp)
        for r in resources:
            Player.add_resource_methods(r)



