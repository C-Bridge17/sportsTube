import React, { useState, useEffect } from 'react';
import { NavLink } from 'react-router-dom'
import { useSelector, useDispatch } from 'react-redux';
import { getComments, postComment } from '../../store/comment'
import ShowComment from '../EditComment/ShowComment';
import AddToPlaylistModal from '../AddToPlaylistModal'
import { Modal } from '../../context/Modal'
import './videoModal.css'


const VideoModal = ({ video }) => {
  const sessionUser = useSelector(state => state.session.user);
  const comments = useSelector(state => Object.values(state.Comments).filter(el => el.videoId === video.id).sort((a, b) => b.id - a.id))
  const [showCommentForm, setShowCommentForm] = useState(false)
  const [newComment, setNewComment] = useState('')
  const [showPlaylistModal, setShowPlaylistModal] = useState(false)
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

    if (newComment.trim() === '') return

    if (newComment.trim().length > 120) return alert('Comment is too long. Max of 120 characters.')

    let payload = {
      userId: sessionUser.id,
      videoId: video.id,
      content: newComment.trim()
    }

    setShowCommentForm(false)
    await dispatch(postComment(payload))
    await dispatch(getComments())
    setNewComment('')

  }

  // const handleLike = (e) => {
  //   e.preventDefault()

  // }



  return (
    <>
      <iframe height='440' width='800' title={`${video.id}`} key={video.id} src={`${video.videoUrl}`} allowFullScreen></iframe>
      <div className='video-modal-content-container'>
        <div>{`${video.caption}`}</div>
        <div className='video-modal-content'>
          <div className='video-modal-profile-img' style={{ backgroundImage: `url(${video?.userId.profileImgUrl})` }}></div>
          <div><NavLink to={`/users/${video.userId.id}`}>{`${video.userId.username}`}</NavLink></div>
          {/* <button type='button' onClick={handleLike}><i className="fas fa-thumbs-up">
            {`   ${video.likes.length}`}</i></button> */}
          <i className="fas fa-plus" onClick={() => setShowPlaylistModal(true)}></i>
        </div>
        <div className='comments-vid-modal'>
          <button hidden={showCommentForm} onClick={() => setShowCommentForm(true)}>Leave a Comment</button>
          {isUser && showCommentForm && (
            <div className='comment-form'>
              <form onSubmit={handleSubmit}>
                <label>Comment: </label>
                <input
                  required
                  value={newComment}
                  onChange={(e) => setNewComment(e.target.value)}
                ></input>
                <button>Submit</button>
              </form>
            </div>
          )}
        </div>
        <div className='comment-container'>

          {comments && comments.map(comment =>
            <ShowComment key={comment.id} comment={comment} sessionUser={sessionUser} isUser={isUser} video={video} />
          )}
          {!comments.length && (
            <p>No Comments yet be the first</p>
          )}
        </div>
      </div>
      {showPlaylistModal && (
        <Modal onClose={() => setShowPlaylistModal(false)}>
          <AddToPlaylistModal video={video} />
        </Modal>

      )}
    </>
  )


}
export default VideoModal
