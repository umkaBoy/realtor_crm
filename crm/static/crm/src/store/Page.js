import * as pageApi from '@/api/Page'
var counter = 0
var dataPage = null

export default {
  namespaced: true,
  state: {
    isLoading: false,
    data: [],
    isFinished: false
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
        return state.data.map(item => item.complexe).filter((obj, pos, arr) => {
          return arr.map(mapObj => mapObj.id).indexOf(obj.id) === pos
        })
      } catch (err) {
        return []
      }
    }
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
        if (!data.length) state.isFinished = true
        state.data.push(...data)
      }
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
    }
  }
}
