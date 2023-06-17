import uuid
from sqlalchemy import Column, String, Float, DateTime, ForeignKey, BINARY
from sqlalchemy.orm import relationship, backref
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

Base = declarative_base()

class User(Base):
    __tablename__ = 'users'

    Pk_UserID = Column(BINARY(16), primary_key=True, default=uuid.uuid4)
    Str_UserName = Column(String)
    Str_Password = Column(String)  # This should be hashed before being stored
    Bl_IsActive = Column(bool, default=True)

class ScoreType(Base):
    __tablename__ = 'scoretypes'

    Pk_ScoreTypeID = Column(BINARY(16), primary_key=True, default=uuid.uuid4)
    Str_ScoreTypeName = Column(String)
    
class Group(Base):
    __tablename__ = 'groups'
    
    Pk_GroupID = Column(BINARY(16), primary_key=True, default=uuid.uuid4)
    Str_GroupName = Column(String)
    Str_GroupDescription = Column(String)
    Fk_LastUpdateUser = Column(BINARY(16), ForeignKey('users.Pk_UserID'))
    Dt_LastUpdateTimeStamp = Column(DateTime)

    locations = relationship("Location", backref="group")

class Location(Base):
    __tablename__ = 'locations'
    
    Pk_LocationID = Column(BINARY(16), primary_key=True, default=uuid.uuid4)
    Str_LocationName = Column(String)
    Str_LocationDescription = Column(String)
    Str_GPSCoordinates = Column(String)  # Stored as "lat,long"
    Fk_GroupID = Column(BINARY(16), ForeignKey('groups.Pk_GroupID'))
    Fk_LastUpdateUser = Column(BINARY(16), ForeignKey('users.Pk_UserID'))
    Dt_LastUpdateTimeStamp = Column(DateTime)
    
    timeseries_scores = relationship("TimeseriesScore", backref="location")

class TimeseriesScore(Base):
    __tablename__ = 'timeseries_scores'
    
    Pk_ScoreID = Column(BINARY(16), primary_key=True, default=uuid.uuid4)
    Fk_ScoreTypeID = Column(BINARY(16), ForeignKey('scoretypes.Pk_ScoreTypeID'))
    Vlr_Score = Column(Float)
    Dt_TimeStamp = Column(DateTime)
    Fk_LocationID = Column(BINARY(16), ForeignKey('locations.Pk_LocationID'))
    Fk_LastUpdateUser = Column(BINARY(16), ForeignKey('users.Pk_UserID'))
    Dt_LastUpdateTimeStamp = Column(DateTime)

# Set up the engine and session
engine = create_engine('sqlite:///gps_performance.db')
Session = sessionmaker(bind=engine)

Base.metadata.create_all(engine)
