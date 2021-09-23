import React from 'react';
import { NavLink } from 'react-router-dom'

const VideoModal = ({ video }) => {

  return (
    <div className='home-video-container'>
      <iframe className='home-video' title={`${video.id}`} key={video.id} src={`${video.videoUrl}`} allowFullScreen hover></iframe>
      <div className='home-video-content'>
        <div className='top-content'>
          <div className='home-img' style={{ backgroundImage: `url(${video?.userId.profileImgUrl})` }}></div>
          <div className='home-profile-name'><NavLink to={`/users/${video.userId.id}`}>{`${video.userId.username}`}</NavLink></div>
          <div className='home-likes'>Likes: {`${video.likes.length}`}</div>
        </div>
        <div className='home-title'>{`${video.caption}`}</div>
        <div>
        </div>
      </div>
    </div>
  )

}
export default VideoModal
