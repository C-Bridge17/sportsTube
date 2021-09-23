from .db import db


class Video(db.Model):
    __tablename__ = "videos"

    id = db.Column(db.Integer, primary_key=True)
    caption = db.Column(db.String)
    videoUrl = db.Column(db.String, nullable=False)
    userId = db.Column(db.Integer, db.ForeignKey("users.id"))
    createdAt = db.Column(db.DateTime)

    user = db.relationship('User', back_populates='videos')
    likes = db.relationship('Like', back_populates='video')
    comments = db.relationship('Comment', back_populates='video')
    videos = db.relationship(
        'PlaylistVideoJoin', back_populates='video', cascade='all, delete')

    def to_dict(self):
        return {
            'id': self.id,
            'caption': self.caption,
            'videoUrl': self.videoUrl,
            'userId': self.userId,
            'createdAt': self.createdAt
        }

    def to_dict_ext(self):
        return {
            'id': self.id,
            'caption': self.caption,
            'videoUrl': self.videoUrl,
            'userId': self.user.to_dict(),
            'createdAt': self.createdAt,
            'likes': [like.to_dict_ext_video() for like in self.likes]
        }
