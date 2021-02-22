<template>
  <v-container style="margin-left: 61px">
    <v-row style="height: 92vh; width: 96vw">
      <v-col
        cols="12"
        sm="12"
        md="12">
        <fc-header></fc-header>
      </v-col>
      <v-col
        cols="12"
        sm="3"
        md="3">
        <v-virtual-scroll
          bench="50"
          :items="complexes"
          height="92vh"
          width="auto"
          item-height="64"
        >
<!--          -->
          <template v-slot:default="{ item, index }">
          <v-list-item :key="item">
            <v-list-item-action>
              <v-btn
                fab
                small
                depressed
                color="primary"
              >
                {{ index }}
              </v-btn>
            </v-list-item-action>

            <v-list-item-content>
              <v-list-item-title>
                ЖК <strong>ID {{ item }}</strong>
              </v-list-item-title>
            </v-list-item-content>
          </v-list-item>

          <v-divider></v-divider>
        </template>
<!--          -->
        </v-virtual-scroll>
      </v-col>
      <v-col
        col="12"
        sm="9"
        md="9">
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
              <v-btn
                fab
                small
                depressed
                color="transparent"
              >
                <v-tooltip right>
                  <template v-slot:activator="{ on, attrs }">
                    <v-img :src="'https://picsum.photos/200/300'" width="40" height="40" v-on="on">
                      <template v-slot:placeholder>
                        <v-row
                          class="fill-height ma-0"
                          align="center"
                          justify="center"
                        >
                          <v-progress-circular
                            indeterminate
                            color="grey lighten-5"
                          ></v-progress-circular>
                        </v-row>
                      </template>
                    </v-img>
                  </template>
                  <v-img :src="'https://picsum.photos/200/300'" width="250" height="auto">
                    <template v-slot:placeholder>
                      <v-row
                        class="fill-height ma-0"
                        align="center"
                        justify="center"
                      >
                        <v-progress-circular
                          indeterminate
                          color="grey lighten-5"
                        ></v-progress-circular>
                      </v-row>
                    </template>
                  </v-img>
                </v-tooltip>
              </v-btn>
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
      </v-col>
    </v-row>
  </v-container>
</template>

<script>
import Header from './base/Header'
// import {mapGetters} from 'vuex'
import MugenScroll from 'vue-mugen-scroll'

export default {
  name: 'Index',
  components: {
    'fc-header': Header,
    'mugen-scroll': MugenScroll
  },
  data () {
    return {
      loading: false,
      lots: Array(10).fill(Math.floor(Math.random() * Math.floor(10000))),
      complexes: Array(10).fill(Math.floor(Math.random() * Math.floor(10000)))
    }
  },
  // computed: {
  //   ...mapGetters('Page', {data: 'getData'})
  // },
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
.col,
.col-12 {
  padding-top: 8px;
}
img {
  object-fit: cover;
}
</style>
