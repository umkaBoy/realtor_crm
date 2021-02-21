export default {
  namespaced: true,
  state: {
    isLoading: false
  },
  getters: {
    isLoading: state => state.isLoading
  },
  mutations: {
    setLoader (state, status) {
      state.isLoading = status
    }
  },
  actions: {
    loading ({ commit }, { flag, timeout }) {
      if (timeout) {
        setTimeout(() => {
          commit('setLoader', flag)
        }, timeout)
      } else {
        commit('setLoader', flag)
      }
    }
  }
}
