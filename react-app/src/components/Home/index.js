import React, { useEffect, useState } from 'react';
import { useDispatch, useSelector } from 'react-redux'
import { NavLink } from 'react-router-dom'
import { getVideos } from '../../store/video'
import VideoOpener from '../VideoModal/videoOpener'

import './home.css'

const Home = () => {
  const dispatch = useDispatch()
  const videos = useSelector(state => Object.values(state.Videos).slice(0, 20))
  const [showVideoModal, setShowVideoModal] = useState(false)

  useEffect(() => {
    (async () => {
      await dispatch(getVideos())
    })();

  }, [dispatch])





  return (
    <div className='home-container'>
      {videos && videos.map(video => (
        <div className='home-video-container' key={video.id}>
          <div className='home-div'>
            <iframe className='home-video' title={`${video.id}`} key={video.id} src={`${video.videoUrl}`} allowFullScreen></iframe>
          </div>
          <VideoOpener video={video} showVideoModal={showVideoModal} setShowVideoModal={setShowVideoModal} />
        </div>
      ))
      }
    </div >
  )
}


export default Home
