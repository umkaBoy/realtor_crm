<template>
  <div class="box">
    <transition-group name="item" tag="div">
      <v-alert
        :icon="icons[alert.type]"
        transition="scroll-x-transition"
        v-for="alert in alerts"
        :key="alert.id"
        class="item"
        outlined
        prominent
        style="background-color: white !important"
        border="right"
        :type="alert.type"
      >
      {{ alert.text }}
      </v-alert>
    </transition-group>
  </div>
</template>

<script>
import { mapGetters } from 'vuex'
import {
  mdiAlertCircleOutline,
  mdiAlertOctagon,
  mdiAlert
} from '@mdi/js'

export default {
  name: 'Alert',
  data () {
    return {
      icons: {
        info: mdiAlertCircleOutline,
        error: mdiAlertOctagon,
        warning: mdiAlert
      }
    }
  },
  computed: {
    ...mapGetters('Alert', {alerts: 'all'})
  }
}
</script>

<style scoped>
  .box {
    text-align: center;
    font-weight: bold;
    position: fixed;
    top: 0;
    right: 0;
    width: 300px;
    z-index: 10000;
    padding: 10px 10px 0 0;
  }
  .item-enter {
    opacity: 0;
  }

  .item-enter-active {
    transition: opacity 1s;
    opacity: 1;
  }
</style>
