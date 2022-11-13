from abc import ABC, abstractmethod


class RobotPlan(ABC):

    @property
    @abstractmethod
    def robot_head(self) -> str:
        pass

    @property
    @abstractmethod
    def robot_torso(self) -> str:
        pass

    @property
    @abstractmethod
    def robot_arms(self) -> str:
        pass

    @property
    @abstractmethod
    def robot_legs(self) -> str:
        pass


class RobotBuilder(ABC):
    @abstractmethod
    def build_robot_head(self):
        raise NotImplementedError

    @abstractmethod
    def build_robot_torso(self):
        raise NotImplementedError

    @abstractmethod
    def build_robot_arms(self):
        raise NotImplementedError

    @abstractmethod
    def build_robot_legs(self):
        raise NotImplementedError

    @abstractmethod
    def get_robot(self):
        raise NotImplementedError
