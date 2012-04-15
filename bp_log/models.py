from google.appengine.ext import db

class Measurement(db.Model):
    sys = db.IntegerProperty()
    dia = db.IntegerProperty()
    pulse = db.IntegerProperty()
    recorded_time = db.DateTimeProperty(auto_now_add=True)
    user = db.UserProperty(auto_current_user_add=True)

    def get_mat(self):
        return (self.sys - self.dia) * 3

    def to_dict(self):
        return {"sys" : self.sys,
                "dia" : self.dia,
                "pulse" : self.pulse,
                "time" : self.recorded_time.strftime("%H:%M:%S %m/%d/%Y"),
                "user" : self.user.email(),
                "mat" : self.get_mat()}
