from .db import db


class Like(db.Model):
    __tablename__ = 'likes'

    id = db.Column(db.Integer, primary_key=True)
    userId = db.Column(db.Integer, db.ForeignKey("users.id"))
    videoId = db.Column(db.Integer, db.ForeignKey('videos.id'))
    commentId = db.Column(db.Integer, db.ForeignKey('comments.id'))
    createdAt = db.Column(db.DateTime)

    user = db.relationship('User', back_populates='likes')
    video = db.relationship('Video', back_populates='likes')
    comment = db.relationship('Comment', back_populates='likes')
