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
      <div key={comment?.id}>
        <NavLink to={`/users/${comment?.user?.id}`}>{`${comment?.user?.username}`}</NavLink>
        <div className='home-img' style={{ backgroundImage: `url(${comment?.user?.profileImgUrl})` }}></div>
        <div>{`Likes: ${comment?.likes?.length}`}</div>
        <div>{`${comment?.content}`}</div>
        {isUser && comment?.user.id === sessionUser?.id && !showEdit && (
          <div onClick={() => editHandler(comment)} > edit</div>
        )}
        {showEdit && (
          <EditComment comment={comment} setShowEdit={setShowEdit} sessionUser={sessionUser} video={video} />
        )}
      </div>
    </>
  )
}
export default ShowComment
