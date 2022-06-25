import ax from 'axios'

const BaseApiURL = "https://stp0sndz7b.execute-api.us-east-1.amazonaws.com/"
export const nodeAxios = ax.create({
  baseURL: `${BaseApiURL}`,
  headers: {
    'Content-Type': 'application/json',

  },
  timeout: 3000
})

nodeAxios.interceptors.response.use(
  res => res,
  err => {
    console.log('🚀 ~ file: axios.js ~ line 19 ~ err', err)
    throw err
  }
)
