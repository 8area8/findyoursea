export const state = () => ({
  authenticated: false
})

export const mutations = {
  authenticated (state, authenticated) {
    state.authenticated = authenticated
  }
}

export const actions = {
  async login ({ commit }, data) {
    try {
      const response = await this.$axios.post('/token/', data)
      console.log(response)
      if (response.data.access) {
        commit('authenticated', true)
        localStorage.setItem('access', response.data.access)
        this.$axios.setToken(response.data.access, 'Bearer')
      }
      if (response.data.refresh) {
        localStorage.setItem('access', response.data.refresh)
      }
      return response.status
    } catch (err) {
      console.log(err)
    }
  }
}
