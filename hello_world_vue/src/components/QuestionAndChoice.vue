<template>
  <div class="QuestionAndChoice">
    <h1>{{ Question }}</h1>
    <p>{{ Choice }}</p>
  </div>
</template>

<script>
export default {
  name: 'QuestionAndChoice',
  data () {
    return {
      Question: 'Who are you ?',
      Choice: 'xautshuanglong'
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
