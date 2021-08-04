<template>
    <div class='pageContainer'>
        <img v-bind:src="this.card">   
    </div>
</template>

<script>
import cardVis from "../services/cardVisualizationService.js"
import router from '../router'
export default {
    name: 'CardView',
    data () {
        return {
            card: '',
            username: ''
        }
    },
    created() {
        cardVis.getCard()
        .then(res => {

            console.log(res)

            console.log(res.data)
            console.log(typeof(res.data))
            /*var byteArray = new Uint8Array(res.data);
            console.log(byteArray);
            var str = String.fromCharCode.apply(null, byteArray);
            console.log(str)
            var src = "data:image/jpeg;base64," + btoa(str);*/

            var arr = new Uint8Array(res.data)
            console.log(arr)

            var img = new Blob( [ res.data ], { type: "image/*" } )
            console.log(img)
            //var url = window.URL.createObjectURL(img)
            console.log(window.URL.createObjectURL(res.data))
            this.card = window.URL.createObjectURL(res.data);
        })
        .catch(err => {
            err;
            router.push("/login")
            this.$destory;
        });
    },
    beforeDestroy() {
        this.username = '';
        this.card = '';
        localStorage.clear()
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
    }
}
</script>

<!-- Add "scoped" attribute to limit CSS to this component only -->
<style scoped>


.pageContainer {
    margin-top: 10px;
}

h1 {
    font-family: 'Lucida Sans', 'Lucida Sans Regular', 'Lucida Grande', 'Lucida Sans Unicode', Geneva, Verdana, sans-serif;
    font-size: 20px; 
}

img {
    height: 50%;
    width: 50%;
}

label {
    font-family: 'Lucida Sans', 'Lucida Sans Regular', 'Lucida Grande', 'Lucida Sans Unicode', Geneva, Verdana, sans-serif;
    font-size: 16px;
}



</style>