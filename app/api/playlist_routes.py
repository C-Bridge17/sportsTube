from flask import Blueprint, jsonify, request
from app.models import Playlist, PlaylistVideoJoin, db
from datetime import datetime

now = datetime.now()


playlists_routes = Blueprint('playlists', __name__)


@playlists_routes.route('')
def get_playlists():
    playlists = Playlist.query.all()
    return {'playlists': [playlist.to_dict_ext() for playlist in playlists]}


@playlists_routes.route('', methods=['POST'])
def postPlaylist():
    data = request.get_json()['payload']

    playlist = Playlist(
        userId=data['userId'],
        title=data['title'],
        default=False
    )
    db.session.add(playlist)
    db.session.commit()
    playlists = Playlist.query.all()
    return {'playlists': [playlist.to_dict_ext() for playlist in playlists]}


@playlists_routes.route('/<int:playlistId>', methods=['PUT'])
def put_playlist(playlistId):
    data = request.get_json()['payload']
    playlist = Playlist.query.get(playlistId)
    playlist.title = data['title']
    db.session.add(playlist)
    db.session.commit()
    playlists = Playlist.query.all()
    return {'playlists': [playlist.to_dict_ext() for playlist in playlists]}


@playlists_routes.route('/<int:playlistId>', methods=['DELETE'])
def delete_playlist(playlistId):
    playlist = Playlist.query.get(playlistId)
    db.session.delete(playlist)
    db.session.commit()
    return 'Playlist deleted'


@playlists_routes.route('/video', methods=['POST'])
def postVideoToPlaylist():
    data = request.get_json()['payload']

    video = PlaylistVideoJoin(
        videoId=data['videoId'],
        playlistId=data['playlistId'],
        createdAt=f'{now}'
    )
    db.session.add(video)
    db.session.commit()
    playlists = Playlist.query.all()
    return {'playlists': [playlist.to_dict_ext() for playlist in playlists]}


@playlists_routes.route('/video/<int:playlistJoinsId>', methods=['DELETE'])
def delete_video(playlistJoinsId):
    video = PlaylistVideoJoin.query.get(playlistJoinsId)
    db.session.delete(video)
    db.session.commit()
    return 'Video deleted from playlist'
