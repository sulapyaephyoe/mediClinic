import { createStore } from 'vuex'

export default createStore({
  state: {
    isLoading: false,
    isAuthenticated: false,
    isAdmin: false,
    token: '',
  },
  getters: {
  },
  mutations: {
    initializeStore(state) {
      if (localStorage.getItem('token')) {
        state.isAuthenticated = true
        state.token = localStorage.getItem('token')
      } else {
        state.token = ''
        state.isAuthenticated = false
      }
    },
    setIsLoading(state, status) {
      state.isLoading = status
    },
    setToken(state, token){
      state.token = token
      state.isAuthenticated = true
    },
    removeToken(state) {
      state.token = ''
      state.isAuthenticated = false
    },
    adminRole(state, status) {
      state.isAdmin = status
      console.log(state.isAdmin)
    },
  },
  actions: {
  },
  modules: {
  }
})
