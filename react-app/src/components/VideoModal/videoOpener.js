import React from 'react'
import VideoModal from '../VideoModal';
import { Modal } from '../../context/Modal'
import { NavLink } from 'react-router-dom'


const VideoOpener = ({ video, setShowVideoModal, showVideoModal }) => {

  return (
    <>
      <div className='home-video-content' onClick={() => setShowVideoModal(true)}>
        <div className='top-content'>
          <div className='home-img' style={{ backgroundImage: `url(${video?.userId.profileImgUrl})` }}></div>
          <div className='home-profile-name'><NavLink to={`/users/${video.userId.id}`}>{`${video.userId.username}`}</NavLink></div>
          <div className='home-likes'>Likes: {`${video.likes.length}`}</div>
        </div>
        <div className='bottom-content'>
          <div className='home-title'>{`${video.caption}`}</div>
        </div>
        <div>
        </div>
      </div>
      {showVideoModal && (
        <Modal onClose={() => setShowVideoModal(false)}>
          <VideoModal video={video} showVideoModal={showVideoModal} setShowVideoModal={setShowVideoModal} />
        </Modal>
      )}
    </>
  )

}

export default VideoOpener
