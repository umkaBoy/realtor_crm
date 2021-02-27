<template>
  <div>
    <v-virtual-scroll
    bench="50"
    :items="complexes"
    height="92vh"
    width="auto"
    item-height="64"
    >
<!--          -->
    <template v-slot:default="{ item, index }">
      <v-list-item :key="item.id">
        <v-list-item-content>
          <v-list-item-title>
            <a href="#" @click.prevent="$emit('selectItem',index)"><strong>{{ item.name }}</strong></a>
            <a href="#" @click.prevent="$emit('selectGroup', index)" class="float-right">{{ index }} лотов</a>
          </v-list-item-title>
        </v-list-item-content>
      </v-list-item>
      <v-divider></v-divider>
    </template>
  <!--          -->
    </v-virtual-scroll>
<!--    <v-btn-->
<!--      style="bottom: 10px"-->
<!--      color="white"-->
<!--      elevation="0"-->
<!--      small-->
<!--      fab-->
<!--      absolute-->
<!--      bottom-->
<!--      left-->
<!--      :href="$route.name === 'lots' ? '/admin/crm/complex/add/' : '/admin/crm/developer/add/'"-->
<!--    >-->
<!--      <v-icon color="green">{{ icons.mdiPlusBoxOutline }}</v-icon>-->
<!--    </v-btn>-->
  </div>
</template>

<script>

import {mapGetters} from 'vuex'

export default {
  name: 'SubComplexes',
  computed: {
    ...mapGetters('Page', {complexes: 'getSubComp'})
  }
}
</script>

<style scoped>
</style>
