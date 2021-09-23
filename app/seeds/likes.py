# userId = db.Column(db.Integer, db.ForeignKey("users.id"))
# videoId = db.Column(db.Integer, db.ForeignKey('videos.id'))
# commentId = db.Column(db.Integer, db.ForeignKey('comments.id'))
# createdAt = db.Column(db.DateTime)

from app.models import db, Like
from faker import Faker

faker = Faker()


def seed_likes():
    for i in range(75):
        like = Like(userId=faker.random_int(min=1, max=71), videoId=faker.random_int(
            min=1, max=150), createdAt=faker.date())
        db.session.add(like)
    for i in range(75):
        like = Like(userId=faker.random_int(min=1, max=71), commentId=faker.random_int(
            min=1, max=150), createdAt=faker.date())
        db.session.add(like)
    db.session.commit()


def undo_likes():
    db.session.execute(
        'TRUNCATE likes RESTART IDENTITY CASCADE;')
    db.session.commit()
