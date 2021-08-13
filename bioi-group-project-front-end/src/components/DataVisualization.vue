<template>
 <div class= "pageContainer">
     <h1 class="sectionTitle">Data Visualization</h1>
     <div class = 'sideBySide'>
        <div class="mapContainer">
            <USAMap class = 'map' v-on:map-clicked='onMapClick'/>
        </div>
        <div class='dataContainer'>
            <label class = "dataMainTitle">Number of Vaccinated Individuals in {{this.vaccineParams.state}}: </label>
            <br>
            <label class = "dataCount">{{this.vaxData.totalCount}}</label>
            <br>
            <br>
            <br>
            <div class = "labelRow">
                <span v-if="vaccineParams.vaxType != 'All'">
                    <label class="dataSubtitle">Number who recieved the {{this.vaccineParams.vaxType}} Vacine: </label>
                    <label class="dataLabel">{{this.vaxData.vaxTypeCount}}</label>
                </span> 
            </div>
            <br>
            <div class = "labelRow">
                <span v-if="vaccineParams.ages != 'None'">
                    <label class="dataSubtitle">Ages {{this.vaccineParams.ages}}: </label>
                    <label class="dataLabel">{{this.vaxData.ageCount}}</label>
                </span> 
            </div>
            <br>
            <br>
            <br>
            <br>
            <br>
            <br>
            <br>
            <br>
            <br>
        </div>
     </div>
     <div class='formContainer'>
         <form class='dataForm' @submit.prevent="submitForm">
             <label class="formLabel">State Selected: </label>
             <label class="formText" style="margin-right:20px">{{this.state}}</label>

             <label class="formLabel">Age Range: </label>
             <select class="formSelect" id = "ages" name="ages" style="margin-right:20px" v-model="ages">
                 <option value="None">None</option>
                 <option value='12-17'>12 - 17</option>
                 <option value='18-64'>18 - 64</option>
                 <option value='65+'>65+</option>
             </select>

             <label class="formLabel">Vaccine Manufacturer: </label>
             <select class="formSelect" id = "manufacturer" name="manufacturer" v-model="vaxType">
                 <option value="All">All</option>
                 <option value='Johnson & Johnson'>Johnson & Johnson</option>
                 <option value='Moderna'>Moderna</option>
                 <option value='Pfizer'>Pfizer</option>
             </select>

             <button class="formButton" id='formButton' type="submit">Submit</button>
         </form>
     </div>
 </div>
</template>

<script>
import USAMap from './USAMap.vue';
import dataVis from '../services/dataVisualizationService.js';
/**
 * @displayName Data Visualization
 */
export default {
  name: 'DataVisualization',
  components: {
      USAMap,
  },
  data () {
      return {
          state: "None",
          stateAbbr: "NA",
          ages: "None",
          vaxType: "All",
          vaccineParams: {
              state: '',
              vaxType: 'All',
              ages: 'None'
          },
          vaxData: {
              totalCount: '',
              vaxTypeCount: '',
              ageCount: ''
          },
      }
  },
  methods: {
      onMapClick: function(attr){
          this.stateAbbr = attr.mapId.substr(3, 5);
          this.state = attr.title;
      },
      submitForm() {
          if (this.stateAbbr) {
            this.vaccineParams.state = this.stateAbbr;
            this.vaccineParams.ages = this.ages;
            this.vaccineParams.vaxType = this.vaxType;
    
            dataVis.getVaccineData(this.vaccineParams)
            .then((res => {
                this.vaxData.totalCount = res.data[0];
                this.vaxData.ageCount = res.data[1];
                this.vaxData.vaxTypeCount = res.data[2];
            }).bind(this))
            .catch(error => {
              //Do nothing
              console.log(error)
            });

          this.clearForm();
          }
      },
      clearForm() {
          this.clearMap()
          this.state = "None",
          this.ages = "None",
          this.vaxType = "All"
      },
      clearMap() {
           const paths = document.getElementsByTagName("path")
                //console.log(paths)
                for (let i = 0; i < paths.length; i++)
                {
                    paths[i].setAttribute('fill', 'white')
                    paths[i].setAttribute('clicked', 'false')
                }
      }
  },
  props: {
  }
}
</script>

<!-- Add "scoped" attribute to limit CSS to this component only -->
<style scoped>
.sectionTitle {
    font-family: 'Lucida Sans', 'Lucida Sans Regular', 'Lucida Grande', 'Lucida Sans Unicode', Geneva, Verdana, sans-serif;
    font-size: 25;
}

.pageContainer {
    width: 100%;
    vertical-align: center;
}

.sideBySide {
    width: 100%;
    height: 100%;
    padding: 0px 5px;
    margin-bottom: 20px;
    display: flex;
    position: relative;

}

.mapContainer {
    width: 50%;
    height: 50%;
    flex: 1;
    margin-right: 20px;
    position: relative;
}

.map {
    padding: 5px;
    height: 100%;
    width: 100%;
    
    border-style: solid;
    border-width: 1px;
    border-color: grey;
    background-color: rgb(69, 203, 247, 0.5);
    
}

.dataContainer{
    width: 50%;
    height: 50%;
    flex-flow: column wrap;
    padding: 22.5px;
    
    border-style: solid;
    border-width: 1px;
    border-color: grey;
    position: relative;
}

