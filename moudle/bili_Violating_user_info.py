import datetime
from mongoengine import *
date = str(datetime.date.today()).replace('-', '')
connect(host="mongodb://localhost:27017/%s" % date, connect=False)

class User(Document):
    mid = StringField(primary_key=True)
    source = StringField()
    update_time = DateTimeField()
    name=StringField()
    content=StringField()
    violation_entry=StringField()
    is_violation=BooleanField()
    index=FloatField()
    emo_score=StringField()#1
    rumor_score = StringField()#3
    secrecy_score = StringField()#2
    similar_score = StringField()#3
    sense_score = StringField()#3
    advertise_score = StringField()#2
    #3  6  9  12

    meta = {
        'collection':'Bilibili',
        'indexes': [
            {'fields': ['source']},
            # {'fields': ['violation_entry']},
            {'fields': ['index']},
            {'fields': ['source']},
            {'fields': ['violation_entry']},
            {'fields': ['is_violation']},
            {'fields': ['is_violation']},
            {'fields': ['emo_score']},
            {'fields': ['rumor_score']},
            {'fields': ['secrecy_score']},
            {'fields': ['similar_score']},
            {'fields': ['sense_score']},
            {'fields': ['advertise_score']}
        ]
    }
    def save(self, *args, **kwargs):
        self.update_time = datetime.datetime.now()
        return super(User, self).save(*args, **kwargs)

