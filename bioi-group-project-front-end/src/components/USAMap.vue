<!-- Based on tutorial from: https://blog.carbonteq.com/creating-interactive-map-in-vue-js/ -->
<template>
    <div :id="svgId" class="svg-container"></div>
</template>

<script>
import usMap from "../assets/usaSvg.js"
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
                //console.log(paths)
                for (let i = 0; i < paths.length; i++)
                {
                    paths[i].setAttribute('fill', 'white')
                    paths[i].setAttribute('clicked', 'false')
                }
                element.attr('clicked', 'true')
                element.attr('fill', '#ffd45e');
                //console.log(element.attr())
                vue.$emit("map-clicked", {mapId, title});
            })

            element.on('mouseover', function () {
                element.attr('fill', "#ffd45e");
            })

            element.on('mouseout', function () {
                //console.log(element.attr('clicked'));
                if (element.attr('clicked') == 'false'){
                    element.attr('fill', 'white');
                }
            })
        },
        clearSelection: function() {
            const paths = document.getElementsByTagName("path")
                //console.log(paths)
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