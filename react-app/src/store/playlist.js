const LOAD_PLAYLIST = 'playlists/LOAD_PLAYLIST'
const POST_PLAYLIST = "playlists/ADD_PLAYLIST"
const DEL_PLAYLIST = "playlists/DEL_PLAYLIST"
const PUT_PLAYLIST = "playlists/PUT_PLAYLIST"


const addPlaylist = list => ({
  type: POST_PLAYLIST,
  list,
})

const loadPlaylist = list => ({
  type: LOAD_PLAYLIST,
  list,
})
const updatePlaylist = list => ({
  type: PUT_PLAYLIST,
  list,
})
const deletePlaylist = list => ({
  type: DEL_PLAYLIST,
  list,
})

export const postPlaylist = (payload) => async dispatch => {
  const res = await fetch('/api/playlists', {
    method: 'POST',
    headers: {
      'Content-Type': 'application/json',
    },
    body: JSON.stringify({
      payload
    }),
  })
  const list = await res.json()
  if (res.ok) {
    dispatch(addPlaylist(list))
  }
  return list
}

export const getPlaylists = () => async (dispatch) => {
  const response = await fetch(`/api/playlists`)

  const list = await response.json();
  if (response.ok) {
    dispatch(loadPlaylist(list))
  }
  return list
}

export const putPlaylist = (payload, playlistId) => async (dispatch) => {
  const response = await fetch(`/api/playlists/${playlistId}`, {
    method: 'PUT',
    headers: {
      'Content-Type': 'application/json',
    },
    body: JSON.stringify({
      payload
    }),
  })

  const list = await response.json();
  if (response.ok) {
    dispatch(updatePlaylist(list))
  }
  return list
}

export const delPlaylist = (playlistId) => async dispatch => {
  await fetch(`/api/playlists/${playlistId}`, {
    method: 'DELETE'
  })
  dispatch(deletePlaylist(playlistId))

  return
}



const playlistReducer = (state = {}, action) => {
  const playlists = {}
  switch (action.type) {
    case LOAD_PLAYLIST:
      for (let playlist of action.list.playlists) {
        playlists[playlist.id] = playlist
      }
      return {
        ...playlists,
        ...state
      }
    case POST_PLAYLIST: {
      for (let playlist of action.list.playlists) {
        playlists[playlist.id] = playlist
      }
      return {
        ...state,
        ...playlists
      };;
    }
    case PUT_PLAYLIST: {
      const playlists = {}
      for (let playlist of action.list.playlists) {
        playlists[playlist.id] = playlist
      }
      return {
        ...state,
        ...playlists
      };
    }
    case DEL_PLAYLIST: {
      const newState = { ...state };
      delete newState[action.list];
      return newState;
    }
    default:
      return state
  }
}

export default playlistReducer
