<template>
  <div style="height: 93vh; overflow: scroll">
    <v-data-table
      :headers="headers"
      :items="complexes"
      hide-default-footer
      hide-default-header
      item-key="id"
      v-model="selected"
      @click:row="selectItems($event.id), selected = [$event]"
      disable-pagination
      disable-sort
      fixed-header
      :items-per-page="complexes.length"
      class="elevation-0"
    >
      <template v-slot:item.name="{ item }">
        <a href="#" @click.prevent="$emit('selectItem', 'complex', item.id)">{{ item.name }}</a>
      </template>
      <template v-slot:item.count_lots_in_sale="{ item }">
        <a href="#" @click.prevent="$emit('selectGroup')" class="float-right">{{ item.count_lots_in_sale }} лотов</a>
      </template>
    </v-data-table>
  </div>
</template>

<script>
import {mapGetters} from 'vuex'

export default {
  name: 'SubComplexes',
  data () {
    return {
      selected: [],
      headers: [
        { text: 'Наименование', value: 'name' },
        { text: 'количество лотов', value: 'count_lots_in_sale' }
      ]
    }
  },
  computed: {
    ...mapGetters('Page', {complexes: 'getSubComp'})
  },
  methods: {
    selectItems (id) {
      const itemsForRemove = document.querySelectorAll('.v-data-table__selected')
      itemsForRemove.forEach(item => {
        item.classList.remove('v-data-table__selected')
      })
      const items = document.querySelectorAll(`.complex-${id}`)
      items.forEach(item => {
        item.closest('tr').classList.add('v-data-table__selected')
      })
    }
  }
}
</script>

<style scoped>
</style>
