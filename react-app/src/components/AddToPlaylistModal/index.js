import React, { useEffect } from "react";
import { useDispatch, useSelector } from "react-redux";
import { getPlaylists, addVideo, delVideoFromPlaylist } from "../../store/playlist";


const AddToPlaylistModal = ({ video }) => {
  const sessionUser = useSelector(state => state.session.user);
  const playlists = useSelector(state => Object.values(state.Playlists).filter(playlist => playlist.userId === sessionUser.id))
  const dispatch = useDispatch()


  useEffect(() => {
    (async () => {
      await dispatch(getPlaylists())
    })();

  }, [dispatch])

  const handleChange = async (playlist, _e) => {
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
    return


  }



  return (
    <>
      <form>
        {playlists && playlists.map(playlist =>
          <>
            <label>{`${playlist.title}`}</label>
            <input
              type='checkbox'
              id={`${playlist.id}`}
              name={`${playlist.title}`}
              value={`${playlist.id}`}
              checked={playlist.videos.find(el => el.video.id === video.id)}
              onChange={(e) => handleChange(playlist, e)}
            ></input>
          </>
        )}
      </form>
    </>
  )
}


export default AddToPlaylistModal
