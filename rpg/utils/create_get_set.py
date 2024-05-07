def create_get_set(thing, name):
    def _get(self):
        return getattr(self, name)

    def _set(self, val):
        setattr(self, name, val)
        return self

    setattr(thing, f"get_{name}", _get)
    setattr(thing, f"set_{name}", _set)