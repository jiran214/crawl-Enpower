import datetime

from mongoengine import *

class User(Document):
    comment_id = StringField(primary_key=True)
    source = StringField()
    update_time = DateTimeField()
    name=StringField()
    content=StringField()
    violation_entry = StringField()
    is_violation = BooleanField()
    index = FloatField()
    emo_score = DictField()
    rumor_score = DictField()
    secrecy_score = DictField()
    similar_score = FloatField()
    sense_score = DictField()
    advertise_score = DictField()
    meta = {
        'collection': 'weibo',
        'indexes': [
            {'fields': ['source']},
            {'fields': ['index']},
            {'fields': ['is_violation']},
            {'fields': ['emo_score']},
            {'fields': ['rumor_score']},
            {'fields': ['secrecy_score']},
            {'fields': ['similar_score']},
            {'fields': ['sense_score']},
            {'fields': ['advertise_score']},
            {'fields': ['is_violation']}

        ]
    }
    def save(self, *args, **kwargs):
        self.update_time = datetime.datetime.now()
        return super(User, self).save(*args, **kwargs)