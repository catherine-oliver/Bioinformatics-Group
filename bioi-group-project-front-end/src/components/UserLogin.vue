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
                .then(res => {
                    res;
                })
                .catch(err => {
                    err;
                })
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
<docs lang="md">
### Description
A form for a user to login prior to viewing their vaccine card.

### Imports 
- Card Visualization Service - "../services/cardVisualizationService.js"

### Data

Username *[String]* - username entered by user

Passord *[String]* - password entered by user

msg *[String Array]* - array holding error messages

### Watch Methods

password() - checks the value of the password field upon each update

**Params:**
        
value *[String]* - the value entered by the user
    
Checks whether the password is less than 8 characters and not equal to 0. If so, it pushes an error message to the msg[] object to be displayed. If not, nothing happens. The not equal to 0 condition ensures that no message will be displayed if input is blank.
```jsx static
password(value) {
            if (value.length < 8 && value.length != 0) {
                this.msg['password'] = 'Password must be 8 characters long';
            }
            else {
                this.msg['password'] = '';
            }
        }
```

### Methods

submitForm() - runs upon submit button click

First, the password to make sure it is greater than 8 characters. Then, the username and password are appended into a JSON object and sent to the API through the login() method of the card visualization service. If the user is sucessfully logged in, the user is redirected to the cardView component. If not, nothing happens, and the user is allowed to try again.
```jsx static
submitForm() {
            if(this.checkPassword(this.password))
            {
            var user = {
                username: this.username,
                password: this.password
            }
                cardVis.login(user)
                .then(res => {
                    res;
                })
                .catch(err => {
                    err;
                })
            }
        }
```

checkPassword() - Ensures that the password is greather than 8 characters
    
**Params:**
    
pass *[string]* - the password to be used
```jsx static
checkPassword(pass) {
            if (pass.length >= 8) {
                return true;
            }
            else {
                return false
            }

        }
```
</docs>