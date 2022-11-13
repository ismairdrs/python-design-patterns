from robot.interfaces import RobotPlan


class Robot(RobotPlan):
    def __init__(self):
        self._robot_torso = None
        self._robot_head = None
        self._robot_legs = None
        self._robot_arms = None

    @property
    def robot_head(self) -> str:
        return self._robot_head

    @property
    def robot_torso(self) -> str:
        return self._robot_torso

    @property
    def robot_arms(self) -> str:
        return self._robot_arms

    @property
    def robot_legs(self) -> str:
        return self._robot_legs

    @robot_head.setter
    def robot_head(self, head: str) -> None:
        self._robot_head = head

    @robot_torso.setter
    def robot_torso(self, torso: str) -> None:
        self._robot_torso = torso

    @robot_arms.setter
    def robot_arms(self, arms: str) -> None:
        self._robot_arms = arms

    @robot_legs.setter
    def robot_legs(self, legs: str) -> None:
        self._robot_legs = legs
