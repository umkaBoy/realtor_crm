<template>
  <div>
    <v-virtual-scroll
      ref="scroll"
      bench="50"
      :items="lots"
      height="92vh"
      width="auto"
      item-height="64"
    >
<!--          -->
      <template v-slot:default="{ item, index }">
      <v-list-item :key="item">
        <v-list-item-action>
          <fc-image :link="'https://picsum.photos/200/300'"></fc-image>
        </v-list-item-action>

        <v-list-item-content>
          <v-list-item-title>
            Лот <strong>ID {{ item }}</strong>
          </v-list-item-title>
        </v-list-item-content>
      </v-list-item>
      <v-divider></v-divider>
      <mugen-scroll
        :handler="fetchData"
        :should-handle="!loading"
        scrollContainer="scroll"
        v-if="index === lots.length - 1">
        Загрузка...
      </mugen-scroll>
    </template>
<!--          -->
    </v-virtual-scroll>
  </div>
</template>

<script>
import FCImage from './inputs/FCImage'
import MugenScroll from 'vue-mugen-scroll'

export default {
  name: 'Lots',
  components: {
    'fc-image': FCImage,
    'mugen-scroll': MugenScroll
  },
  data () {
    return {
      loading: false,
      lots: Array(10).fill(Math.floor(Math.random() * Math.floor(10000)))
    }
  },
  methods: {
    fetchData () {
      this.loading = true
      this.lots = this.lots.concat(Array(10).fill(Math.floor(Math.random() * Math.floor(10000))))
      // ... the code you wanna run to fetch data
      setTimeout(() => {
        this.loading = false
      }, 500)
    }
  }
}
</script>

<style scoped>
</style>
