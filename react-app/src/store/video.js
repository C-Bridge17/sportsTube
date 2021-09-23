const LOAD = "home/LOAD"

export const loadVideos = payload => ({
  type: LOAD,
  payload
})


export const getVideos = () => async dispatch => {
  const res = await fetch(`/api/videos`, {
    method: 'GET',
    headers: {
      'Access-Control-Allow-Credentials': true,
      'Access-Control-Allow-Origin': '*',
      'Access-Control-Allow-Methods': 'GET',
      'Access-Control-Allow-Headers': 'application/json',
    }
  })

  const payload = await res.json();
  if (res.ok) {
    console.log('------', payload)
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
        videoFeed: videoFeed,
        ...state
      }
    default:
      return state
  }
}

export default Videos
