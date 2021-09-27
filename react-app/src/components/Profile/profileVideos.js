import React from 'react';



const ProfileVideos = ({ video }) => {

  return (
    <div className='home-video-container' key={video.id}>
      <div className='home-div'>
        <iframe width="560" height="315" className='home-video' title={`${video.id}`} key={video.id} src={`${video.videoUrl}`} allowFullScreen allow="autoplay"></iframe>
      </div>
      <div className='home-video-content' >
        <div className='top-content'>
          <div className='home-img' style={{ backgroundImage: `url(${video?.userId.profileImgUrl})` }}></div>
          <div className='home-likes'>Likes: {`${video.likes.length}`}</div>
        </div>
        <div className='home-title'>{`${video.caption}`}</div>

      </div>
    </div>
  )
}


export default ProfileVideos
