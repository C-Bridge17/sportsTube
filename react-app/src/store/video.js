const LOAD = "home/LOAD"

export const loadVideos = payload => ({
  type: LOAD,
  payload
})


export const getVideos = () => async dispatch => {
  const res = await fetch(`/api/videos`)

  const payload = await res.json();
  if (res.ok) {
    dispatch(loadVideos(payload.videos))
  }
  return payload
}


const Videos = (state = {}, action) => {
  const videoFeed = {}
  switch (action.type) {
    case LOAD:
      for (let video of action.payload) {
        videoFeed[video.id] = video
      }
      return {
        ...videoFeed,
        ...state
      }
    default:
      return state
  }
}

export default Videos
