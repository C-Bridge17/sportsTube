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
    likes = db.relationship(
        'Like', back_populates='comment', cascade='all, delete')

    def to_dict(self):
        return {
            'id': self.id,
            'userId': self.userId,
            'videoId': self.videoId,
            'content': self.content,
            'createdAt': self.createdAt.strftime('%m/%d/%Y %H:%M:%S')

        }

    def to_dict_ext(self):
        return{
            'id': self.id,
            'user': self.user.to_dict(),
            'content': self.content,
            'videoId': self.videoId,
            'createdAt': self.createdAt.strftime('%m/%d/%Y %H:%M:%S'),
            'likes': [like.to_dict_ext_comment() for like in self.likes]
        }
