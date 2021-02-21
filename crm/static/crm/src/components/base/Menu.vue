<template>
  <v-navigation-drawer
    permanent
    expand-on-hover
    color="secondary"
  >
    <v-list>
      <v-list-item class="px-2">
        <v-list-item-avatar>
          <v-img src="https://png.pngtree.com/template/20191014/ourmid/pngtree-home-or-house-roof-logo-design-template-with-water-wave-image_317799.jpg"></v-img>
        </v-list-item-avatar>
      </v-list-item>
      <v-list-item link>
        <v-list-item-content>
          <v-list-item-title class="title">
            {{ username || '¯\\_(ツ)_/¯' }}
          </v-list-item-title>
          <v-list-item-subtitle>{{ user.email }}</v-list-item-subtitle>
        </v-list-item-content>
      </v-list-item>
    </v-list>
    <v-divider></v-divider>
    <template v-slot:append>
      <div class="pa-2">
        <v-list
          nav
          dense>
          <v-list-item link href="/admin" v-if="user && user.is_superuser">
            <v-list-item-icon>
              <v-icon>{{ icons.mdiCogs }}</v-icon>
            </v-list-item-icon>
            <v-list-item-title>Админ-панель</v-list-item-title>
          </v-list-item>
          <v-list-item link href="/logout">
            <v-list-item-icon>
              <v-icon>{{ icons.mdiLogoutVariant }}</v-icon>
            </v-list-item-icon>
            <v-list-item-title>Выход</v-list-item-title>
          </v-list-item>
        </v-list>
      </div>
    </template>
  </v-navigation-drawer>
</template>

<script>
import {mapGetters} from 'vuex'
import {
  mdiLogoutVariant,
  mdiCogs
} from '@mdi/js'

export default {
  name: 'Menu',
  data () {
    return {
      icons: {
        mdiLogoutVariant,
        mdiCogs
      }
    }
  },
  computed: {
    ...mapGetters('User', {user: 'user'}),
    ...mapGetters('User', {username: 'getFullName'})
  }
}
</script>

<style scoped>
.v-navigation-drawer {
  position: fixed;
  height: 100vh;
  min-width: 65px !important;
}

</style>
