from infrastructure import Session, TimeseriesScore


class TimeseriesScoreService:
    def __init__(self):
        self.session = Session()

    def create_timeseries_score(self, score_type_id, score, timestamp, location_id):
        new_timeseries_score = TimeseriesScore(
            Fk_ScoreTypeID=score_type_id, 
            Vlr_Score=score, 
            Dt_TimeStamp=timestamp, 
            Fk_LocationID=location_id
        )
        self.session.add(new_timeseries_score)
        self.session.commit()
