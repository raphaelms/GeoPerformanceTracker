from sqlalchemy import Column, Integer, String, Float, DateTime, ForeignKey
from sqlalchemy.orm import relationship, backref
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

Base = declarative_base()

class Group(Base):
    __tablename__ = 'groups'
    
    id = Column(Integer, primary_key=True)
    name = Column(String)
    description = Column(String)
    
    locations = relationship("Location", backref="group")

class Location(Base):
    __tablename__ = 'locations'
    
    id = Column(Integer, primary_key=True)
    name = Column(String)
    description = Column(String)
    gps_coordinates = Column(String)  # Store as "lat,long"
    group_id = Column(Integer, ForeignKey('groups.id'))
    
    timeseries_scores = relationship("TimeseriesScore", backref="location")

class TimeseriesScore(Base):
    __tablename__ = 'timeseries_scores'
    
    id = Column(Integer, primary_key=True)
    score_type = Column(String)
    score = Column(Float)
    timestamp = Column(DateTime)
    location_id = Column(Integer, ForeignKey('locations.id'))

# Set up the engine and session
engine = create_engine('sqlite:///gps_performance.db')
Session = sessionmaker(bind=engine)

Base.metadata.create_all(engine)
