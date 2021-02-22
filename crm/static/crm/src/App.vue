<template>
  <v-app id="app">
    <v-progress-linear
      style="z-index: 10000"
      v-if="isLoading"
      :active="isLoading"
      :indeterminate="isLoading"
      fixed
      color="blue accent-4"
    ></v-progress-linear>
    <fc-menu>
    </fc-menu>
    <router-view></router-view>
    <alerts>
    </alerts>
  </v-app>
</template>

<script>
import Menu from '@/components/base/Menu'
import Alert from '@/components/base/Alert'
import {mapGetters} from 'vuex'

export default {
  name: 'App',
  components: {
    'fc-menu': Menu,
    'alerts': Alert
  },
  computed: {
    ...mapGetters('Page', {isLoading: 'isLoading'})
  }
}
</script>

<style>
#app {
  width: 100vw;
  min-height: 100vh;
}
body {
  overflow: hidden; /* Hide scrollbars */
}
body::-webkit-scrollbar {
    display: none;
}
::-webkit-scrollbar-track {border-radius: 4px;}
::-webkit-scrollbar {width: 6px;}
::-webkit-scrollbar-thumb {border-radius: 4px;background: #f0f2f5;}
:hover::-webkit-scrollbar-thumb {background: #6a7d9b;}
</style>