.dataMainTitle {
    font-family: 'Lucida Sans', 'Lucida Sans Regular', 'Lucida Grande', 'Lucida Sans Unicode', Geneva, Verdana, sans-serif;
    font-size: 20px;
    font-weight: bold;
    text-decoration: underline;
    margin: 10px;
}

.dataCount {
    font-family: 'Lucida Sans', 'Lucida Sans Regular', 'Lucida Grande', 'Lucida Sans Unicode', Geneva, Verdana, sans-serif;
    font-size: 30px;
    font-weight: bold;
    margin: 10px;
}

.dataSubtitle {
    font-family: 'Lucida Sans', 'Lucida Sans Regular', 'Lucida Grande', 'Lucida Sans Unicode', Geneva, Verdana, sans-serif;
    font-size: 16px;
    font-weight: bold;
    margin: 10px 10px 5px 5px;
}

.dataLabel {
    font-family: 'Lucida Sans', 'Lucida Sans Regular', 'Lucida Grande', 'Lucida Sans Unicode', Geneva, Verdana, sans-serif;
    font-size: 16px;
    margin: 10px 10px 5px 5px;
}

.formContainer {
    width: 100%;
    height: 25%;
    margin: 5px;
    padding: 10px;

    border-style: solid;
    border-width: 1px;
    border-color: grey;
}

.formLabel {
    font-family: 'Lucida Sans', 'Lucida Sans Regular', 'Lucida Grande', 'Lucida Sans Unicode', Geneva, Verdana, sans-serif;
    font-size: 16px;
    font-weight: bold;
    margin: 0px 5px;
}

.formText {
    font-family: 'Lucida Sans', 'Lucida Sans Regular', 'Lucida Grande', 'Lucida Sans Unicode', Geneva, Verdana, sans-serif;
    font-size: 16px;
    margin: 0px 5px;
}

.formSelect {
    font-family: 'Lucida Sans', 'Lucida Sans Regular', 'Lucida Grande', 'Lucida Sans Unicode', Geneva, Verdana, sans-serif;
    font-size: 16px;
    padding: 2px;
    margin: 0px 5px;
}

.formButton {
    font-family: 'Lucida Sans', 'Lucida Sans Regular', 'Lucida Grande', 'Lucida Sans Unicode', Geneva, Verdana, sans-serif;
    font-size: 16px;
    padding: 2px 5px;
    margin: 0px 5px;
}

.dataForm {
    flex-flow: row wrap;
    align-items: center;
    margin-left: auto;
    margin-right:auto;
}

.labelRow {
    flex-flow: row wrap;
    align-items: center;
    margin-left: auto;
    margin-right: auto;
}
</style>

<docs lang="md">
### Description
Allows users to query and view vaccination data from the CDC.

### Imports 
- USA Map - './USAMap.vue'
- Data Visualization Service - '../services/dataVisualizationService.js'

### Data

State *[String]* - Name of State selected by the user

stateAbbr *[String]* - Abbreviation of state selected by the user [Default = 'NA']

ages *[String]* - Age range selected by the user [Default = 'None']

vaxType *[String]* - Vaccine type seleted by the user [Default = 'All']

vaccineParams *[JSON object]* - Holds the state, vaccine type, and ages to be sent to the API. Format: {state: '', vaxType: '', ages: ''}

vaxData *[JSON object]* - Holds the data returned by the API to be displayed. Format: {totalCount: '', vaxTypeCount: '', ageCount: ''}

### Methods

onMapClick() - updates the state and state abbreviation data objects when a state is clicked on the map.
```jsx static
onMapClick: function(attr){
          this.stateAbbr = attr.mapId.substr(3, 5);
          this.state = attr.title;
      }
```

submitForm() - runs upon submit button click

First, checks that a state has been selected and sets the vaccine params data object equal to the entered state, age range, and/or vaccine type. Then, it calls the getVaccineData() function from the data visualization service. Upon a successful return, the vaxData object is updated displaying the data, and the form is cleared. If an error is recieved, nothing happens, and the user is free to submit again.
```jsx static
submitForm() {
          if (this.stateAbbr) {
            this.vaccineParams.state = this.stateAbbr;
            this.vaccineParams.ages = this.ages;
            this.vaccineParams.vaxType = this.vaxType;
    
            dataVis.getVaccineData(this.vaccineParams)
            .then((res => {
                this.vaxData.totalCount = res.data[0];
                this.vaxData.ageCount = res.data[1];
                this.vaxData.vaxTypeCount = res.data[2];
            }).bind(this))
            .catch(error => {
              //Do nothing
              console.log(error)
            });

          this.clearForm();
          }
      }
```

clearForm() - clears the form and map inputs by clearing the data objects.
```jsx static
clearForm() {
          this.clearMap()
          this.state = "None",
          this.ages = "None",
          this.vaxType = "All"
      }
```

clearMap() - removes any coloring & selection on the U.S. Map. Loops through all the states on the map by grabbing HTML path elements and changing their attributes. Each element's fill is set to white and 'clicked' attribute is set to to false.

```jsx static
clearMap() {
           const paths = document.getElementsByTagName("path")
                //console.log(paths)
                for (let i = 0; i < paths.length; i++)
                {
                    paths[i].setAttribute('fill', 'white')
                    paths[i].setAttribute('clicked', 'false')
                }
      }
```
</docs>