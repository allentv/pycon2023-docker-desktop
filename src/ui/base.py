from abc import ABC, abstractmethod


class LayoutBase(ABC):
    """Defines the methods that has to be present for any UI related layout classes"""

    @abstractmethod
    def get_layout(self) -> list[list]:
        pass
