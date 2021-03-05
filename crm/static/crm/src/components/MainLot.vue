<template>
  <v-container>
    Лот {{ lot.id }}
  </v-container>
</template>

<script>
import {mapGetters} from 'vuex'

export default {
  name: 'MainLot',
  computed: {
    ...mapGetters('Page', {lot: 'getMain'})
  }
}
</script>

<style scoped>

</style>
