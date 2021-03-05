import * as pageApi from '@/api/Page'
var counter = 0
var dataPage = null

export default {
  namespaced: true,
  state: {
    isLoading: false,
    data: [],
    isFinished: false,
    main: {}
  },
  getters: {
    isLoading: state => state.isLoading,
    getData: state => state.data,
    isFinished: state => state.isFinished,
    getSubDev: (state) => {
      try {
        return state.data.map(item => item.developer).filter((obj, pos, arr) => {
          return arr.map(mapObj => mapObj.id).indexOf(obj.id) === pos
        })
      } catch (err) {
        return []
      }
    },
    getSubComp: (state) => {
      try {
        return state.data.map(item => item.complex).filter((obj, pos, arr) => {
          return arr.map(mapObj => mapObj.id).indexOf(obj.id) === pos
        })
      } catch (err) {
        return []
      }
    },
    getMain: state => state.main
  },
  mutations: {
    setLoader (state, status) {
      state.isLoading = status
    },
    setData (state, data) {
      if (counter === 0) {
        state.data = data
        state.isFinished = false
      } else {
        if (!data.length || data.length < 15) state.isFinished = true
        state.data.push(...data)
      }
    },
    setMain (state, data) {
      state.main = data
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
    async load ({ dispatch, commit }, {page}) {
      dispatch('Page/loading', {flag: true}, {root: true})
      try {
        if (dataPage !== page) {
          dataPage = page
          counter = 0
          commit('setData', [])
          counter++
        }
        const data = await pageApi.loadData(counter, page)
        counter++
        commit('setData', data)
      } catch (e) {
        dispatch('Alert/add', { type: 'error', text: 'Не удалось загрузить список объектов', timeout: 5000 }, { root: true })
      } finally {
        dispatch('Page/loading', {flag: false, timeout: 300}, {root: true})
      }
    },
    async loadMain ({ dispatch, commit }, {id, type}) {
      dispatch('Page/loading', {flag: true}, {root: true})
      try {
        const data = await pageApi.loadMainObject(id, type)
        commit('setMain', data)
      } catch (e) {
        dispatch('Alert/add', { type: 'error', text: 'Не удалось загрузить данный объект', timeout: 5000 }, { root: true })
      } finally {
        dispatch('Page/loading', {flag: false, timeout: 300}, {root: true})
      }
    }
  }
}
