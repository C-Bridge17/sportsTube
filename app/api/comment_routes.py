from flask import Blueprint, jsonify, request
from app.models import Comment
from app.forms.comment_form import commentForm
from app.models import Comment, db
from datetime import datetime

now = datetime.now()


comment_routes = Blueprint('comments', __name__)


@comment_routes.route('', methods=['POST'])
def postCommment():
    data = request.get_json()['payload']

    comment = Comment(
        videoId=data['videoId'],
        userId=data['userId'],
        content=data['content'],
        createdAt=f'{now}'
    )
    db.session.add(comment)
    db.session.commit()
    comments = Comment.query.all()
    return {'comments': [comment.to_dict_ext() for comment in comments]}


@comment_routes.route('')
def get_comments():
    comments = Comment.query.all()
    return {'comments': [comment.to_dict_ext() for comment in comments]}


@comment_routes.route('', methods=['PUT'])
def put_comment():
    data = request.get_json()['payload']
    comment = Comment.query.get(data['commentId'])
    comment.content = data['content']
    db.session.add(comment)
    db.session.commit()
    comments = Comment.query.all()
    return {'comments': [comment.to_dict_ext() for comment in comments]}


@comment_routes.route('/<int:commentId>', methods=['DELETE'])
def delete_comment(commentId):
    comment = Comment.query.get(commentId)
    db.session.delete(comment)
    db.session.commit()
    return 'Comment deleted'
