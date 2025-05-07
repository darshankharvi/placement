from enum import Enum
import random
from typing import List
import uuid

class BookingStatus(Enum):
    CONFIRMED = 'CONFIRMED'
    PENDING  = 'PENDING'
    REJECTED = 'REJECTED'
    
class seatAvailablity(Enum):
    AVAILABLE : any
    NOT_AVAILABLE : any
    
class Seat(Enum):
    REGULAR  = 'REGULAR'
    PREMIUM  = 'PREMIUM'
    
class Address():
    def __init__(self,state,city,street,zip):
        self.street = street
        self.city = city
        self.zip = zip
        self.state = state
        
class Account():
    def __init__(self,id,password):
        self.id = id
        self.password = password
 
class SeatShow():
    def __init__(self,seatid,reserved,sType,price):
        self.seatid = seatid
        self.reserved = reserved
        self.stype = sType
        self.price = price
       
class Show():
    #seats = SeatShow()
    def __init__(self,id):
        self.id = id
        self.seats: List[SeatShow] = []

class Movie():
    #shows = Show()
    def __init__(self,movie_name):
        self.movie_name = movie_name
        self.shows : List[Show] = []
        
    def add_show(self,show : Show):
        self.shows.append(show)

class Booking():
    def __init__(self,status : BookingStatus,seats : List[SeatShow], show : Show):
        self.uuid = uuid.uuid4() 
        self.status = status 
        self.seats = seats 
        self.show = show 

        
        
    
        

    