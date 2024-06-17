from abc import ABC, abstractmethod
class UserComponent(ABC):
    @abstractmethod
    def to_JSON(self):
        pass
