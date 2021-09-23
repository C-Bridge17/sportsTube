import React, { useEffect } from 'react';
import { useDispatch, useSelector } from 'react-redux'
import { getVideos } from '../../store/video';

const Home = () => {
  const dispatch = useDispatch()
  const videos = useSelector(state => Object.values(state.Videos).slice(0, 20))


  useEffect(() => {
    (async () => {
      await dispatch(getVideos())
    })();

  }, [dispatch])




  return (
    <>
      {videos && videos.map(video => (
        <div key={video.id}>{`${video.id}`}
          <iframe title={`${video.id}`} key={video.id} src={`${video.videoUrl}`} allowFullScreen></iframe>
        </div>
      ))}
    </>
  )
}


export default Home
