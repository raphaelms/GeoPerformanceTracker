from infrastructure import ScoreType, Session


class ScoreTypeService:
    def __init__(self):
        self.session = Session()

    def create_score_type(self, score_type_name):
        new_score_type = ScoreType(Str_ScoreTypeName=score_type_name)
        self.session.add(new_score_type)
        self.session.commit()

    def get_score_type(self, score_type_id):
        score_type = self.session.query(ScoreType).filter_by(Pk_ScoreTypeID=score_type_id).first()
        return score_type

    def update_score_type(self, score_type_id, score_type_name=None):
        score_type = self.session.query(ScoreType).filter_by(Pk_ScoreTypeID=score_type_id).first()
        if score_type and score_type_name:
            score_type.Str_ScoreTypeName = score_type_name
            self.session.commit()

    def delete_score_type(self, score_type_id):
        score_type = self.session.query(ScoreType).filter_by(Pk_ScoreTypeID=score_type_id).first()
        if score_type:
            self.session.delete(score_type)
            self.session.commit()