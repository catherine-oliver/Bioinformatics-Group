<template>
  <div id="app">
    <div id="nav">
      <router-link class='navItem' to="/">Home</router-link> |
      <router-link class='navItem' to="/info">General Info</router-link> |
      <router-link class='navItem' to="/data-visualization">Data Visualization</router-link> |
      <router-link class='navItem' to="/create-user">Create User</router-link> |
      <router-link class='navItem' to="/login">Vaccine Card View</router-link>
    </div>
    <router-view/>
  </div>
</template>

<style scoped>
#app {
  font-family: Avenir, Helvetica, Arial, sans-serif;
  -webkit-font-smoothing: antialiased;
  -moz-osx-font-smoothing: grayscale;
  text-align: center;
}

#nav {
  width: 100%;
  padding: 10px;
  background-color: rgb(17, 112, 253);
  text-align: left;
  box-shadow: 0px 1px 5px black;
}

.navItem {
  font-weight: bold;
  padding:10px;
  font-family: 'Lucida Sans', 'Lucida Sans Regular', 'Lucida Grande', 'Lucida Sans Unicode', Geneva, Verdana, sans-serif;
  background-color: rgb(17, 112, 253);
  text-decoration: none;
  color: black;
}

.navItem:hover {
  background-color: rgb(15, 100, 228);
}
</style>
