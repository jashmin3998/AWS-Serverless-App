const { nodeAxios } = require('./axios')

export const uploadfile = async body => {
  return await nodeAxios.post('v1', JSON.stringify(body))
}