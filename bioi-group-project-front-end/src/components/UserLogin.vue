<template>
    <div class='formContainer'>
        <h1 class="sectionTitle">Login</h1>
        <form @submit.prevent='submitForm'>
            <input name='username' type='text' v-model='username' placeholder="Enter Username" required>
            <span v-if='msg.password'>{{msg.password}}</span>
            <input name='password' type='password' v-model='password' placeholder='Enter Password' required>
            <input type='submit'>
        </form>    
    </div>
</template>

<script>
import cardVis from "../services/cardVisualizationService.js"
export default {
    name: 'Login',
    data () {
        return {
            username: '',
            password: '',
            msg: []
        }
    },
    watch: {
        password(value) {
            if (value.length < 8 && value.length != 0) {
                this.msg['password'] = 'Password must be 8 characters long';
            }
            else {
                this.msg['password'] = '';
            }
        }
    },
    methods: {
        submitForm() {
            if(this.checkPassword(this.password))
            {
            var user = {
                username: this.username,
                password: this.password
            }

                cardVis.login(user)
            }
        },
        checkPassword(pass) {
            if (pass.length >= 8) {
                return true;
            }
            else {
                return false
            }

        }
    }
}
</script>

<!-- Add "scoped" attribute to limit CSS to this component only -->
<style scoped>

.sectionTitle {
    font-family: 'Lucida Sans', 'Lucida Sans Regular', 'Lucida Grande', 'Lucida Sans Unicode', Geneva, Verdana, sans-serif;
    font-size: 25;
}

.formContainer {
    margin-top: 10px;
}


label {
    font-family: 'Lucida Sans', 'Lucida Sans Regular', 'Lucida Grande', 'Lucida Sans Unicode', Geneva, Verdana, sans-serif;
    font-size: 16px;
}

span {
    font-family: 'Lucida Sans', 'Lucida Sans Regular', 'Lucida Grande', 'Lucida Sans Unicode', Geneva, Verdana, sans-serif;
    font-size: 16px;
    padding: 5px;
    color: red;
    margin: 0px 5px;
    display: inline-block;
    width: 50%;
}

input[type=text], input[type=password] {
    font-family: 'Lucida Sans', 'Lucida Sans Regular', 'Lucida Grande', 'Lucida Sans Unicode', Geneva, Verdana, sans-serif;
    font-size: 16px;
    padding: 5px;
    margin: 5px 5px;
    display: inline-block;
    width: 50%;
}


input[type=submit] {
    display: inline-block;
    font-family: 'Lucida Sans', 'Lucida Sans Regular', 'Lucida Grande', 'Lucida Sans Unicode', Geneva, Verdana, sans-serif;
    font-size: 16px;
    margin: 5px;
    margin-left: 47%;
    padding: 5px;
}


</style>