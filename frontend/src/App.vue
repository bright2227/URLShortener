<template>
  <!-- <div id="app" :class="$style.app"> -->
    <URLTransfer msg="Welcome to Your Vue.js App"/>
  <!-- </div> -->
</template>

<script>
import URLTransfer from './components/URLTransfer.vue'

export default {
  name: 'App',
  components: {
    URLTransfer
  },
}
</script>

<style module>
  html,
  body {
    height: 100%;
  }
  body {
    background: -webkit-linear-gradient(yellow, tomato);
    background: -o-linear-gradient(yellow, tomato);
    background: -moz-linear-gradient(yellow, tomato);
    background: linear-gradient(yellow, tomato);
    display: flex;
    justify-content: center;
    flex-direction: column;
  }
  body > div {
    flex: 1 0;
    display: flex;
    flex-direction: column;
    justify-content: space-around;
  }
</style>
