from .db import db


class Playlist(db.Model):
    __tablename__ = 'playlists'

    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String)
    userId = db.Column(db.Integer, db.ForeignKey("users.id"))
    default = db.Column(db.Boolean, default=False)

    user = db.relationship('User', back_populates='playlists')
    playlist_content = db.relationship(
        'PlaylistVideoJoin', back_populates='playlist', cascade='all, delete')

    def to_dict(self):
        return{
            'id': self.id,
            'title': self.title,
            'userId': self.userId,
            'default': self.default
        }

    def to_dict_ext(self):
        return{
            'id': self.id,
            'title': self.title,
            'userId': self.userId,
            'videos': self.playlist_content.to_dict(),
            'default': self.default
        }
