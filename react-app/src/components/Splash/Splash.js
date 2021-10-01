import React, { useState } from "react"
import LoginForm from '../auth/LoginForm'
import home from './splash images/home_page.png'
import profile from './splash images/profile_page.png'
import video_modal from './splash images/video_modal.png'
import playlist_modal from './splash images/playlist_modal.png'
import './splash.css'

const Splash = () => {
  const [currentShow, setCurrentShow] = useState(1)
  const [showLogIn, setShowLogIn] = useState(true)
  const Next = (e) => {
    e.preventDefault()
    if (currentShow > 5) {
      setShowLogIn(false)
      setCurrentShow(1)
      return
    }
    setShowLogIn(true)
    let next1 = currentShow + 1
    setCurrentShow(next1)
  }
  const Back = (e) => {
    e.preventDefault()
    setShowLogIn(true)
    let next1 = currentShow - 1
    setCurrentShow(next1)
  }

  return (
    <div className='splash-container'>
      <h1>SportsTube</h1>
      <button hidden={!showLogIn} type='button' onClick={() => setShowLogIn(false)}>Log In/Sign Up</button>
      <div className='splash-button-container'>
        <div>
          {currentShow > 1 && (<button onClick={Back}><i className="fas fa-arrow-left"></i></button>)}
        </div>
        <div>
          {currentShow < 5 && (<button onClick={Next}><i className="fas fa-arrow-right"></i></button>)}
        </div>
      </div>
      <div className='splash-slide-container'>
        <div hidden={!(currentShow === 1) || !(showLogIn === true)}>
          <h2>Welcome to SportsTube</h2>
          <h4>
            Click the Arrow above to take a quick tour of SportsTube.
            Already been here? Hit the <button type='button' onClick={() => setShowLogIn(false)}>Log In/Sign Up</button> button to get right into the App.
          </h4>
          <div><iframe width="660" height="415" src="https://www.youtube.com/embed/CEVdca9U9LM" title="YouTube video player" frameborder="0" allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture" allowfullscreen></iframe></div>
        </div>

        <div hidden={!(currentShow === 2) || !(showLogIn === true)}>
          <div>
            <p>
              This the home page where you can view multiple videos from some of the best sports content creators out there.
            </p>
          </div>
          <div>
            <div className='splash-img' style={{ backgroundImage: `url(${home})` }}></div>
          </div>
        </div>

        <div hidden={!(currentShow === 3) || !(showLogIn === true)}>
          <div>
            <p>
              This is a profile page - Find other users through the search bar on the top of screen or go to your own profile by clicking your profile image.
            </p>
          </div>
          <div>
            <div className='splash-profile' style={{ backgroundImage: `url(${profile})` }}></div>
          </div>

        </div>
        <div hidden={!(currentShow === 4) || !(showLogIn === true)}>
          <div>
            <p>
              This is the video pop up where you can view as well as comment on videos.
            </p>
          </div>
          <div>
            <div className='splash-video' style={{ backgroundImage: `url(${video_modal})` }}></div>
          </div>
        </div>

        <div hidden={!(currentShow === 5) || !(showLogIn === true)}>
          <div>
            <p>
              This is the playlist pop up where you add new playlists to store videos that you would like to watch later.</p>
            <p>
              If you already have an existing playlist you would like to add a video to, just click the checkbox next to the playlists name and it will be waiting in your profile page for you.
            </p>
            <p>
              Now that you've seen what this site is about, hit the <button type='button' onClick={() => setShowLogIn(false)}>Log In/Sign Up</button> and sign up or log in as the Demo User to check things out.
            </p>
          </div>
          <div>
            <div className='splash-playlist' style={{ backgroundImage: `url(${playlist_modal})` }}></div>
          </div>
        </div>


        <div hidden={showLogIn}>
          <LoginForm />
        </div>
      </div>
    </div >
  )
}

export default Splash
