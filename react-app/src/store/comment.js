const LOAD_COMMENT = 'comments/LOAD_COMMENT'
const POST_COMMENT = "comments/ADD_COMMENT"
const DEL_COMMENT = "comments/DEL_COMMENT"
const PUT_COMMENT = "comments/PUT_COMMENT"


const addComment = list => ({
  type: POST_COMMENT,
  list,
})

const loadComments = list => ({
  type: LOAD_COMMENT,
  list,
})
const updateComment = list => ({
  type: PUT_COMMENT,
  list,
})
const deleteComment = list => ({
  type: DEL_COMMENT,
  list,
})

export const postComment = (payload) => async dispatch => {
  const res = await fetch('/api/comments', {
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
    dispatch(addComment(list))
  }
  return list
}

export const getComments = () => async (dispatch) => {
  const response = await fetch(`/api/comments`)

  const list = await response.json();
  if (response.ok) {
    dispatch(loadComments(list))
  }
  return list
}

export const putComment = (payload) => async (dispatch) => {
  const response = await fetch(`/api/comments`, {
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
    dispatch(updateComment(list))
  }
  return list
}

export const delComment = (commentId) => async dispatch => {
  await fetch(`/api/comments/${commentId}`, {
    method: 'DELETE'
  })
  dispatch(deleteComment(commentId))

  return
}



const commentReducer = (state = {}, action) => {
  switch (action.type) {
    case LOAD_COMMENT:
      const comments = {}
      for (let comment of action.list.comments) {
        comments[comment.id] = comment
      }
      return {
        ...comments,
        ...state
      }
    case POST_COMMENT: {
      const comments = {}
      for (let comment of action.list.comments) {
        comments[comment.id] = comment
      }
      return {
        ...state,
        comments: comments
      };;
    }
    case PUT_COMMENT: {
      const comments = {}
      for (let comment of action.list.comments) {
        comments[comment.id] = comment
      }
      return {
        ...state,
        ...comments
      };;
    }
    case DEL_COMMENT: {
      const newState = { ...state };
      delete newState[action.list];
      return newState;
    }
    default:
      return state
  }
}

export default commentReducer
