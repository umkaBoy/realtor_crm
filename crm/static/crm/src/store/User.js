import * as userApi from '@/api/User'

export default {
  namespaced: true,
  state: {
    user: {}
  },
  getters: {
    getFullName: state => {
      return state.user && state.user.first_name ? `${state.user.first_name} ${state.user.last_name}`
        .replaceAll('undefined', '') : ''
    },
    user: state => state.user,
    isAdmin: state => state.user && !!state.user.is_superuser,
    isStaff: state => state.user && !!state.user.is_staff
  },
  mutations: {
    setUser (state, user) {
      state.user = user
    }
  },
  actions: {
    async load ({ dispatch, commit }) {
      dispatch('Page/loading', {flag: true}, {root: true})
      try {
        const user = await userApi.self()
        commit('setUser', user)
      } catch (e) {
        dispatch('Alert/add', { type: 'error', text: 'Не удалось загрузить профиль', timeout: 5000 }, { root: true })
      } finally {
        dispatch('Page/loading', {flag: false, timeout: 300}, {root: true})
      }
    }
  }
}
