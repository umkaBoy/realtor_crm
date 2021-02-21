let messageAI = 0

export default {
  namespaced: true,
  state: {
    messages: []
  },
  getters: {
    all: state => state.messages
  },
  mutations: {
    add (state, message) {
      state.messages.push(message)
    },
    remove (state, id) {
      state.messages = state.messages.filter(msg => msg.id !== id)
    }
  },
  actions: {
    add ({ commit }, { type, text, timeout = null }) {
      let id = ++messageAI
      commit('add', { type, text, id })

      if (timeout) {
        setTimeout(() => {
          commit('remove', id)
        }, timeout)
      }
    }
  }
}
