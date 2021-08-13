<!-- Based on tutorial from: https://blog.carbonteq.com/creating-interactive-map-in-vue-js/ -->
<template>
    <div :id="svgId" class="svg-container"></div>
</template>

<script>
import usMap from "../assets/usaSvg.js"
/**
 * @displayName USA Map
 */
export default {
    name: "USAMap",
    data: function() {
        return {
            svgId: "usMap",
            mapAttr: {
                viewBoxWidth: 1100,
                viewBoxHeight: 800,
                imageWidth: 1000,
                imageHeight: 500,
            },
            svgContainer: null
        }
    },
    mounted: function() {
        this.generateVenueMap()
    },
    methods: {
        generateVenueMap: function() {
            const vue = this;
            const mapData = usMap.g.path
            const svgContainer = vue.$svg("usMap").size('100%', '100%').viewbox(185, -10, vue.mapAttr.viewBoxWidth, vue.mapAttr.viewBoxHeight);
            vue.svgContainer = svgContainer;
            mapData.forEach((pathObj) => {
                vue.generatePath(vue,svgContainer, pathObj);
            })
        },
        generatePath: function(svg, svgCont, pathObj) {
            const vue = this;

            const attrs = {
                'fill': "white",
                'stroke': "black",
                'stroke-width': 2,
                'title': pathObj["_title"],
                'map-id': pathObj["_id"],
                'clicked': 'false',
            };
            const element = svgCont.path(pathObj["_d"]).attr(attrs);
            element.click(function () {
                const mapId = this.node.attributes["map-id"].value;
                const title = this.node.attributes["title"].value;
                const paths = document.getElementsByTagName("path")
                for (let i = 0; i < paths.length; i++)
                {
                    paths[i].setAttribute('fill', 'white')
                    paths[i].setAttribute('clicked', 'false')
                }
                element.attr('clicked', 'true')
                element.attr('fill', '#ffd45e');
                vue.$emit("map-clicked", {mapId, title});
            })

            element.on('mouseover', function () {
                element.attr('fill', "#ffd45e");
            })

            element.on('mouseout', function () {
                if (element.attr('clicked') == 'false'){
                    element.attr('fill', 'white');
                }
            })
        },
        clearSelection: function() {
            const paths = document.getElementsByTagName("path")
                for (let i = 0; i < paths.length; i++)
                {
                    paths[i].setAttribute('fill', 'white')
                    paths[i].setAttribute('clicked', 'false')
                }
        }
    }
}
</script>

<style scoped>
</style>

<docs lang="md">
### Description
A Scalable Vector Graphics (SVG) Interactive United States Map based on a tutorial from https://blog.carbonteq.com/creating-interactive-map-in-vue-js/

### Imports 
- US Map Data - "../assets/usaSvg.js"

### Data

svgID *[String]* - The id of the map in the HTML DOM

mapAttr *[JSON object]* - An object containing information about the map component attributes. Format: {viewBoxWidth: 1100, viewBoxHeight: 800, imageWidth: 1000, imageHeight: 500}

svgContainer *[Object]* - Contains the created SVG container.

### Methods

mounted() - runs when the component is loaded and generates the map component.
```jsx static
mounted: function() {
        this.generateVenueMap()
    }
```

generateVenueMap() - Creates the map component.
    Creates an SVG container within the HTML DOM with the attriutes set in the data objects. Then, the container is saved to the component data object. Finally, all of the states are loaded into HTML path tags.
```jsx static
generateVenueMap: function() {
            const vue = this;
            const mapData = usMap.g.path
            const svgContainer = vue.$svg("usMap").size('100%', '100%').viewbox(185, -10, vue.mapAttr.viewBoxWidth, vue.mapAttr.viewBoxHeight);
            vue.svgContainer = svgContainer;
            mapData.forEach((pathObj) => {
                vue.generatePath(vue,svgContainer, pathObj);
            })
        }
```

generatePath() - creates an HTML path tag and path object given svg data

**Params**

svg *[object]* - the svg parsing library

svgCont *[object]* - the svgContainer to place the path in

pathObj *[object]* - containing attributes about the path to load into the path tag

Takes data about a path object from svg data and creates an HTML tag and path object for that given data. First, default attributes for the object are loaded. Then, functions to handle when an object is clicked or hovered over are created.
When an object is clicked, the fill is set to a yellow color, and the fill of all other path objects is cleared. When an object is hovered over, the object's fill is temporarily set to yellow.
When the mouse leaves the object, the fill is reset to white. 

```jsx static
generatePath: function(svg, svgCont, pathObj) {
            const vue = this;

            const attrs = {
                'fill': "white",
                'stroke': "black",
                'stroke-width': 2,
                'title': pathObj["_title"],
                'map-id': pathObj["_id"],
                'clicked': 'false',
            };
            const element = svgCont.path(pathObj["_d"]).attr(attrs);
            element.click(function () {
                const mapId = this.node.attributes["map-id"].value;
                const title = this.node.attributes["title"].value;
                const paths = document.getElementsByTagName("path")
                for (let i = 0; i < paths.length; i++)
                {
                    paths[i].setAttribute('fill', 'white')
                    paths[i].setAttribute('clicked', 'false')
                }
                element.attr('clicked', 'true')
                element.attr('fill', '#ffd45e');
                vue.$emit("map-clicked", {mapId, title});
            })

            element.on('mouseover', function () {
                element.attr('fill', "#ffd45e");
            })

            element.on('mouseout', function () {
                if (element.attr('clicked') == 'false'){
                    element.attr('fill', 'white');
                }
            })
        }
```

clearSelection() - clears the formatting of all of the path objects in the component

```jsx static
clearSelection: function() {
            const paths = document.getElementsByTagName("path")
                for (let i = 0; i < paths.length; i++)
                {
                    paths[i].setAttribute('fill', 'white')
                    paths[i].setAttribute('clicked', 'false')
                }
        }
```
</docs>