<template>
  <v-container>
    Комплекс {{ complex.id }}
  </v-container>
</template>

<script>
import {mapGetters} from 'vuex'

export default {
  name: 'MainComplex',
  computed: {
    ...mapGetters('Page', {complex: 'getMain'})
  }
}
</script>

<style scoped>
</style>
