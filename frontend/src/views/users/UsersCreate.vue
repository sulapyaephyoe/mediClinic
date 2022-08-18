<template>
<div class="container mt-5 mb-5">
    <div id="alert-panel" :class="alert_class" role="alert" v-if="alert_show">
        {{alert_message}}
        <button type="button" class="btn-close" aria-label="Close" @click="alert_show = false"></button>
    </div>
    
    <form class="row justify-content-center g-2 form-layout" @submit.prevent="submitForm">
    <h3  class="text-center">Sign up your account</h3>
        <div class="row justify-content-center">
            <div class="col-sm-2">
                <label for="username">Username</label>
            </div>
            <div class="col-sm-3">
                <input type="text" class="form-control" id="username" placeholder="john1234" v-model="username">
            </div>
        </div>
        <div class="row justify-content-center">
            <div class="col-sm-2">
                <label for="email">Email</label>
            </div>
            <div class="col-sm-3">
                <input type="email" class="form-control" id="email" placeholder="john@gmail.com" v-model="email">
            </div>
        </div>
        <div class="row justify-content-center mb-2">
            <div class="col-sm-2">
                <label for="password1">Password</label>
            </div>
            <div class="col-sm-3">
                <input type="password" class="form-control" id="password1" placeholder="Password" v-model="password1">
            </div>
        </div>
        <div class="row justify-content-center mb-2">
            <div class="col-sm-2">
                <label for="password2">Confirm Password</label>
            </div>
            <div class="col-sm-3">
                <input type="password" class="form-control" id="password2" placeholder="Password" v-model="password2">
            </div>
        </div>
        <div class="row justify-content-center mb-2">
            <div class="col-auto link-btn"><button type="submit" class="btn-style-one mb-3">Register</button></div>
        </div>
    </form>
      <div class="text-center fs-6">
            <router-link to="/users/forgetPassword" id="text-color">Forget password?</router-link> or <router-link to="/login" id="text-color">Log In</router-link>
        </div>
</div>

</template>

<script>
import { getAPI } from '../../axios-api'

export default {
    name:'UsersCreate',
    data () {
        return {
            username: '',
            email: '',
            password1: '',
            password2: '',
            alert_show: false,
            alert_message: '',
            alert_class: '',
        }
    },
    methods: {
        async submitForm() {
            console.log('reach action')
            const dataArray = {
                username: this.username,
                email: this.email,
                password1: this.password1,
                password2: this.password2,
            }
            getAPI.post('dj-rest-auth/registration/',dataArray)
            .then(response => {
                this.APIData = response.data
                console.log('reached to then')       
                this.$router.push('/login')                      
            })
            .catch(err => {
                console.log('reached to catch')
                console.log(err)
               this.alert_show=true;
               this.alert_class = "alert alert-danger alert-dismissible fade show";
               this.alert_message = err.response.data;             
            })

        },
    },
}
</script>

<style scoped>
.row {
   padding-top: 2rem !important;
}
</style>