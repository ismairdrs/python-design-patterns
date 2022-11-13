from abc import ABC, abstractmethod


class Profile(ABC):
    def __init__(self):
        self.sections = []
        self.create_profile()

    @abstractmethod
    def create_profile(self):
        raise NotImplementedError

    def add_sections(self, section):
        self.sections.append(section)

    def describe_sections(self):
        for section in self.sections:
            section.describe()
