from infrastructure import Session, User


class UserService:
    def __init__(self):
        self.session = Session()

    def create_user(self, username, password):
        new_user = User(
            Str_UserName=username,
            Str_Password=password  # Hash before storing in real-life application
        )
        self.session.add(new_user)
        self.session.commit()

    def get_user(self, user_id):
        user = self.session.query(User).filter_by(Pk_UserID=user_id).first()
        return user

    def update_user(self, user_id, username=None, password=None):
        user = self.session.query(User).filter_by(Pk_UserID=user_id).first()
        if user:
            if username:
                user.Str_UserName = username
            if password:
                user.Str_Password = password  # Hash before storing in real-life application
            self.session.commit()
        else:
            raise Exception("User not found")

    def delete_user(self, user_id):
        user = self.session.query(User).filter_by(Pk_UserID=user_id).first()
        if user:
            self.session.delete(user)
            self.session.commit()
        else:
            raise Exception("User not found")
