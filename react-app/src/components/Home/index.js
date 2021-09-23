import React, { useEffect } from 'react';
import { useDispatch } from 'react-redux'
import { getVideos } from '../../store/video';

const Home = () => {
  const dispatch = useDispatch()

  useEffect(() => {

    (async () => {
      await dispatch(getVideos())
    })();

  }, [dispatch])




  return (
    <>
      <iframe src="https://www.youtube.com/embed/X7eyXz4AKq8" ></iframe>
      <h1>home</h1>
    </>
  )
}


export default Home
