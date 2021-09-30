from app.models import db, PlaylistVideoJoin
from faker import Faker

faker = Faker()


def seed_playlistvideojoins():
    for i in range(75):
        joins = PlaylistVideoJoin(playlistId=faker.random_int(
            min=1, max=40), videoId=faker.random_int(min=1, max=140), createdAt=faker.date())
        db.session.add(joins)
    db.session.commit()


def undo_playlistvideojoins():
    db.session.execute('TRUNCATE playlistvideojoins RESTART IDENTITY CASCADE;')
    db.session.commit()
