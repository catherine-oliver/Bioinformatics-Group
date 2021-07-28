<template>
    <div class='formContainer'>
        <h1 class="sectionTitle">Create User</h1>
        <form @submit.prevent='submitForm'>
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
            if (value.length < 8) {
                this.msg['password'] = 'Password must be 8 characters long';
            }
            else {
                this.msg['password'] = '';
            }
        }
    },
    methods: {
        onFileUpload() {
            console.log(this.$refs.card.files[0])
            this.cardImage = this.$refs.card.files[0];
        },
        submitForm() {
            var data = new FormData();
            data.append('username', this.username);
            data.append('password', this.password);
            data.append('image', this.cardImage);

            cardVis.createUser(data)
            .then((res => {
                console.log(res);
            }))
            .catch(error => {
                console.log(error);
                this.msg["formError"] = "Error submitting this form"
            })
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
