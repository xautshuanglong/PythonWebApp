<template>
  <div class="Test">
    <h1>{{ TestApp }}</h1>
  </div>
</template>

<script>
export default {
  name: 'Test',
  data () {
    return {
      TestApp: 'This is test page'
    }
  }
}
</script>

<!-- Add "scoped" attribute to limit CSS to this component only -->
<style scoped>
h1, h2
{
  font-weight: normal;
}
</style>
