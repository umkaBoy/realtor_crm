<template>
  <div style="height: 93vh; overflow: scroll">
    <v-data-table
      :headers="headers"
      :items="developers"
      hide-default-footer
      hide-default-header
      disable-pagination
      disable-sort
      fixed-header
      :items-per-page="developers.length"
      class="elevation-1"
    >
      <template v-slot:item.name="{ item }">
        <a href="#" @click.prevent="$emit('selectItem', item.id)"><strong>{{ item.name }}</strong></a>
      </template>
      <template v-slot:item.count_complexes="{ item }">
        <a href="#" @click.prevent="$emit('selectGroup', item.id)" class="float-right">{{ item.count_complexes}} жк</a>
      </template>
    </v-data-table>
  </div>
</template>

<script>
import {mapGetters} from 'vuex'

export default {
  name: 'SubDevelopers',
  data () {
    return {
      headers: [
        { text: 'Наименование', value: 'name' },
        { text: 'количество жк', value: 'count_complexes' }
      ]
    }
  },
  computed: {
    ...mapGetters('Page', {developers: 'getSubDev'})
  }
}
</script>

<style scoped>
</style>
