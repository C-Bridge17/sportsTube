from app.models import db, Comment
from faker import Faker

faker = Faker()


# id = db.Column(db.Integer, primary_key=True)
#     userId = db.Column(db.Integer, db.ForeignKey("users.id"))
#     videoId = db.Column(db.Integer, db.ForeignKey('videos.id'))
#     content = db.Column(db.String)
#     createdAt = db.Column(db.DateTime)
userId = faker.random_int(min=1, max=53)


def seed_comments():
    for i in range(150):
        comment = Comment(userId=faker.random_int(min=1, max=71), videoId=faker.random_int(
            min=1, max=150), content=faker.sentence(), createdAt=faker.date())
        db.session.add(comment)
    db.session.commit()


def undo_comments():
    db.session.execute(
        'TRUNCATE comments RESTART IDENTITY CASCADE;')
    db.session.commit()
