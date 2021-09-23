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

    def to_dict(self):
        return{
            'id': self.id,
            'userId': self.userId,
            'videoId': self.videoId,
            'commentId': self.commentId,
            'createdAt': self.createdAt
        }

    def to_dict_ext(self):
        return{
            'id': self.id,
            'userId': self.user.to_dict(),
            'videoId': self.video.to_dict(),
            'commentId': self.commentId.to_dict(),
            'createdAt': self.createdAt
        }

    def to_dict_ext_video(self):
        return{
            'id': self.id,
            'videoId': self.videoId,
            'userId': self.user.to_dict(),
            'createdAt': self.createdAt
        }

    def to_dict_ext_comment(self):
        return{
            'id': self.id,
            'commentId': self.commentId,
            'createdAt': self.createdAt
        }
