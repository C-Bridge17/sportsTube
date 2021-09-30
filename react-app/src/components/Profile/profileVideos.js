import React, { useState } from 'react';
import { Modal } from '../../context/Modal'
import AddToPlaylistModal from '../AddToPlaylistModal'
import VideoOpener from '../VideoModal/videoOpener';



const ProfileVideos = ({ video }) => {

  const [showPlaylistModal, setShowPlaylistModal] = useState(false)

  return (
    <div className='home-video-container' key={video.id}>
      <div className='home-div'>
        <iframe width="560" height="315" className='home-video' title={`${video.id}`} key={video.id} src={`${video.videoUrl}`} allowFullScreen allow="autoplay"></iframe>
      </div>
      <div className='home-video-content' >
        <VideoOpener video={video} />
      </div>
    </div>
  )
}


export default ProfileVideos
