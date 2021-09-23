from flask import Blueprint, jsonify
from flask_login import current_user
from app.models import Video


video_routes = Blueprint('videos', __name__)


@video_routes.route('/')
def get_videos():
    videos = Video.query.all()
    return {'videos': [video.to_dict_ext() for video in videos]}
