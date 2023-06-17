from infrastructure import Group, Session


class GroupService:
    def __init__(self):
        self.session = Session()

    def create_group(self, group_name, group_description):
        new_group = Group(Str_GroupName=group_name, Str_GroupDescription=group_description)
        self.session.add(new_group)
        self.session.commit()
