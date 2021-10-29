import React, { useEffect, useState } from "react";
import { useDispatch, useSelector } from "react-redux";
import { getPlaylists, addVideo, delVideoFromPlaylist, postPlaylist } from "../../store/playlist";
import './playlistModal.css'


const AddToPlaylistModal = ({ video }) => {
  const sessionUser = useSelector(state => state.session.user);
  const playlists = useSelector(state => Object.values(state.Playlists).filter(playlist => playlist.userId === sessionUser.id))
  const dispatch = useDispatch()
  const [title, setTitle] = useState('')


  useEffect(() => {
    (async () => {
      await dispatch(getPlaylists())
    })();
  }, [dispatch])

  const handleChange = async (playlist, e) => {
    e.preventDefault()
    let found = playlist.videos.filter(el => el.video.id === video.id)
    if (!found.length) {
      let payload = {
        videoId: video.id,
        playlistId: playlist.id
      }
      await dispatch(addVideo(payload, playlists.id))
    }
    if (found.length) {
      await dispatch(delVideoFromPlaylist(found[0].id, found[0].video.id, playlist.id))
    }
    return
  }

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

  const checker = (playlist) => {
    let found = playlist.videos.find(el => el.video.id === video.id)
    if (found) return true
    if (!found) return false
    return
  }



  return (
    <div className='playlist-add-modal'>
      <iframe className='video-playlist-modal' height='200' width='350' title={`${video.id}`} key={video.id} src={`${video.videoUrl}`}></iframe>
      <div className='new-playlist-form'>
        <h4>New Playlist</h4>
        <form onSubmit={handleSubmit}>
          <input
            className='check-box'
            required
            value={title}
            onChange={(e) => setTitle(e.target.value)}
          ></input>
          <button>Submit</button>
        </form>
      </div>
      <form>
        <div className='add-playlist-form'>
          <p>Check The boxes to add a video to a playlist.
          </p>
          <p>UnCheck to delete from that playlist</p>
          {playlists && playlists.map(playlist =>
            <div key={playlist.id} className='playlist-form-div'>

              <label>{`${playlist.title}`}</label>
              <input
                type='checkbox'
                id={`${playlist.id}`}
                name={`${playlist.title}`}
                value={`${playlist.id}`}
                checked={checker(playlist)}
                onChange={(e) => handleChange(playlist, e)}
              ></input>
            </div>
          )}
        </div>
      </form>
    </div>
  )
}


export default AddToPlaylistModal
