from .db import db


class PlaylistVideoJoin(db.Model):
    __tablename__ = 'PlaylistVideoJoins'

    id = db.Column(db.Integer, primary_key=True)
    playlistId = db.Column(db.Integer, db.ForeignKey("playlists.id"))
    videoId = db.Column(db.Integer, db.ForeignKey('videos.id'))
    createdAt = db.Column(db.DateTime)

    playlist = db.relationship('Playlist', back_populates='playlists')
    video = db.relationship('Video', back_populates='videos')
