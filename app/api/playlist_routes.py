from flask import Blueprint, jsonify, request
from app.models import Playlist
from app.models import Playlist, db
from datetime import datetime

now = datetime.now()


playlists_routes = Blueprint('playlists', __name__)


@playlists_routes.route('')
def get_playlists():
    playlists = Playlist.query.all()
    return {'playlists': [playlist.to_dict_ext() for playlist in playlists]}

# @playlists_routes.route('', methods=['POST'])
# def postPlaylist():
#     data = request.get_json()['payload']

#     playlist = Playlist(
#     )
#     db.session.add(playlist)
#     db.session.commit()
#     playlists = Playlist.query.all()
#     return {'playlists': [playlist.to_dict_ext() for playlist in playlists]}

# @playlists_routes.route('', methods=['PUT'])
# def put_playlist():
#     data = request.get_json()['payload']
#     comment = Comment.query.get(data['commentId'])
#     comment.content = data['content']
#     db.session.add(comment)
#     db.session.commit()
#     comments = Comment.query.all()
#     return {'comments': [comment.to_dict_ext() for comment in comments]}


# @playlists_routes.route('/<int:commentId>', methods=['DELETE'])
# def delete_comment(commentId):
#     print('asdfafsdfdsasdafadfafsdsdfdffdsafdafdasfdsafd', commentId)
#     comment = Comment.query.get(commentId)
#     db.session.delete(comment)
#     db.session.commit()
#     return 'Comment deleted'
