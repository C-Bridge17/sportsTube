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
    videos = db.relationship('Playlist', back_populates='video')
