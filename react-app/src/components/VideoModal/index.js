import React from 'react';
import { NavLink } from 'react-router-dom'

const VideoModal = ({ video }) => {

  return (
    <div>
      <iframe height='440' width='800' title={`${video.id}`} key={video.id} src={`${video.videoUrl}`} allowFullScreen hover></iframe>
      <div>
        <div>
          <div style={{ backgroundImage: `url(${video?.userId.profileImgUrl})` }}></div>
          <div><NavLink to={`/users/${video.userId.id}`}>{`${video.userId.username}`}</NavLink></div>
          <div>Likes: {`${video.likes.length}`}</div>
        </div>
        <div>{`${video.caption}`}</div>
        <div>
        </div>
      </div>
    </div>
  )

}
export default VideoModal
