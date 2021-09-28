import React, { useState } from 'react';
import ProfileVideos from './profileVideos';
import { useDispatch, useSelector } from 'react-redux';
import EditPlaylistOpen from '../EditPlaylist/editPlaylistOpen';
import { postPlaylist } from '../../store/playlist'

const ProfilePlaylist = ({ playlists, isOwner }) => {
  const [title, setTitle] = useState('')
  const sessionUser = useSelector(state => state.session.user);
  const dispatch = useDispatch()

  const handleSubmit = async (e) => {
    e.preventDefault()
    let payload = {
      title,
      userId: sessionUser.id
    }
    await dispatch(postPlaylist(payload))
    setTitle('')
  }





  return (
    <>
      {isOwner && (
        <div className='new-playlist-form'>
          <h4>New Playlist</h4>
          <form onSubmit={handleSubmit}>
            <input
              required
              value={title}
              onChange={(e) => setTitle(e.target.value)}
            ></input>
            <button>Submit</button>
            <button type='button' onClick={() => setTitle('')}>Cancel</button>
          </form>
        </div>
      )}
      {playlists && playlists.map(playlist =>
        <div key={playlist.id} className='playlist-holder'>
          <EditPlaylistOpen playlist={playlist} />
          <div className='playlist-videos'>
            {playlist.videos && playlist.videos.map(video =>
              <ProfileVideos key={video.id} video={video.video} />
            )}
          </div>
        </div>
      )}
    </>
  )
}

export default ProfilePlaylist