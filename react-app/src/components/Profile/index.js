import React, { useState, useEffect } from 'react';
import { useSelector, useDispatch } from 'react-redux';
import { useParams } from 'react-router-dom';
import { getVideos } from '../../store/video'
import { getPlaylists } from '../../store/playlist';
import ProfileVideos from './profileVideos';
import ProfilePlaylist from './profilePlaylists';
import './profile.css'

function Profile() {
  const [user, setUser] = useState({});
  const { userId } = useParams();
  const sessionUser = useSelector(state => state.session.user);
  const videos = useSelector(state => Object.values(state.Videos).filter(vid => vid.userId.id === user.id))
  const playlists = useSelector(state => Object.values(state.Playlists).filter(playlist => playlist.userId === +userId))
  const dispatch = useDispatch()
  const [isOwner, setIsOwner] = useState(false)
  const [isHome, setIsHome] = useState(true)
  const [isPlaylist, setIsPlaylist] = useState(false)

  useEffect(() => {
    if (videos.length === 0) {
      handlePlaylistClick()
    }
    return
  }, [videos])

  useEffect(() => {
    (async () => {
      await dispatch(getVideos())
      await dispatch(getPlaylists())
    })();

  }, [dispatch])

  useEffect(() => {
    if (!userId) {
      return;
    }
    (async () => {
      const response = await fetch(`/api/users/${userId}`);
      const user = await response.json();
      setUser(user);
    })();
  }, [userId]);

  if (!user) {
    return null;
  }


  const handleHomeClick = () => {
    setIsHome(true)
    setIsPlaylist(false)
  }
  const handlePlaylistClick = () => {
    if (sessionUser.id === user.id) setIsOwner(true)
    else setIsOwner(false)
    setIsHome(false)
    setIsPlaylist(true)
  }

  return (
    <div className='profile-div'>
      <div className='profile-header'>
        <div className='profile-img-header' style={{ backgroundImage: `url(${user?.profileImgUrl})` }}></div>
        <ul className='header-info'>
          <li className='header-username'>{`${user?.username}`}</li>
        </ul>
        {/* {user?.subbed?.length === 0 && (
            <li>No Subscribers</li>
          )}
          {user?.subbed?.length > 0 && (
            <li>{`Subscribers: ${user?.subbed?.length}`}</li>
          )}
          <div className='sub-button'>
          {subbed && (
            <button>Subscribe</button>
            )}
            {!subbed && (
              <button>unSubscribe</button>
            )} */}
        {/* </div> */}

      </div>
      <ul className='profile-directions'>
        {videos.length > 0 && (
          <li onClick={handleHomeClick}>{`${user?.username}`} Videos</li>
        )}
        <li onClick={handlePlaylistClick}>Playlists</li>

      </ul>
      <div className='profile-container'>
        {isHome && videos && videos.map(video => (
          <ProfileVideos key={video.id} video={video} />
        ))
        }
      </div>
      <div className='playlist-container'>
        {isPlaylist && (
          <ProfilePlaylist playlists={playlists} isOwner={isOwner} />
        )}
      </div>
    </div >
  );
}
export default Profile;
