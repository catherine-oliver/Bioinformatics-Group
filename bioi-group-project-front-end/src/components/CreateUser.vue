<template>
    <div class='formContainer'>
        <h1 class="sectionTitle">Create User</h1>
        <form @submit.prevent='submitForm'>
            <span class='validForm' v-if='msg.formSuccess'>{{msg.formSuccess}}</span>
            <span v-if='msg.formError'>{{msg.formError}}</span>
            <input name='username' type='text' v-model='username' placeholder="Enter Username" required>
            <span v-if='msg.password'>{{msg.password}}</span>
            <input name='password' type='password' v-model='password' placeholder='Enter Password' required>
            <div class='uploadContainer'>
                <label>Vaccine Card:</label>
                <input name='vaxCard' type='file' ref='card' v-on:change='onFileUpload' accept='image/*' required>
            </div>
            <input type='submit'>
        </form>    
    </div>
</template>

<script>
import cardVis from "../services/cardVisualizationService.js"
/**
 * @displayName Create User
 */
export default {
    name: 'CreateUser',
    data () {
        return {
            username: '',
            password: '',
            cardImage: '',
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
        onFileUpload() {
            this.cardImage = this.$refs.card.files[0];
        },
        submitForm() {
            if (this.checkPassword(this.password))
            {
                var data = new FormData();
                data.append('username', this.username);
                data.append('password', this.password);
                data.append('image', this.cardImage);

                cardVis.createUser(data)
                .then((res => {
                    res.data;
                    this.clearForm();
                    this.msg['formSuccess'] = "Form Submitted Successfully"
                }))
                .catch(error => {
                    console.log(error);
                    this.msg["formError"] = "Error submitting this form"
                })
            }
        },
        clearForm() {
            this.username = '';
            this.password = '';
            this.cardImage = '';
            this.msg = [];
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

.uploadContainer {
    width: 50%;
    display: inline-block;
    text-align: left;
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

.validForm {
    color: rgb(3, 163, 3);
}

input[type=text], input[type=password] {
    font-family: 'Lucida Sans', 'Lucida Sans Regular', 'Lucida Grande', 'Lucida Sans Unicode', Geneva, Verdana, sans-serif;
    font-size: 16px;
    padding: 5px;
    margin: 5px 5px;
    display: inline-block;
    width: 50%;
}

input[type=file] {
    font-family: 'Lucida Sans', 'Lucida Sans Regular', 'Lucida Grande', 'Lucida Sans Unicode', Geneva, Verdana, sans-serif;
    font-size: 16px;
    margin: 5px;
    margin-left: 5px;
    margin-right: 0px;
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
A form to create a user.

### Imports 
- Card Visualization Service - "../services/cardVisualizationService.js"

### Data

Username *[String]* - username entered by user

Passord *[String]* - password entered by user

cardImage *[File]* - image file entered by user

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

onFileUpload() - grabs the file uploaded by the user and saves it to the cardImage data object.
```jsx static
onFileUpload() {
            this.cardImage = this.$refs.card.files[0];
        }
```

submitForm() - runs upon submit button click

First, the password to make sure it is greater than 8 characters. Then, the username, password, and image file are added into a form data object. Next, it sends this data to the API through the createUser() method of the card visualization service. If the user is sucessfully added, the form will be cleared and a success message will be added to the msg[] object and displayed. If not, an error message will be added to the msg[] object and displayed.
```jsx static
submitForm() {
            if (this.checkPassword(this.password))
            {
                var data = new FormData();
                data.append('username', this.username);
                data.append('password', this.password);
                data.append('image', this.cardImage);

                cardVis.createUser(data)
                .then((res => {
                    res.data;
                    this.clearForm();
                    this.msg['formSuccess'] = "Form Submitted Successfully"
                }))
                .catch(error => {
                    console.log(error);
                    this.msg["formError"] = "Error submitting this form"
                })
            }
        }
```

clearForm() - clears the form inputs by clearing the data objects.
```jsx static
clearForm() {
            this.username = '';
            this.password = '';
            this.cardImage = '';
            this.msg = [];
        }
```

checkPassword() - Ensures that the password is greather than 8 characters before submitting. In this check, the password cannot be equal to 0.
    
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