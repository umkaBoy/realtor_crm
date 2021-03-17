<template>
  <div style="height: 93vh; overflow: scroll">
    <v-row v-if="lot">
      <v-col
        :md="7"
        sm="12"
        cols="12">
        <v-card
          min-height="70"
          class="pa-1"
        >
          <h3> {{ lot.__str__ }} </h3>
          <br>
          <span class="grey--text float-right" v-if="lot.complex && lot.complex.developer"><strong> {{ lot.complex.developer.name }} </strong></span>
          <p>
            <span class="primary--text" v-if="lot.complex"><strong> {{ lot.complex.near_metro }}, </strong> {{ lot.complex.address }} </span><br>
            <span class="primary--text"><strong> {{ lot.lease }} </strong></span>
          </p>
        </v-card>
        <v-card color="transparent">
          <v-expansion-panels multiple>
          </v-expansion-panels>
        </v-card>
      </v-col>
      <v-col
        md="5"
        sm="12"
        cols="12">
        <v-card
          class="pa-1"
          outlined
          color="transparent"
          v-if="images && images.length"
        >
          <v-carousel
            :show-arrows="images.length > 1"
            hide-delimiters
            v-model="img"
            :next-icon="icons.mdiMenuRight"
            :prev-icon="icons.mdiMenuLeft"
            :delimiter-icon="icons.mdiCircleOutline"
            cycle
            show-arrows-on-hover
            height="300">
            <v-carousel-item
              v-for="(image) in images"
              :key="image.id"
              :src="image.get_url"
            >
            </v-carousel-item>
          </v-carousel>
        </v-card>
        <v-card
          color="transparent"
          class="pa-1"
          outlined
          v-if="lot.links && lot.links.length"
        >
          <v-chip
            class="ma-2"
            color="primary"
            outlined
            v-for="(link, i) in lot.links"
            :key="i"
            :href="link.link"
            target="_blank"
          >
            {{ link.name }}
          </v-chip>
        </v-card>
        <v-expansion-panels multiple>
          <v-expansion-panel v-if="lot.contacts && lot.contacts.length" style="background-color: transparent !important;">
            <v-expansion-panel-header :expand-icon="icons.mdiChevronDown">
              <h5 class="primary--text text-right">Контакты</h5>
            </v-expansion-panel-header>
            <v-expansion-panel-content>
              <v-card
                color="transparent"
                class="pa-1"
                outlined
                :key="contact.id"
                v-for="(contact) in lot.contacts"
                v-if="lot.contacts && lot.contacts.length"
              >
                <h5 class="primary--text">{{contact.name}}</h5>
                <a :href="`tel:${contact.phone}`" v-if="contact.phone">{{contact.phone}}<br></a>
                <a :href="`mailto:${contact.email}`" v-if="contact.email">{{contact.email}}</a>
                <p class="grey--text" v-if="contact.note">{{contact.note}}</p>
              </v-card>
            </v-expansion-panel-content>
          </v-expansion-panel>
          <v-expansion-panel v-if="lot.files && lot.files.length" style="background-color: transparent !important;">
            <v-expansion-panel-header :expand-icon="icons.mdiChevronDown">
              <h5 class="primary--text text-right">Презентации и документы</h5>
            </v-expansion-panel-header>
            <v-expansion-panel-content>
              <v-card
                color="transparent"
                class="pa-1"
                outlined
                v-for="(type, i) in new Set(lot.files.map(obj => obj.type))"
                :key="i"
              >
                <h4 class="primary--text">{{ type }}</h4>
                <v-card
                  color="transparent"
                  class="pa-1"
                  outlined
                  v-for="(file, index) in lot.files.filter(obj => obj.type === type)"
                  :key="index"
                >
                  <h5 v-if="file.name">{{ file.name }}</h5>
                  <a :href="file.get_url">
                    <span>{{file.filename}}</span>
                  </a>
                  <p class="grey--text">
                    <span>{{ file.get_created_at }}</span> | <span>{{file.get_size}}</span>
                  </p>
                </v-card>
              </v-card>
            </v-expansion-panel-content>
          </v-expansion-panel>
        </v-expansion-panels>
      </v-col>
    </v-row>
  </div>
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
  name: 'MainLot',
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
    ...mapGetters('Page', {lot: 'getMain'}),
    images () {
      if (this.lot && this.lot.images) {
        let arr = [{get_url: this.lot.url_plan, id: 0}].concat(this.lot.images).concat(this.lot.complex.images)
        return arr
      }
      return []
    }
  },
  methods: {
    humanized_sum (sum) {
      return parseInt(sum).toLocaleString()
    }
  }
}
</script>

<style scoped>
.v-sheet {
  box-shadow: none;
}
</style>
