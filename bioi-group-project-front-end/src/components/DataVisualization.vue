<template>
 <div class= "pageContainer">
     <h1 class="sectionTitle">Data Visualization</h1>
     <div class = 'sideBySide'>
        <div class="mapContainer">
            <USAMap class = 'map' v-on:map-clicked='onMapClick'/>
        </div>
        <div class='dataContainer'>
            <label class = "dataMainTitle">Number of Vaccinated Individuals: </label>
            <br>
            <label class = "dataCount">{{this.vaxData.count}}</label>
            <br>
            <br>
            <div class = "labelRow">
                <span v-if="vaxData.state != 'None'">
                    <label class="dataSubtitle">State:</label>
                    <label class="dataLabel">{{this.vaxData.state}}</label>
                </span> 
            </div>
            <br>
            <div class = "labelRow">
                <span v-if="vaxData.vaxType != 'All'">
                    <label class="dataSubtitle">Vaccine Type: </label>
                    <label class="dataLabel">{{this.vaxData.vaxType}}</label>
                </span> 
            </div>
            <br>
            <div class = "labelRow">
                <span v-if="vaxData.ageRange != 'None'">
                    <label class="dataSubtitle">Age Range: </label>
                    <label class="dataLabel">{{this.vaxData.ageRange}}</label>
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
                 <option value='johnson'>Johnson & Johnson</option>
                 <option value='moderna'>Moderna</option>
                 <option value='pfizer'>Pfizer</option>
             </select>

             <button class="formButton" id='formButton' type="submit">Submit</button>
         </form>
     </div>
 </div>
</template>

<script>
import USAMap from './USAMap.vue';
import dataVis from '../services/dataVisualizationService.js';
export default {
  name: 'DataVisualization',
  components: {
      USAMap,
  },
  data () {
      return {
          state: "None",
          ages: "None",
          vaxType: "All",
          vaxData: {
              state: 'Test',
              count: '1000',
              vaxType: 'All',
              ageRange: "None"
          },
      }
  },
  methods: {
      onMapClick: function(attr){
          console.log(attr)
          console.log(attr.title);
          this.state = attr.title;
      },
      submitForm() {
          var vaccineParams = {
              state: this.state,
              ages: this.ages,
              vaxType: this.vaxType,
          };

          dataVis.getVaccineData(vaccineParams)
          .then(res => {
              this.$set(this, "vaxData", res.data)
          })
          .catch(error => {
              //Do nothing
              console.log(error)
          });

          this.clearForm();
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