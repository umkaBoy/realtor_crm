<template>
  <div>
    <v-virtual-scroll
      ref="scroll"
      bench="50"
      :items="complexes"
      height="92vh"
      width="auto"
      item-height="64"
    >
<!--          -->
      <template v-slot:default="{ item, index }">
      <v-list-item :key="item.id">

        <v-list-item-content>
          <v-row>
            <v-col
              cols="12"
              sm="12"
              md="4">
              <strong> {{ item.name }}</strong>
            </v-col>
            <v-col
              cols="12"
              sm="12"
              md="4">
              <strong> {{ item.end_of_construction }}</strong>
            </v-col>
            <v-col
              cols="12"
              sm="12"
              md="4">
              <strong> {{ item.count_floors }}</strong>
            </v-col>
          </v-row>
        </v-list-item-content>
      </v-list-item>
      <v-divider></v-divider>
      <mugen-scroll
        :handler="fetchData"
        :should-handle="!loading"
        scrollContainer="scroll"
        v-if="index === complexes.length - 1 && !isFinished"
        class="text-center">
        Загрузка...
      </mugen-scroll>
    </template>
<!--          -->
    </v-virtual-scroll>
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
      loading: false
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
        this.loading = false
      }, 100)
    }
  }
}
</script>

<style scoped>
</style>
