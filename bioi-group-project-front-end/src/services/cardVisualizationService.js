import axios from 'axios';
import router from '../router'
import authHeader from './authHeader'

var local = ''

export default {
    async createUser(userParams) {
        let res = await axios.post((local + "/api/createUser"), userParams, { headers: {
            'Content-Type': 'multipart/form-data' }
          })
        return res;
    },

    async login(user) {
      var loginData = new FormData()
      loginData.append('username', user.username);
      loginData.append('password', user.password);
      return axios.post((local + "/api/login"), loginData, { headers: {
          'Content-Type': 'multipart/form-data' }
       })
       .then(response => {
        if (response.data.token) {
            localStorage.setItem('user', JSON.stringify(response.data));
        }
        router.push('/card')
        })
        .catch(err => {
            err;
        });
    },

    async getCard() {
        var head = authHeader()
        let res = await axios.get((local + "/api/getCard"), {params: head, responseType: "blob" }, { headers: {  
            'Content-Type': 'application/json'}});

        return res;

    }
}