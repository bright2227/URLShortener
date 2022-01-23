<template>
  <div :class="$style.div">
    <div>
      <input id="input1" type="text" :class="$style.input" v-model="shortUrl" placeholder="Short Url">
    </div>

    <div :class="$style.button">
      <div>
        <button type="submit" @click="short2long"> Short2Long</button>
      </div>
      <div>
        <button type="submit" @click="long2short"> Long2Short </button>
      </div>
    </div>

    <div>
      <input id="input2" type="text" :class="$style.input" v-model="longUrl" placeholder="Long Url">
    </div>

    <div>
      <p v-text="message"></p>
      <a v-bind:href="longUrl" v-if="ableRedirect">redirect to LongUrl</a>
    </div>

  </div>
</template>

<script>
import axios from 'axios';

export default {
  name: 'URLTransfer',
  props: {
    msg: String
  },
  data () {
      return {
        shortUrl: '',
        longUrl: '',
        message: '',
        ableRedirect:false
      }
  },
  methods: {
    long2short() {
        axios.post(
          "https://longurl2short.tk/api/shorturl/v1", {"long_url":this.longUrl}
        ).then(
          (res)=>{
            this.longUrl = "";
            this.shortUrl = res.data.short_url;
          }
        ).catch(
          (err)=>{this.message = err; console.log(err); }
        )
    },
    short2long() {
        axios.get(
          "https://longurl2short.tk/api/shorturl/v1/" + this.shortUrl
        ).then(
          (res)=>{
            this.shortUrl = "";
            this.longUrl = res.data.long_url;
            this.ableRedirect = true;
          }
        ).catch(
          (err)=>{this.message = err; console.log(err); }
        )
    },
    watch: {
      shortUrl: (val, ) => {this.shortUrl = val; },
      longUrl: (val, ) => {this.longUrl = val;  this.ableRedirect = false;}
    }
  }
}
</script>

<style module>
  .div {
    flex: 1;
    display: flex;
    align-items: center;
    flex-direction: column;
    text-align: center;
    justify-content: space-around;
  }

  .input {
    text-align: center;
  }

  .button {
    display: flex;
    flex-direction: row;
    text-align: center;
    justify-content: space-around;
    width: 100%;
  }

  .button > div {
    flex: 2;
  }
</style>
