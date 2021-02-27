<template>
  <v-container style="margin-left: 61px">
    <v-row>
      <v-col
        cols="12"
        sm="12"
        md="12">
        <fc-header></fc-header>
      </v-col>
    </v-row>
    <v-row class="fill-height" style="width: 96vw" >
<!--    контент-->
      <v-col
        cols="12"
        sm="12"
        md="12">
        <div class="outer">
          <div class="block block-1" ref="block1" v-show="navigation.shown">
            <router-view @selectItem="onSelectSubItem" @selectGroup="onSelectGroup" name="sub"></router-view>
          </div>
        <div class="slider" ref="slider1" v-show="navigation.shown">
        </div>
        <div class="block block-2" ref="block2" v-show="navigationC.shown">
          <router-view name="main"></router-view>
        </div>
        <div class="slider" ref="slider2" v-show="!navigation.shown && navigationR.shown">
        </div>
        <div class="block block-2" ref="block3" v-show="navigationR.shown">
          информация по объекту
        </div>
  <!--      Конеч контента-->
        </div>
      </v-col>
    </v-row>
  </v-container>
</template>

<script>
import Header from './base/Header'
import { mdiPlusBoxOutline } from '@mdi/js'

export default {
  name: 'Index',
  components: {
    'fc-header': Header
  },
  data () {
    return {
      icons: {
        mdiPlusBoxOutline
      },
      dataL: Array(10).fill(Math.floor(Math.random() * Math.floor(10000))),
      navigation: {
        shown: true
      },
      navigationC: {
        hasToggled: false,
        shown: true
      },
      navigationR: {
        shown: false
      }
    }
  },
  beforeRouteUpdate (to, from, next) {
    this.setBlocksVisibility()
    next()
  },
  mounted () {
    this.setEvents()
  },
  methods: {
    toggleCLassOnBlock () {
      let block = this.$refs.block2
      block.classList.toggle('block-2')
      block.classList.toggle('block-1')
    },
    setBlocksVisibility (b1 = true, b2 = true, b3 = false) {
      this.navigation.shown = b1
      this.navigationR.shown = b3
      this.navigationC.shown = b2
      if (this.navigationC.hasToggled && !b3) {
        this.toggleCLassOnBlock()
        this.navigationC.hasToggled = false
        this.setEvents()
      } else if (!this.navigationC.hasToggled && b3) {
        this.toggleCLassOnBlock()
        const block = this.$refs.block2
        const slide = this.$refs.slider2
        this.navigationC.hasToggled = true
        this.setEvents(block, slide)
      }
    },
    setEvents (el = null, slide = null) {
      let block = el || this.$refs.block1
      let slider = slide || this.$refs.slider1

      slider.onmousedown = function dragMouseDown (e) {
        let dragX = e.clientX
        document.onmousemove = function onMouseMove (e) {
          block.style.width = block.offsetWidth + e.clientX - dragX + 'px'
          dragX = e.clientX
        }
        // remove mouse-move listener on mouse-up
        document.onmouseup = () => {
          document.onmousemove = document.onmouseup = null
        }
      }
    },
    onSelectGroup (id = null) {
      this.setBlocksVisibility()
    },
    onSelectSubItem (id = null) {
      this.setBlocksVisibility(true, false, true)
    }
  }
}
</script>

<style>
.outer {
  display: flex;
  height: 100%;
  flex-direction: row;
}

.block {
  height: 100%;
}

.block-1 {
  width: 30%;
}

.block-2 {
  flex: 1; /* adjust automatically */
  min-width: 0; /* allow flexing beyond auto width */
  overflow: hidden; /* hide overflow on small width */
}

.slider {
  line-height: 100%;
  width: 5px;
  background-color: #c2c2c2;
  border: none;
  cursor: col-resize;
  user-select: none; /* disable selection */
  text-align: center;
}
.v-virtual-scroll__item:hover {
  background-color: #fbffe7;
}
</style>
