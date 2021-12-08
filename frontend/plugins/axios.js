export default function ({ $axios, redirect }) {
  /**
   * Refresh the access token
   * TODO: finish this function then test it
   */
  $axios.onError((error) => {
    const originalConfig = error.config
    if (error.response) {
      if (error.response.status === 401 && !originalConfig._retry) {
        originalConfig._retry = true

        // Do something, call refreshToken() request for example
        return this.$axios(originalConfig)
      }

      if (error.response.status !== 401) {
        return Promise.reject(error.response.data)
      }
    }

    return Promise.reject(error)
  })
}
