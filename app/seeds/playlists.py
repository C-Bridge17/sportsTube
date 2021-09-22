from app.models import db, Playlist
from faker import Faker

faker = Faker()


def seed_playlists():
    for i in range(71):
        playlist = Playlist(title='Watch List', userId=i+1, default=True)
        db.session.add(playlist)
    db.session.commit()


def undo_playlists():
    db.session.execute('TRUNCATE playlists RESTART IDENTITY CASCADE;')
    db.session.commit()
