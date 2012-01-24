import datetime
from google.appengine.ext import db

def Measurements(db.Model):
    sys = db.IntegerProperty()
    dia = db.IntegerProperty()
    pulse = db.IntegerProperty()
    recorded_time = db.DateTimeProperty(auto_now_add=True)
    user = db.UserProperty()

    def get_mat(self):
        return (sys - dia) * 3