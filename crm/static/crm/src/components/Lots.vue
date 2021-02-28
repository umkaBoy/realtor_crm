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
      <v-list-item :key="item.id">
        <v-list-item-action>
          <fc-image :link="item.url_plan"></fc-image>
        </v-list-item-action>

        <v-list-item-content>
          <v-row>
            <v-col
              cols="12"
              sm="12"
              md="4">
              <strong> {{ item.name }}</strong>
            </v-col>
          </v-row>
        </v-list-item-content>
      </v-list-item>
      <v-divider></v-divider>
      <mugen-scroll
        :handler="fetchData"
        :should-handle="!loading"
        scrollContainer="scroll"
        v-if="index === lots.length - 1 && !isFinished"
        class="text-center">
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
import {mapGetters} from 'vuex'

export default {
  name: 'Lots',
  components: {
    'fc-image': FCImage,
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
        this.loading = false
      }, 100)
    }
  }
}
</script>

<style scoped>
</style>
