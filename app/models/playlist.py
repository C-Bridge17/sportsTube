from .db import db


class Playlist(db.Model):
    __tablename__ = 'playlists'

    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String)
    userId = db.Column(db.Integer, db.ForeignKey("users.id"))
    default = db.Column(db.Boolean, default=False)

    user = db.relationship('User', back_populates='playlists')
    playlists = db.relationship('Playlist', back_populates='playlist')
