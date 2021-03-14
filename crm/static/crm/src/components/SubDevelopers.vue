<template>
  <div style="height: 93vh; overflow: scroll">
    <v-data-table
      :headers="headers"
      :items="developers"
      hide-default-footer
      hide-default-header
      item-key="id"
      disable-pagination
      disable-sort
      @click:row="selectItems($event.id), selected = [$event]"
      fixed-header
      v-model="selected"
      :items-per-page="developers.length"
      class="elevation-0"
    >
      <template v-slot:item.name="{ item }">
        <a href="#" @click.prevent="$emit('selectItem', 'developer', item.id)">{{ item.name }}</a>
      </template>
      <template v-slot:item.count_complexes="{ item }">
        <a href="#" @click.prevent="$emit('selectGroup')" class="float-right">{{ item.count_complexes}} жк</a>
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
      selected: [],
      headers: [
        { text: 'Наименование', value: 'name' },
        { text: 'количество жк', value: 'count_complexes' }
      ]
    }
  },
  computed: {
    ...mapGetters('Page', {developers: 'getSubDev'})
  },
  methods: {
    selectItems (id) {
      const itemsForRemove = document.querySelectorAll('.v-data-table__selected')
      itemsForRemove.forEach(item => {
        item.classList.remove('v-data-table__selected')
      })
      const items = document.querySelectorAll(`.developer-${id}`)
      items.forEach(item => {
        item.closest('tr').classList.add('v-data-table__selected')
      })
      items[0].scrollIntoView()
    }
  }
}
</script>

<style scoped>
</style>
