import React, { useState, useEffect } from 'react';
import { NavLink } from 'react-router-dom'
import { useSelector, useDispatch } from 'react-redux';
import { getComments, postComment } from '../../store/comment'
import ShowComment from '../EditComment/ShowComment';
import './videoModal.css'


const VideoModal = ({ video }) => {
  const sessionUser = useSelector(state => state.session.user);
  const comments = useSelector(state => Object.values(state.Comments).filter(el => el.videoId === video.id).sort((a, b) => b.id - a.id))
  const [newComment, setNewComment] = useState('')
  const dispatch = useDispatch()
  const [isUser, setIsUser] = useState(false)

  useEffect(() => {
    if (!sessionUser) return;
    setIsUser(true)
  }, [sessionUser])

  useEffect(() => {
    (async () => {
      await dispatch(getComments())
    })();

  }, [dispatch])

  const handleSubmit = async (e) => {
    e.preventDefault()
    let payload = {
      userId: sessionUser.id,
      videoId: video.id,
      content: newComment
    }

    await dispatch(postComment(payload))
    await dispatch(getComments())
    setNewComment('')

  }



  return (
    <div className='video-modal-container'>
      <iframe height='440' width='800' title={`${video.id}`} key={video.id} src={`${video.videoUrl}`} allowFullScreen></iframe>
      <div>
        <div>
          <div style={{ backgroundImage: `url(${video?.userId.profileImgUrl})` }}></div>
          <div><NavLink to={`/users/${video.userId.id}`}>{`${video.userId.username}`}</NavLink></div>
          <div>Likes: {`${video.likes.length}`}</div>
        </div>
        <div>{`${video.caption}`}</div>
        <div className='comments-vid-modal'>
          {isUser && (
            <>
              <form onSubmit={handleSubmit}>
                <label>Comment:</label>
                <input
                  required
                  value={newComment}
                  onChange={(e) => setNewComment(e.target.value)}
                ></input>
                <button>Submit</button>
              </form>
            </>
          )}
          {!isUser && (
            <>
              <form>
                <label>Comment: </label>
                <input disabled></input>
                <button disabled>Submit</button>
              </form>
              <label>Log in to leave a comment: </label>
              <button>Log in</button>
            </>
          )}
        </div>

        <div>
          {comments && comments.map(comment =>
            <div key={comment.id} >
              <ShowComment comment={comment} sessionUser={sessionUser} isUser={isUser} video={video} />
            </div>
          )}
          {!comments.length && (
            <p>No Comments yet be the first</p>
          )}
        </div>
      </div>
    </div >

  )

}
export default VideoModal
