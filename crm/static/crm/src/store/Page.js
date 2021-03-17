import * as pageApi from '@/api/Page'
var counter = 0
var dataPage = null
var flag = false

export default {
  namespaced: true,
  state: {
    isLoading: [],
    data: [],
    isFinished: false,
    main: {},
    filterObj: {}
  },
  getters: {
    isLoading: state => state.isLoading.length,
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
      if (status) {
        state.isLoading.push(true)
      } else {
        state.isLoading.pop()
      }
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
    },
    setFilter (state, data) {
      state.filterObj = data
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
    async load ({ dispatch, commit, state }, {page}) {
      dispatch('Page/loading', {flag: true}, {root: true})
      try {
        if (!flag) flag = true
        else return null
        if (dataPage !== page) {
          dataPage = page
          counter = 0
          commit('setData', [])
          counter++
        }
        const data = await pageApi.loadData(counter, page, state.filterObj)
        counter++
        commit('setData', data)
        flag = false
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
    },
    setFilter ({ dispatch, commit }, data) {
      try {
        commit('setFilter', data)
        let copyPage = dataPage
        dataPage = null
        dispatch('Page/load', {page: copyPage}, {root: true})
      } catch (e) {
        console.log('Не удалось отфильтровать')
      }
    }
  }
}
