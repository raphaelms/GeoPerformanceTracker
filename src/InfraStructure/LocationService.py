from infrastructure import Location, Session


class LocationService:
    def __init__(self):
        self.session = Session()

    def create_location(self, location_name, location_description, gps_coordinates, group_id):
        new_location = Location(
            Str_LocationName=location_name, 
            Str_LocationDescription=location_description, 
            Str_GPSCoordinates=gps_coordinates, 
            Fk_GroupID=group_id
        )
        self.session.add(new_location)
        self.session.commit()