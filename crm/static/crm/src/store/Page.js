export default {
  namespaced: true,
  state: {
    isLoading: false,
    data: [
      '1',
      '2',
      '3',
      '4',
      '5',
      '6',
      '7',
      '8',
      '9',
      '10',
      '11',
      '12',
      '13',
      '14',
      '15',
      '16',
      '17'
    ]
  },
  getters: {
    isLoading: state => state.isLoading,
    getData: state => state.data
  },
  mutations: {
    setLoader (state, status) {
      state.isLoading = status
    },
    setData (state, data) {
      state.data = data
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
    },
    async load ({ dispatch, commit }) {
      dispatch('Page/loading', {flag: true}, {root: true})
      try {
        console.log('3')
        // const user = await userApi.self()
        // commit('setUser', user)
      } catch (e) {
        dispatch('Alert/add', { type: 'error', text: 'Не удалось загрузить список объектов', timeout: 5000 }, { root: true })
      } finally {
        dispatch('Page/loading', {flag: false, timeout: 300}, {root: true})
      }
    }
  }
}
