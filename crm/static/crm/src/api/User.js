import http from '@/api/Http'

export async function self () {
  let { data } = await http.get('profile')
  return data
}

export async function get (id) {
  const params = { id }
  let { data } = await http.get('profile', { params })
  return data
}
