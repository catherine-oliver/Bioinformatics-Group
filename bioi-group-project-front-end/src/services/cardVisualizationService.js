import axios from 'axios';
import router from '../router'


export default {
    async createUser(userParams) {
        console.log(userParams)
        let res = await axios.post(("http://127.0.0.1:5000/createUser"), userParams, { headers: {
            'Content-Type': 'multipart/form-data' }
          })
        return res;
    },

    async login(user) {
      await axios.post(("http://127.0.0.1:5000/login"), {
        username: user.username,
        password: user.password
    })
    .then(response => {
        if (response.data.accessToken) {
            localStorage.setItem('user', JSON.stringify(response.data));
        }
        console.log("Success")
    })
    },

    async getCard() {
        await axios.post(("http://127.0.0.1:5000/login"), {
        username: user.username,
        password: user.password
    })
    .then(response => {
        return response.data
    })
    .except(err => { 
        router.push("/login")
        
    } )

    }
}