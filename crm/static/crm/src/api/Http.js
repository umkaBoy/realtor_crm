import axios from 'axios'

axios.defaults.xsrfHeaderName = 'X-CSRFToken'
axios.defaults.auth = {
  username: 'test@mail.ru',
  password: 'qwerty123'
}
axios.defaults.xsrfCookieName = 'csrftoken'

const instance = axios.create({
  baseURL: '/rest/',
  timeout: 10000
})

export default instance
