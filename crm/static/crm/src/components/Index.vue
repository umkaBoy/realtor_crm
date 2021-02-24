<template>
  <v-container style="margin-left: 61px">
    <v-row style="height: 93vh; width: 96vw">
      <v-col
        cols="12"
        sm="12"
        md="12">
        <fc-header></fc-header>
      </v-col>
      <v-navigation-drawer ref="drawer" left stateless :width="navigation.width" v-model="navigation.shown">
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
            <v-list-item-content>
              <v-list-item-title>
                <a href="#">ЖК <strong>№{{ index }}</strong></a>
                <a href="#" class="float-right">10 лотов</a>
              </v-list-item-title>
            </v-list-item-content>
          </v-list-item>

          <v-divider></v-divider>
        </template>
<!--          -->
        </v-virtual-scroll>
       </v-navigation-drawer>
       <v-navigation-drawer stateless>
          <lots></lots>
       </v-navigation-drawer>
    </v-row>
  </v-container>
</template>

<script>
import Header from './base/Header'
// import {mapGetters} from 'vuex'
import Lots from './Lots'

export default {
  name: 'Index',
  components: {
    'fc-header': Header,
    'lots': Lots
  },
  data () {
    return {
      complexes: Array(10).fill(Math.floor(Math.random() * Math.floor(10000))),
      navigation: {
        width: '20vw',
        borderSize: 3,
        shown: true
      }
    }
  },
  mounted () {
    this.setBorderWidth()
    this.setEvents()
  },
  methods: {
    setBorderWidth () {
      let i = this.$refs.drawer.$el.querySelector(
        '.v-navigation-drawer__border'
      )
      i.style.width = this.navigation.borderSize + 'px'
      i.style.cursor = 'ew-resize'
      i.style.backgroundColor = 'lightgrey'
    },
    setEvents () {
      const minSize = this.navigation.borderSize
      const el = this.$refs.drawer.$el
      const drawerBorder = el.querySelector('.v-navigation-drawer__border')
      const direction = el.classList.contains('v-navigation-drawer--right')
        ? 'right'
        : 'left'

      function resize (e) {
        document.body.style.cursor = 'ew-resize'
        let f =
          direction === 'right'
            ? document.body.scrollWidth - e.clientX
            : e.clientX
        el.style.width = (f - 61) + 'px'
      }

      drawerBorder.addEventListener(
        'mousedown',
        (e) => {
          el.classList.add('unselectable')
          if (e.offsetX < minSize) {
            el.style.transition = 'initial'
            document.addEventListener('mousemove', resize, false)
          }
        },
        false
      )

      document.addEventListener(
        'mouseup',
        () => {
          el.classList.remove('unselectable')
          el.style.transition = ''
          this.navigation.width = el.style.width
          document.body.style.cursor = ''
          document.removeEventListener('mousemove', resize, false)
        },
        false
      )
    }
  }
  // computed: {
  //   ...mapGetters('Page', {data: 'getData'})
  // },
}
</script>

<style scoped>
.col,
.col-12 {
  padding-top: 8px;
}
.unselectable {
  -webkit-touch-callout: none; /* iOS Safari */
  -webkit-user-select: none;   /* Chrome/Safari/Opera */
  -khtml-user-select: none;    /* Konqueror */
  -moz-user-select: none;      /* Firefox */
  -ms-user-select: none;       /* Internet Explorer/Edge */
  user-select: none;           /* Non-prefixed version, currently
                                  not supported by any browser */
}
</style>
