from entities.profile import Profile
from entities.section import Section


class PersonalSection(Section):
    def describe(self):
        print('Personal Section')


class AlbumSection(Section):
    def describe(self):
        print('Album  Section')


class PatentSection(Section):
    def describe(self):
        print('Patent Section')


class PublicationSection(Section):
    def describe(self):
        print('Publication Section')


class Linkedin(Profile):
    def create_profile(self):
        self.add_sections(PersonalSection())
        self.add_sections(PatentSection())
        self.add_sections(PublicationSection())


class Facebook(Profile):
    def create_profile(self):
        self.add_sections(PersonalSection())
        self.add_sections(AlbumSection())


if __name__ == '__main__':
    profile_type = input('Qual perfil você gostaria de criar? [Linkedin or Facebook]')
    profile = eval(profile_type.title())()
    print('Criando perfil...', type(profile).__name__)
    print('O perfil tem as seções --')
    profile.describe_sections()
