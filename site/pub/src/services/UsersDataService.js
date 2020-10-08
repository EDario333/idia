import http from '../http-common'

class UsersDataService {
  getAll () {
    return http.get('/users')
  }

  get (id) {
    return http.get(`/users/${id}`)
  }

  byEmail (email) {
    return http.get(`/users?email=${email}`)
  }

  create (data) {
    return http.post('/users/', data)
  }

  update (id, data) {
    return http.put(`/users/${id}`, data)
  }

  delete (id) {
    return http.delete(`/users/${id}`)
  }

  deleteAll () {
    return http.delete('/users')
  }

  login(data) {
    return http.post(`/users/login`, data);
  }

  token(data) {
    return http.post(`/token/`, data);
  }
}

export default new UsersDataService()
