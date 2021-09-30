import React, { useState } from 'react'
import VideoModal from './index';
import { Modal } from '../../context/Modal'
import { NavLink } from 'react-router-dom'
import AddToPlaylistModal from '../AddToPlaylistModal'


const VideoOpener = ({ video }) => {
  const [showVideoModal, setShowVideoModal] = useState(false)
  const [showPlaylistModal, setShowPlaylistModal] = useState(false)
  const openModal = () => {
    setShowVideoModal(true)
  }

  return (
    <>
      <div className='home-video-content' >
        <div className='top-content'>
          <div className='home-img' style={{ backgroundImage: `url(${video?.userId.profileImgUrl})` }}></div>
          <div className='home-profile-name'><NavLink to={`/users/${video.userId.id}`}>{`${video.userId.username}`}</NavLink></div>
          {/* <button className='home-likes'><i className="fas fa-thumbs-up">{`     ${video.likes.length}`}</i></button> */}
          <i className="fas fa-plus" onClick={() => setShowPlaylistModal(true)}></i>
        </div>
        <div className='bottom-content' onClick={openModal}>
          <div className='home-title'>{`${video.caption}`}</div>
        </div>
      </div>
      {
        showVideoModal && (
          <Modal onClose={() => setShowVideoModal(false)}>
            <VideoModal video={video} />
          </Modal>

        )
      }
      {showPlaylistModal && (
        <Modal onClose={() => setShowPlaylistModal(false)}>
          <AddToPlaylistModal video={video} />
        </Modal>

      )}
    </>
  )

}

export default VideoOpener
