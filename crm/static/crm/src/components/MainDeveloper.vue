<template>
  <v-container style="height: 93vh; overflow: scroll">
    <v-row>
      <v-col
        :md="7"
        sm="12"
        cols="12">
        <v-card
          class="pa-2"
        >
          <h3>Застройщик {{ developer.name }}</h3>
          <span class="grey--text">Дата основания: {{ developer.created_at }}</span>
        </v-card>
        <v-spacer></v-spacer>
        <v-card
          v-if="percentage_objects_under_construction"
          class="pa-2"
        >
          <span>
            <v-progress-circular
              :rotate="180"
              :size="70"
              :width="10"
              :value="percentage_objects_under_construction"
              color="primary"
            >
              <span class="black--text">{{ developer.objects_under_construction }}</span>
            </v-progress-circular>
            <p class="grey--text circular-label">
              На стадии строительства
            </p>
          </span>
          <span class="float-right">
            <v-progress-circular
              :rotate="180"
              :size="70"
              :width="10"
              :value="100 - percentage_objects_under_construction"
              color="blue"
            >
              <span class="black--text">{{ developer.objects_delivered }}</span>
            </v-progress-circular>
            <p class="grey--text circular-label">
               Построено объектов
            </p>
          </span>
        </v-card>
        <v-card>
          <v-expansion-panels>
            <v-expansion-panel v-if="developer.description">
              <v-expansion-panel-header :expand-icon="icons.mdiChevronDown">
                <h5 class="primary--text">Информация о застройщике</h5>
              </v-expansion-panel-header>
              <v-expansion-panel-content>
                <p>{{ developer.description }}</p>
              </v-expansion-panel-content>
            </v-expansion-panel>
          </v-expansion-panels>
        </v-card>
      </v-col>
      <v-col
        md="5"
        sm="12"
        cols="12">
        <v-card
          class="pa-2"
          outlined
          color="transparent"
          v-if="developer.images && developer.images.length"
        >
          <v-carousel
            :show-arrows="developer.images.length > 1"
            hide-delimiters
            v-model="img"
            :next-icon="icons.mdiMenuRight"
            :prev-icon="icons.mdiMenuLeft"
            :delimiter-icon="icons.mdiCircleOutline"
            cycle
            show-arrows-on-hover
            height="300">
            <v-carousel-item
              v-for="(image, i) in developer.images"
              :key="image.id"
              :src="image.get_url"
            >
            </v-carousel-item>
          </v-carousel>
        </v-card>
        <v-card
          color="transparent"
          class="pa-2"
          outlined
          :key="contact.id"
          v-for="(contact, i) in developer.contacts"
          v-if="developer.contacts && developer.contacts.length"
        >
          <h5 class="primary--text">{{contact.name}}</h5>
          <a :href="`tel:${contact.phone}`" class="grey--text" v-if="contact.phone">{{contact.phone}}<br></a>
          <a :href="`mailto:${contact.email}`" class="grey--text" v-if="contact.email">{{contact.email}}</a>
          <p v-if="contact.note">{{contact.note}}</p>
        </v-card>
      </v-col>
    </v-row>
  </v-container>
</template>

<script>
import {mapGetters} from 'vuex'
import {
  mdiMenuLeft,
  mdiMenuRight,
  mdiCircleOutline,
  mdiChevronDown
} from '@mdi/js'

export default {
  name: 'MainDeveloper',
  data () {
    return {
      img: 0,
      icons: {
        mdiMenuLeft,
        mdiMenuRight,
        mdiCircleOutline,
        mdiChevronDown
      }
    }
  },
  computed: {
    ...mapGetters('Page', {developer: 'getMain'}),
    percentage_objects_under_construction () {
      if (this.developer.objects_under_construction !== undefined) {
        const sum = this.developer.objects_under_construction + this.developer.objects_delivered
        return this.developer.objects_under_construction / sum * 100
      } else {
        return 0
      }
    }
  }
}
</script>

<style scoped>
.circular-label {
  width: 110px;
  display: inline-block;
  position: relative;
  top: 10px;
}
.v-sheet {
  box-shadow: none;
}
</style>
