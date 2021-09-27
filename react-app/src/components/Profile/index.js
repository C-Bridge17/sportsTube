import React, { useState, useEffect } from 'react';
import { useSelector, useDispatch } from 'react-redux';
import { useParams } from 'react-router-dom';
import { getVideos } from '../../store/video'
import ProfileVideos from './profileVideos';
import ProfilePlaylist from './profilePlaylists';
import './profile.css'

function Profile() {
  const [user, setUser] = useState({});
  const { userId } = useParams();
  const sessionUser = useSelector(state => state.session.user);
  const subbed = sessionUser.subbed.filter(subs => subs.id === +userId)
  const videos = useSelector(state => Object.values(state.Videos).filter(vid => vid.userId.id === user.id))
  const dispatch = useDispatch()
  const [isHome, setIsHome] = useState(true)
  const [isPlaylist, setIsPlaylist] = useState(false)

  useEffect(() => {
    (async () => {
      await dispatch(getVideos())
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
    setIsHome(false)
    setIsPlaylist(true)
  }

  return (
    <div className='profile-div'>
      <div className='profile-header'>
        <div className='profile-img-header' style={{ backgroundImage: `url(${user?.profileImgUrl})` }}></div>
        <ul className='header-info'>
          <li className='header-username'>{`${user?.username}`}</li>
          {user?.subbed?.length === 0 && (
            <li>No Subscribers</li>
          )}
          {user?.subbed?.length > 0 && (
            <li>{`Subscribers: ${user?.subbed?.length}`}</li>
          )}
        </ul>
        <div className='sub-button'>
          {subbed && (
            <button>Subscribe</button>
          )}
          {!subbed && (
            <button>unSubscribe</button>
          )}
        </div>

      </div>

      <ul className='profile-directions'>
        <li onClick={handleHomeClick}>Home</li>
        <li onClick={handlePlaylistClick}>Playlists</li>

      </ul>
      <div className='profile-container'>
        {isHome && videos && videos.map(video => (
          <ProfileVideos key={video.id} video={video} />
        ))
        }
      </div>
      {isPlaylist && (
        <ProfilePlaylist />
      )}
    </div>
  );
}
export default Profile;
