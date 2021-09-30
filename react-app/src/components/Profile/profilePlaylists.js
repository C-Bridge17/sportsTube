import React, { useState } from 'react';
import { useDispatch, useSelector } from 'react-redux';
import EditPlaylistOpen from '../EditPlaylist/editPlaylistOpen';
import { postPlaylist } from '../../store/playlist'
import PlaylistVideoSeperator from './PlaylistVideoSeperator'

const ProfilePlaylist = ({ playlists, isOwner }) => {
  const [title, setTitle] = useState('')
  const sessionUser = useSelector(state => state.session.user);
  const dispatch = useDispatch()

  const handleSubmit = async (e) => {
    e.preventDefault()
    if (title.trim() === '') return

    if (title.trim().length > 120) return alert('Playlist Title is to long.')
    let payload = {
      title: title.trim(),
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
            {playlist.videos && (
              <PlaylistVideoSeperator videos={playlist.videos} />
            )}
          </div>
        </div>
      )}
    </>
  )
}

export default ProfilePlaylist
