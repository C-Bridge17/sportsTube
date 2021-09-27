import React, { useState } from 'react'
import EditComment from '../EditComment'
import { NavLink } from 'react-router-dom'

const ShowComment = ({ comment, sessionUser, isUser, video }) => {
  const [showEdit, setShowEdit] = useState(false)


  const editHandler = () => {
    setShowEdit(true)
  }

  return (
    <>
      <div key={comment?.id} className='comments'>
        <div className='comment-user-info'>
          <div className='home-img' style={{ backgroundImage: `url(${comment?.user?.profileImgUrl})` }}></div>
          <NavLink to={`/users/${comment?.user?.id}`}>{`${comment?.user?.username}`}</NavLink>
        </div>
        <div className='comment-content-div'>
          {showEdit && (
            <EditComment comment={comment} setShowEdit={setShowEdit} sessionUser={sessionUser} video={video} />
          )}
          <div className='comment-content-area' hidden={showEdit}>{`${comment?.content}`}</div>
          <div >{`Likes: ${comment?.likes?.length}`}</div>
          {isUser && comment?.user.id === sessionUser?.id && !showEdit && (
            <div onClick={() => editHandler(comment)} > edit</div>
          )}
        </div>
      </div>
    </>
  )
}
export default ShowComment
