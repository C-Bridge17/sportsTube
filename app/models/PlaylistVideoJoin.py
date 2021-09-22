from .db import db


class PlaylistVideoJoin(db.Model):
    __tablename__ = 'playlistvideojoins'

    id = db.Column(db.Integer, primary_key=True)
    playlistId = db.Column(db.Integer, db.ForeignKey("playlists.id"))
    videoId = db.Column(db.Integer, db.ForeignKey('videos.id'))
    createdAt = db.Column(db.DateTime)

    playlist = db.relationship('Playlist', back_populates='playlist_content')
    video = db.relationship('Video', back_populates='videos')

    def to_dict(self):
        return {
            'id': self.id,
            'playlist': self.playlist.to_dict(),
            'video': self.video.to_dict(),
            'createdAt': self.createdAt.strftime('%m/%d/%Y %H:%M:%S')
        }
