import React, { useEffect } from 'react';
import { useDispatch } from 'react-redux'
import { getPlaylists } from '../../store/playlist';

const ProfilePlaylist = () => {
  const dispatch = useDispatch()

  useEffect(() => {
    (async () => {
      await dispatch(getPlaylists())
    })();
  })

  return (
    <h1>Test</h1>
  )
}

export default ProfilePlaylist
