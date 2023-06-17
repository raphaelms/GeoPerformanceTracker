class Group:
    def __init__(self, name, description):
        self.name = name
        self.description = description
        self.locations = []

class Location:
    def __init__(self, name, description, gps_coordinates):
        self.name = name
        self.description = description
        self.gps_coordinates = gps_coordinates
        self.timeseries_scores = []

class TimeseriesScore:
    def __init__(self, score_type, scores):
        self.score_type = score_type
        self.scores = scores  # a list of tuples (timestamp, score)
