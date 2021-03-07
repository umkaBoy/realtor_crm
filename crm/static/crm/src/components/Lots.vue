<template>
  <div style="height: 93vh; overflow: scroll" ref="scroll">
    <v-data-table
      :headers="headers"
      :items="lots"
      item-key="id"
      @click:row="clearSelect(), selected = [$event], $emit('selectItem', $event.type_building, $event.id, [!1, !0, !0])"
      hide-default-footer
      v-model="selected"
      disable-pagination
      disable-sort
      fixed-header
      :items-per-page="counter"
      class="elevation-1"
    >
      <template v-slot:item.url_plan="{ item }">
        <div :class="'complex-' + item.complex.id">
          <fc-image :link="item.url_plan">
          </fc-image>
        </div>
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
      selected: [],
      loading: false,
      counter: 30,
      headers: [
        {
          text: 'планировка',
          align: 'start',
          value: 'url_plan'
        },
        { text: 'Наименование', value: '__str__' },
        { text: 'Статус', value: 'status' },
        { text: 'Этаж', value: 'floor' },
        { text: 'Стоимость', value: 'price' },
        { text: 'Площадь', value: 's' }
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
    clearSelect () {
      const itemsForRemove = document.querySelectorAll('.v-data-table__selected')
      itemsForRemove.forEach(item => {
        item.classList.remove('v-data-table__selected')
      })
    },
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
