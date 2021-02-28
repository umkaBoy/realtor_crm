<template>
  <div style="height: 93vh; overflow: scroll" ref="scroll">
    <v-data-table
      :headers="headers"
      :items="lots"
      hide-default-footer
      disable-pagination
      disable-sort
      fixed-header
      :items-per-page="counter"
      class="elevation-1"
    >
      <template v-slot:item.url_plan="{ item }">
        <fc-image :link="item.url_plan">
        </fc-image>
      </template>
    </v-data-table>
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
import FCImage from './inputs/FCImage'
import MugenScroll from 'vue-mugen-scroll'
import {mapGetters} from 'vuex'

export default {
  name: 'Lots',
  components: {
    'fc-image': FCImage,
    'mugen-scroll': MugenScroll
  },
  data () {
    return {
      loading: false,
      counter: 30,
      headers: [
        {
          text: 'планировка',
          align: 'start',
          value: 'url_plan'
        },
        { text: 'Наименование', value: 'name' },
        { text: 'статус', value: 'status' },
        { text: 'этаж', value: 'floor' },
        { text: 'стоимость', value: 'price' },
        { text: 'площадь', value: 's' }
      ]
    }
  },
  created () {
    this.fetchData()
  },
  computed: {
    ...mapGetters('Page', {lots: 'getData'}),
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
        this.counter = this.lots.length
        this.loading = false
      }, 10)
    }
  }
}
</script>

<style scoped>
</style>
