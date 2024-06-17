from .userDecorator import UserDecorator


class AdditionalAttributes(UserDecorator):
    def __init__(self, component, attr1, attr2, attr3, attr4):
        super().__init__(component)
        self.attr1 = attr1
        self.attr2 = attr2
        self.attr3 = attr3
        self.attr4 = attr4

    def to_JSON(self):
        data = super().to_JSON()
        data.update({
            'username': self.attr1,
            'contrasena': self.attr2,
            'rol': self.attr3,
            'activo': self.attr4
        })
        return data
