<template>
  <div style="height: 93vh; overflow: scroll" ref="scroll">
    <v-data-table
      :headers="headers"
      :items="complexes"
      hide-default-footer
      @click:row="$emit('selectItem', 'complex', $event.id, [!1, !0, !0])"
      disable-pagination
      disable-sort
      fixed-header
      :items-per-page="counter"
      class="elevation-1"
    ></v-data-table>
    <div>
      <mugen-scroll
        :handler="fetchData"
        :should-handle="!loading"
        scrollContainer="scroll"
        v-if="!isFinished"
        class="text-center">
        Загрузка...
      </mugen-scroll>
    </div>
  </div>
</template>

<script>
import MugenScroll from 'vue-mugen-scroll'
import {mapGetters} from 'vuex'

export default {
  name: 'Complexes',
  components: {
    'mugen-scroll': MugenScroll
  },
  data () {
    return {
      loading: false,
      counter: 30,
      headers: [
        { text: 'id', value: 'id' },
        { text: 'Имя', value: 'name' },
        { text: 'Адрес', value: 'address' },
        { text: 'Сдача', value: 'end_of_construction' }
      ]
    }
  },
  created () {
    this.fetchData()
  },
  computed: {
    ...mapGetters('Page', {complexes: 'getData'}),
    ...mapGetters('Page', {isFinished: 'isFinished'})
  },
  methods: {
    fetchData () {
      this.loading = true
      this.$store.dispatch('Page/load', {
        page: this.$route.name
      }, {
        root: true
      })
      setTimeout(() => {
        this.counter = this.complexes.length
        this.loading = false
      }, 10)
    }
  }
}
</script>

<style scoped>
</style>
