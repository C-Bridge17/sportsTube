import React, { useEffect, useState } from 'react';
import { useDispatch, useSelector } from 'react-redux'
import { getVideos } from '../../store/video'
import VideoOpener from '../VideoModal/videoOpener'

import './home.css'

const Home = () => {
  const dispatch = useDispatch()
  const [start, setStart] = useState(0)
  const [end, setEnd] = useState(20)
  const videos = useSelector(state => Object.values(state.Videos).slice(start, end))

  useEffect(() => {
    (async () => {
      await dispatch(getVideos())
    })();

  }, [dispatch])

  const Next = (e) => {
    e.preventDefault()
    if (end === 140) return
    let next1 = start + 20
    let next2 = end + 20
    setStart(next1)
    setEnd(next2)
  }
  const Back = (e) => {
    e.preventDefault()
    if (start === 0) return
    let next1 = start - 20
    let next2 = end - 20
    setStart(next1)
    setEnd(next2)

  }




  return (
    <>
      <div className='page-selector'>
        <button onClick={Back}><i className="fas fa-arrow-left"></i></button>
        <button onClick={Next}><i className="fas fa-arrow-right"></i></button>
      </div>
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
    </>
  )
}


export default Home
