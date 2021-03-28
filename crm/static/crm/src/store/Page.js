import * as pageApi from '@/api/Page'
var counter = 0
var subCounter = 0
var dataPage = null

export default {
  namespaced: true,
  state: {
    isLoading: [],
    data: [],
    isFinished: false,
    main: {},
    filterObj: {},
    sub: [],
    //  sub
    isSubFinished: false
  },
  getters: {
    isLoading: state => state.isLoading.length,
    getData: state => state.data,
    isFinished: state => state.isFinished,
    isSubFinished: state => state.isSubFinished,
    getMain: state => state.main,
    getSub: state => state.sub
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
    },
    setSub (state, data) {
      if (subCounter === 0) {
        state.sub = data
        state.isSubFinished = false
      } else {
        if (!data.length || data.length < 15) state.isSubFinished = true
        state.sub.push(...data)
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
    async load ({ dispatch, commit, state }, {page}) {
      dispatch('Page/loading', {flag: true}, {root: true})
      try {
        if (dataPage !== page) {
          dataPage = page
          counter = 0
          commit('setData', [])
          counter++
        }
        const data = await pageApi.loadData(counter, page, state.filterObj)
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
    },
    async subload ({ dispatch, commit, state }, {page}) {
      dispatch('Page/loading', {flag: true}, {root: true})
      try {
        if (dataPage !== page) {
          subCounter = 0
          commit('setSub', [])
          subCounter++
        }
        if (page === 'complexes') {
          page = 'developers'
        } else if (page === 'lots') {
          page = 'complexes'
        }
        const data = await pageApi.loadData(subCounter, page)
        subCounter++
        commit('setSub', data)
      } catch (e) {
        dispatch('Alert/add', { type: 'error', text: 'Не удалось загрузить список объектов', timeout: 5000 }, { root: true })
      } finally {
        dispatch('Page/loading', {flag: false, timeout: 300}, {root: true})
      }
    }
  }
}
