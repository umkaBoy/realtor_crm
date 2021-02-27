import http from '@/api/Http'

export async function loadData (counter, page) {
  const params = {
    counter,
    page
  }
  let { data } = await http.post('load-data', params)
  return data
}
