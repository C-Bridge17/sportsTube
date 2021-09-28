import React, { useState } from 'react';
import { Modal } from '../../context/Modal'
import AddToPlaylistModal from '../AddToPlaylistModal'



const ProfileVideos = ({ video }) => {

  const [showPlaylistModal, setShowPlaylistModal] = useState(false)

  return (
    <div className='home-video-container' key={video.id}>
      <div className='home-div'>
        <iframe width="560" height="315" className='home-video' title={`${video.id}`} key={video.id} src={`${video.videoUrl}`} allowFullScreen allow="autoplay"></iframe>
      </div>
      <div className='home-video-content' >
        <div className='top-content'>
          <div className='home-img' style={{ backgroundImage: `url(${video?.userId.profileImgUrl})` }}></div>
          <div className='home-likes'>
            <i className="fas fa-thumbs-up">
              {`   ${video.likes.length}`}</i>
          </div>
          <div className='add-to-playlist' onClick={() => setShowPlaylistModal(true)}>
            <i className="fas fa-plus"></i>
          </div>
        </div>
        <div className='home-title'>{`${video.caption}`}</div>
        {showPlaylistModal && (
          <Modal onClose={() => setShowPlaylistModal(false)}>
            <AddToPlaylistModal video={video} />
          </Modal>

        )}

      </div>
    </div>
  )
}


export default ProfileVideos
