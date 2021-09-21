from .db import db


class Comment(db.Model):
    __tablename__ = 'comments'

    id = db.Column(db.Integer, primary_key=True)
    userId = db.Column(db.Integer, db.ForeignKey("users.id"))
    videoId = db.Column(db.Integer, db.ForeignKey('videos.id'))
    content = db.Column(db.String)
    createdAt = db.Column(db.DateTime)

    user = db.relationship('User', back_populates='comments')
    video = db.relationship('Video', back_populates='comments')
    likes = db.relationship('Like', back_populates='comment')
