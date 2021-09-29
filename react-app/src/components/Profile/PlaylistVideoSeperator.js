import React, { useState } from 'react'
import ProfileVideos from './profileVideos'


const PlaylistVideoSeperator = ({ videos }) => {
  const [start, setStart] = useState(0)
  const [end, setEnd] = useState(4)
  const Next = (e) => {
    e.preventDefault()
    if (end >= videos.length) return
    let next1 = start + 4
    let next2 = end + 4
    setStart(next1)
    setEnd(next2)
  }
  const Back = (e) => {
    e.preventDefault()
    if (start === 0) return
    let next1 = start - 4
    let next2 = end - 4
    setStart(next1)
    setEnd(next2)
  }
  return (
    <>
      <div className='playlist-video-seperate'>
        {videos && videos.slice(start, end).map(video =>
          <ProfileVideos key={video.video.id} video={video.video} />
        )
        }
      </div >
      <div className='playlist-sliders'>
        <div>
          <button hidden={start === 0} onClick={Back}><i className="fas fa-arrow-left"></i></button>
        </div>
        <div>
          <button hidden={end >= videos.length} onClick={Next}><i className="fas fa-arrow-right"></i></button>
        </div>
      </div>
    </>
  )

}

export default PlaylistVideoSeperator
