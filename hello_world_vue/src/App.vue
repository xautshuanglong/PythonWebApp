<template>
  <div id="app">
    <img src="./assets/logo.png">
    <router-view/>
    <h1> Hello vue.js </h1>
    <h4> —— Shuanglong </h4>
  </div>
</template>

<script>
export default {
  name: 'App'
}
</script>

<style>
#app {
  font-family: 'Avenir', Helvetica, Arial, sans-serif;
  -webkit-font-smoothing: antialiased;
  -moz-osx-font-smoothing: grayscale;
  text-align: center;
  color: #2c3e50;
  margin-top: 60px;
}
</style>
