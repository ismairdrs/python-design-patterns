from robot.interfaces import RobotBuilder
from robot.entities.robot import Robot


class OldRobotBuilder(RobotBuilder):
    def __init__(self, robot: Robot):
        self.robot = robot

    def build_robot_head(self):
        self.robot.robot_head = "Tin Head"

    def build_robot_torso(self):
        self.robot.robot_torso = "Tin Torso"

    def build_robot_arms(self):
        self.robot.robot_arms = "Tin Arms"

    def build_robot_legs(self):
        self.robot.robot_legs = "Tin Legs Skates"

    def get_robot(self):
        return self.robot


class RaulRobotBuilder(RobotBuilder):
    def __init__(self, robot: Robot):
        self.robot = robot

    def build_robot_head(self):
        self.robot.robot_head = "Raul Head"

    def build_robot_torso(self):
        self.robot.robot_torso = "Raul Torso"

    def build_robot_arms(self):
        self.robot.robot_arms = "Raul Arms"

    def build_robot_legs(self):
        self.robot.robot_legs = "Raul Legs"

    def get_robot(self):
        return self.robot


class RobotEngineer:
    def __init__(self, robot_builder: RobotBuilder):
        self.robot_builder = robot_builder

    def get_robot(self):
        return self.robot_builder.get_robot()

    def make_robot(self):
        self.robot_builder.build_robot_head()
        self.robot_builder.build_robot_torso()
        self.robot_builder.build_robot_arms()
        self.robot_builder.build_robot_legs()


if __name__ == "__main__":
    old_style_robot = OldRobotBuilder(Robot())
    robot_engineer = RobotEngineer(old_style_robot)
    robot_engineer.make_robot()
    first_robot = robot_engineer.get_robot()

    print("Robot Built")
    print(f"Robot Head Type: {first_robot.robot_head}")
    print(f"Robot Torso Type: {first_robot.robot_torso}")
    print(f"Robot Arms Type: {first_robot.robot_arms}")
    print(f"Robot Legs Type: {first_robot.robot_legs}")

    print(50 * "=")
    raul_robot = RaulRobotBuilder(Robot())
    robot_engineer = RobotEngineer(raul_robot)
    robot_engineer.make_robot()
    second_robot = robot_engineer.get_robot()

    print("Robot Built")
    print(f"Robot Head Type: {second_robot.robot_head}")
    print(f"Robot Torso Type: {second_robot.robot_torso}")
    print(f"Robot Arms Type: {second_robot.robot_arms}")
    print(f"Robot Legs Type: {second_robot.robot_legs}")