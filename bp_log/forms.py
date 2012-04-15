from flaskext.wtf import Form, IntegerField, Required

class MeasForm(Form):
    sys = IntegerField('Systolic', [Required()])
    dia = IntegerField('Diastolic', [Required()])
    pulse = IntegerField('Pulse', [Required()])
