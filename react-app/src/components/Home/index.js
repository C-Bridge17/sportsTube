import React, { useEffect } from 'react';
import { useDispatch, useSelector } from 'react-redux'
import { getVideos } from '../../store/video'
import VideoOpener from '../VideoModal/videoOpener'

import './home.css'

const Home = () => {
  const dispatch = useDispatch()
  const videos = useSelector(state => Object.values(state.Videos).slice(0, 20))

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
            <iframe width="560" height="315" className='home-video' title={`${video.id}`} key={video.id} src={`${video.videoUrl}`} allowFullScreen allow="autoplay"></iframe>
          </div>
          <VideoOpener video={video} />
        </div>
      ))
      }
    </div >
  )
}


export default Home
