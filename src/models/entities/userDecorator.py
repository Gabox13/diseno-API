from .userComponent import UserComponent

class UserDecorator(UserComponent):
    
    def __init__(self, component):
        self._component = component

    def to_JSON(self):
        return self._component.to_JSON()