<template>
<div class="container">
  <div class="row justify-content-md-center">
    <div class="row">
      <div class="col">
          <label>Title:</label>
      </div>
      <div class="col">
          <input class="input" type="text" placeholder="title" v-model="title">
      </div>
    </div>
    <div class="row">
      <div class="col">
        <label>Content:</label>
      </div>
      <div class="col">
          <input class="input" type="text" placeholder="content" v-model="content"/>
      </div>
    </div>
    <div class="row">
      <div class="col">
        <input type="submit" value="Create Post" @click="save"/>
      </div>       
    </div>
  </div>
</div>

</template>

<script>
    import { getAPI } from '../axios-api'
    export default {
        name: 'TestData',
        data () {
            return {
                title:'',
                content:'',
            }
        },
        methods: {
            save () {
                console.log('Reached to save func')
                const formData = {
                    title: this.title,
                    content: this.content,
                }
                getAPI.post('/posts/',formData)
                .then(response => {
                console.log('Post API has sent data \n'+response)
                })
                .catch(err => {
                console.log(err)
                })

            },
        }
        
    }
</script>

<style scoped>
</style>