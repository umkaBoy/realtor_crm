<template>
  <v-container style="height: 93vh; overflow: scroll">
    <v-row v-if="complex.name">
      <v-col
        :md="7"
        sm="12"
        cols="12">
        <v-card
          min-height="70"
          class="pa-2"
        >
          <h3>{{ complex.name }}</h3>
          <span class="grey--text float-right">Застройщик {{ complex.developer.name }}</span>
          <span class="grey--text"><strong>{{ complex.region.name }}</strong> {{ complex.address }}</span>
        </v-card>
        <v-card color="transparent">
          <v-expansion-panels multiple>
            <v-expansion-panel v-if="complex.description">
              <v-expansion-panel-header :expand-icon="icons.mdiChevronDown">
                <h5 class="primary--text">Описание</h5>
              </v-expansion-panel-header>
              <v-expansion-panel-content>
                <p>{{ complex.description }}</p>
              </v-expansion-panel-content>
            </v-expansion-panel>
            <v-expansion-panel>
              <v-expansion-panel-header :expand-icon="icons.mdiChevronDown">
                <h5 class="primary--text">Сведения о ЖК</h5>
              </v-expansion-panel-header>
              <v-expansion-panel-content>
                <v-simple-table>
                <template v-slot:default>
                  <tbody>
                    <tr v-if="complex.premises_type">
                      <td>Вид объекта</td>
                      <td>{{ complex.premises_type.name }}</td>
                    </tr>
                    <tr v-if="complex.object_class">
                      <td>Класс</td>
                      <td>{{ complex.object_class.name }}</td>
                    </tr>
                    <tr v-if="complex.construction_tech">
                      <td>Технология строительства</td>
                      <td>{{ complex.construction_tech.name }}</td>
                    </tr>
                    <tr>
                      <td>Лоты</td>
                      <td>{{ complex.count_lots }}</td>
                    </tr>
                    <tr>
                      <td>В продаже</td>
                      <td>{{ complex.count_lots_in_sale }}</td>
                    </tr>
                    <tr v-if="complex.s_range">
                      <td>Площадь</td>
                      <td>{{ complex.s_range }}м²</td>
                    </tr>
                    <tr>
                      <td>Этажность</td>
                      <td>{{ complex.count_floors }}</td>
                    </tr>
                    <tr v-if="complex.min_price">
                      <td>Апартаменты</td>
                      <td>от {{ complex.min_price }}₽ за м²</td>
                    </tr>
                    <tr>
                      <td>Начало</td>
                      <td>{{ complex.start_of_construction }}</td>
                    </tr>
                    <tr>
                      <td>Сдача</td>
                      <td>{{ complex.end_of_construction }}</td>
                    </tr>
                    <tr>
                      <td>Инфраструктура</td>
                      <td>{{ complex.infrastructure }}</td>
                    </tr>
                    <tr>
                      <td>Транспортная доступность</td>
                      <td>{{ complex.transport_accessibility }}</td>
                    </tr>
                  </tbody>
                </template>
              </v-simple-table>
              </v-expansion-panel-content>
            </v-expansion-panel>
            <v-expansion-panel>
              <v-expansion-panel-header :expand-icon="icons.mdiChevronDown">
                <h5 class="primary--text">Детали</h5>
              </v-expansion-panel-header>
              <v-expansion-panel-content>
                <v-simple-table>
                <template v-slot:default>
                  <tbody>
                    <tr v-if="complex.trim">
                      <td>Отделка</td>
                      <td>{{ complex.trim }}</td>
                    </tr>
                    <tr v-if="complex.facade">
                      <td>Фасад</td>
                      <td>{{ complex.facade }}</td>
                    </tr>
                    <tr v-if="complex.elevators">
                      <td>Лифты</td>
                      <td>{{ complex.elevators }}</td>
                    </tr>
                    <tr v-if="complex.windows">
                      <td>Окна</td>
                      <td>{{ complex.windows }}</td>
                    </tr>
                    <tr v-if="complex.ventilation">
                      <td>Вентиляция</td>
                      <td>{{ complex.ventilation }}</td>
                    </tr>
                    <tr v-if="complex.conditioning">
                      <td>Кондиционирование</td>
                      <td>{{ complex.conditioning }}</td>
                    </tr>
                  </tbody>
                </template>
              </v-simple-table>
              </v-expansion-panel-content>
            </v-expansion-panel>
            <v-expansion-panel>
              <v-expansion-panel-header :expand-icon="icons.mdiChevronDown">
                <h5 class="primary--text">Юридические детали</h5>
              </v-expansion-panel-header>
              <v-expansion-panel-content>
                <v-simple-table>
                <template v-slot:default>
                  <tbody>
                    <tr v-if="complex.cadastre">
                      <td>Кадастр</td>
                      <td>{{ complex.cadastre }}</td>
                    </tr>
                    <tr v-if="complex.tax">
                      <td>Налог</td>
                      <td>{{ complex.tax }}</td>
                    </tr>
                    <tr v-if="complex.content">
                      <td>Содержание</td>
                      <td>{{ complex.content }}</td>
                    </tr>
                    <tr v-if="complex.contract">
                      <td>Договор</td>
                      <td>{{ complex.contract }}</td>
                    </tr>
                    <tr v-if="complex.ceilings">
                      <td>Потолки</td>
                      <td>{{ complex.ceilings }}</td>
                    </tr>
                    <tr v-if="complex.parking">
                      <td>Паркинг</td>
                      <td>{{ complex.parking }}</td>
                    </tr>
                    <tr v-if="complex.parking_price">
                      <td>Паркинг, Р</td>
                      <td>{{ complex.parking_price }}</td>
                    </tr>
                    <tr v-if="complex.trade_registration">
                      <td>Регистрация сделки</td>
                      <td>{{ complex.trade_registration }}</td>
                    </tr>
                    <tr v-if="complex.mortgage">
                      <td>Ипотека</td>
                      <td>{{ complex.mortgage }}</td>
                    </tr>
                    <tr v-if="complex.installment">
                      <td>Рассрочка</td>
                      <td>{{ complex.installment }}</td>
                    </tr>
                    <tr v-if="complex.promotions">
                      <td>Акции</td>
                      <td>{{ complex.promotions }}</td>
                    </tr>
                    <tr v-if="complex.complex_infrastructure">
                      <td>Инфраструктура комплекса</td>
                      <td>{{ complex.complex_infrastructure }}</td>
                    </tr>
                    <tr v-if="complex.commercial_space">
                      <td>Коммерческие площади</td>
                      <td>{{ complex.commercial_space }}</td>
                    </tr>
                  </tbody>
                </template>
              </v-simple-table>
              </v-expansion-panel-content>
            </v-expansion-panel>
            <v-expansion-panel>
              <v-expansion-panel-header :expand-icon="icons.mdiChevronDown">
                <h5 class="primary--text">Закрытые для клиента данные</h5>
              </v-expansion-panel-header>
              <v-expansion-panel-content>
                <v-simple-table>
                <template v-slot:default>
                  <tbody>
                    <tr v-if="complex">
                      <td>Будни</td>
                      <td>{{ complex.weekdays_from }}-{{ complex.weekdays_to }}</td>
                    </tr>
                    <tr v-if="complex">
                      <td>Выходные</td>
                      <td>{{ complex.weekend_form }}-{{complex.weekend_to}}</td>
                    </tr>
                    <tr v-if="complex.sales_office_address">
                      <td>Адрес офиса продаж</td>
                      <td>{{ complex.sales_office_address }}</td>
                    </tr>
                    <tr v-if="complex.note">
                      <td>Примечание</td>
                      <td>{{ complex.note }}</td>
                    </tr>
                    <tr v-if="complex.parking_close">
                      <td>Паркинг</td>
                      <td>{{ complex.parking_close }}</td>
                    </tr>
                  </tbody>
                </template>
              </v-simple-table>
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
          v-if="complex.images && complex.images.length"
        >
          <v-carousel
            :show-arrows="complex.images.length > 1"
            hide-delimiters
            v-model="img"
            :next-icon="icons.mdiMenuRight"
            :prev-icon="icons.mdiMenuLeft"
            :delimiter-icon="icons.mdiCircleOutline"
            cycle
            show-arrows-on-hover
            height="300">
            <v-carousel-item
              v-for="(image, i) in complex.images"
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
          v-if="complex.links && complex.links.length"
        >
          <v-chip
            class="ma-2"
            color="primary"
            outlined
            v-for="(link, i) in complex.links"
            :key="i"
            :href="link.link"
            target="_blank"
          >
            {{ link.name }}
          </v-chip>
        </v-card>
        <v-expansion-panels multiple>
          <v-expansion-panel v-if="complex.contacts && complex.contacts.length" style="background-color: transparent !important;">
            <v-expansion-panel-header :expand-icon="icons.mdiChevronDown">
              <h5 class="primary--text text-right">Контакты</h5>
            </v-expansion-panel-header>
            <v-expansion-panel-content>
              <v-card
                color="transparent"
                class="pa-2"
                outlined
                :key="contact.id"
                v-for="(contact, i) in complex.contacts"
                v-if="complex.contacts && complex.contacts.length"
              >
                <h5 class="primary--text">{{contact.name}}</h5>
                <a :href="`tel:${contact.phone}`" class="grey--text" v-if="contact.phone">{{contact.phone}}<br></a>
                <a :href="`mailto:${contact.email}`" class="grey--text" v-if="contact.email">{{contact.email}}</a>
                <p v-if="contact.note">{{contact.note}}</p>
              </v-card>
            </v-expansion-panel-content>
          </v-expansion-panel>
          <v-expansion-panel v-if="complex.files && complex.files.length" style="background-color: transparent !important;">
            <v-expansion-panel-header :expand-icon="icons.mdiChevronDown">
              <h5 class="primary--text text-right">Презентации и документы</h5>
            </v-expansion-panel-header>
            <v-expansion-panel-content>
              <v-card
                color="transparent"
                class="pa-2"
                outlined
                v-for="(type, i) in new Set(complex.files.map(obj => obj.type))"
                :key="i"
              >
                <h4 class="primary--text">{{ type }}</h4>
                <v-card
                  color="transparent"
                  class="pa-2"
                  outlined
                  v-for="(file, index) in complex.files.filter(obj => obj.type === type)"
                  :key="index"
                >
                  <h5 v-if="file.name">{{ file.name }}</h5>
                  <a :href="file.get_url">
                    скачать <span>{{get_filename(file.get_url)}}</span>
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
  name: 'MainComplex',
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
    ...mapGetters('Page', {complex: 'getMain'})
  },
  methods: {
    get_filename (url) {
      if (!url) return ''
      const arrName = url.split('/')
      return arrName[arrName.length - 1]
    }
  }
}
</script>

<style scoped>
.v-sheet {
  box-shadow: none;
}
</style>
