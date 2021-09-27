import EditPlaylist from "."
import { useState } from "react"
import { delPlaylist } from '../../store/playlist'
import { useDispatch } from 'react-redux';


const EditPlaylistOpen = ({ playlist }) => {
  const [showEdit, setShowEdit] = useState(false)
  const dispatch = useDispatch()


  const handleDelete = async (e, playlist) => {
    e.preventDefault()
    await dispatch(delPlaylist(playlist.id))
  }


  return (
    <>
      <h1 hidden={showEdit}>{`${playlist.title}`}</h1>
      {showEdit && (
        <EditPlaylist setShowEdit={setShowEdit} playlist={playlist} />
      )}
      {playlist.default === false && (
        <div hidden={showEdit}>
          <button type='button' onClick={(e) => handleDelete(e, playlist)}>Delete</button>
          <button type='button' onClick={() => setShowEdit(true)}>Edit</button>
        </div>
      )}
    </>
  )

}
export default EditPlaylistOpen
