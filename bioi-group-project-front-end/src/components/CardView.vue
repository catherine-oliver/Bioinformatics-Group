<template>
    <div class='pageContainer'>
        <img v-bind:src="this.card">   
    </div>
</template>

<script>
import cardVis from "../services/cardVisualizationService.js"
import router from '../router'
/**
 * @displayName Card View
 */
export default {
    name: 'CardView',
    data () {
        return {
            card: '',
        }
    },
    created() {
        cardVis.getCard()
        .then(res => {

            var arr = new Uint8Array(res.data)
            console.log(arr)

            var img = new Blob( [ res.data ], { type: "image/*" } )
            console.log(img)
            /**
             * Stores the converted image
             */
            this.card = window.URL.createObjectURL(res.data);
        })
        .catch(err => {
            err;
            router.push("/login")
            this.$destory;
        });
    },
    beforeDestroy() {
        this.card = '';
        localStorage.clear()
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

<docs lang="md">
### Description
Displays the vaccine card of a logged-in user

### Imports 
- Card Visualization Service - "../services/cardVisualizationService.js"
- Router - "../router"

### Data

Card - Image file retrieved from API

### Methods

created() - runs on creation of page
    Calls the getCard() function from the cardViewService.
    Upon successful validation that user is logged in, converts the binary image data recieved into an image file format.
    Upon failure to validate that user is logged in, destroys the instance and returns to the login page.
```jsx static
created() {
        cardVis.getCard()
        .then(res => {

            var arr = new Uint8Array(res.data)

            var img = new Blob( [ res.data ], { type: "image/*" } )

            this.card = window.URL.createObjectURL(res.data);
        })
        .catch(err => {
            err;
            router.push("/login")
            this.$destory;
        });
    }
```

beforeDestroy() - runs before the page is destroyed
    Clears any image data from the card data object and clears the browser local storage.
```jsx static
beforeDestroy() {
        this.card = '';
        localStorage.clear()
    }
```

</docs>