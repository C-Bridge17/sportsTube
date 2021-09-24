import React, { useState } from 'react';
import { putComment, getComments, delComment } from "../../store/comment"
import { useDispatch } from 'react-redux';
const EditComment = ({ comment, sessionUser, video, setShowEdit }) => {
  const [editComment, setEditComment] = useState(comment.content)
  const dispatch = useDispatch()




  const editSubmit = (e) => {
    e.preventDefault()
    let payload = {
      commentId: comment.id,
      userId: sessionUser.id,
      videoId: video.id,
      content: editComment
    }
    dispatch(putComment(payload))
    setShowEdit(false)
    setEditComment('')
  }

  const deleteComment = (e) => {
    console.log(comment.id)
    e.preventDefault()
    dispatch(delComment(comment.id))
    setShowEdit(false)
  }


  return (
    <form onSubmit={editSubmit}>
      <label>Comment:</label>
      <input
        required
        value={editComment}
        onChange={(e) => setEditComment(e.target.value)}
      ></input>
      <button>Submit</button>
      <button type='button' onClick={() => setShowEdit(false)}>Cancel</button>
      <button type='button' onClick={deleteComment}>Delete Comment</button>
    </form>

  )
}


export default EditComment
