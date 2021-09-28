import React, { useEffect, useState } from "react";
import { useDispatch, useSelector } from "react-redux";
import { getPlaylists, addVideo, delVideoFromPlaylist } from "../../store/playlist";
import './playlistModal.css'


const AddToPlaylistModal = ({ video }) => {
  const sessionUser = useSelector(state => state.session.user);
  const playlists = useSelector(state => Object.values(state.Playlists).filter(playlist => playlist.userId === sessionUser.id))
  const dispatch = useDispatch()


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
      await dispatch(addVideo(payload))
    }
    if (found.length) {
      await dispatch(delVideoFromPlaylist(found[0].id, playlist.id))
    }
    await dispatch(getPlaylists())



  }

  const checker = (playlist) => {
    let found = playlist.videos.find(el => el.video.id === video.id)
    if (found) return true
    if (!found) return false
    return
  }



  return (
    <div>
      <form>
        {playlists && playlists.map(playlist =>
          <>

            <label>{`${playlist.title}`}</label>
            <input
              type='checkbox'
              id={`${playlist.id}`}
              name={`${playlist.title}`}
              value={`${playlist.id}`}
              checked={checker(playlist)}
              onChange={(e) => handleChange(playlist, e)}
            ></input>
          </>
        )}
      </form>
    </div>
  )
}


export default AddToPlaylistModal
