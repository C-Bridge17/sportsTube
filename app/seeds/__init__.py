from flask.cli import AppGroup
from .users import seed_users, undo_users
from .videos import seed_videos, undo_videos
from .comments import seed_comments, undo_comments
from .likes import seed_likes, undo_likes
from .playlists import seed_playlists, undo_playlists
from .playlistvideojoin import seed_playlistvideojoins, undo_playlistvideojoins

# Creates a seed group to hold our commands
# So we can type `flask seed --help`
seed_commands = AppGroup('seed')


# Creates the `flask seed all` command
@seed_commands.command('all')
def seed():
    seed_users()
    seed_videos()
    seed_comments()
    seed_likes()
    seed_playlists()
    seed_playlistvideojoins()
    # Add other seed functions here


# Creates the `flask seed undo` command
@seed_commands.command('undo')
def undo():
    undo_users()
    undo_videos()
    undo_comments()
    undo_likes()
    undo_playlists()
    undo_playlistvideojoins()
    # Add other undo functions here
