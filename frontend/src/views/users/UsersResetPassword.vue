<template>
<div class="container mt-5 mb-5">
    <div id="alert-panel" :class="alert_class" role="alert" v-if="alert_show">
        {{alert_message}}
        <button type="button" class="btn-close" aria-label="Close" @click="alert_show = false"></button>
    </div>
    <div class="container mt-5 mb-5">
       
        <form class="row justify-content-center g-2 form-layout" @submit.prevent="submitForm">
         <!-- <div class="mt-5">
            <span class="lock-icon"><i class="bi bi-lock-fill"></i></span>
        </div> -->
        <div class="row mb-3">
            <label for="password"><h2 class="text-center mb-2">Forgot Password?</h2></label>
            <label for="password" class="text-center">You can reset you password here.</label>
        </div>
           <div class="input-group mt-3 mr-3 ml-3" style="width:400px !important;">
            <div class="input-group-prepend" style=" margin-left: 50px !important;">
                <span class="input-group-text" id="basic-addon1"><i class="bi bi-envelope"></i></span>
            </div>
            <input type="email" class="form-control" placeholder="email address" v-model="email" required>
        </div>
            <div class="row justify-content-center mb-2">
                <div class="col-auto link-btn"><button type="submit" class="btn-style-one mb-3 mt-3">Reset Password</button></div>
            </div>
        </form>
        <div class="text-center fs-6 mb-5">
            <router-link to="/Login" id="text-color">Log In</router-link> or <router-link to="/users/users_create" id="text-color">Sign Up</router-link>
        </div>
    </div>
</div>

</template>

<script>
import { getAPI } from '../../axios-api'

export default {
    name:'UsersResetPassword',
    data () {
        return {
            email: '',
            alert_show: false,
            alert_message: '',
            alert_class: '',
        }
    },
    methods: {
        async submitForm() {
            const dataArray = {
                email: this.email,
            }
            getAPI.post('users/resetPassword',dataArray)
            .then(response => {
                console.log('reset passwrod')
                localStorage.setItem('uid', response.data['id'])
                localStorage.setItem('username', response.data['username'])
                localStorage.setItem('email', response.data['email'])
                localStorage.setItem('code', response.data['code'])
                this.$router.push('/users/confirmCode')
            })
            .catch(err => {
                console.log('reached to catch')
                console.log(err)
               this.alert_show=true;
               this.alert_class = "alert alert-danger alert-dismissible fade show";
               this.alert_message = "Sorry we can't find the email that you entered. Please Check Again!";   
               this.email='';          
            })

        },
        validateEmail(value){
            console.log('reached to validateEmail')
            if (/^\w+([.-]?\w+)*@\w+([.-]?\w+)*(\.\w{2,3})+$/.test(value)) {
                this.msg['email'] = 'Invalid Email Address';
            } else{
                this.msg['email'] = '';
            } 
        },
        validatePassword(value){
            let difference = 8 - value.length;
            if (value.length<8) {
                this.msg['password'] = 'Must be 8 characters! '+ difference + ' characters left' ;
            } else {
                this.msg['password'] = '';
            }
        },
    },
}
</script>

<style scoped>
.row {
   padding-top: 1rem !important;
}
.pass-form {
    border: 1px solid gray;
    border-radius: 10px;
    text-align: center;
    width: 500px;
    margin-left : 25vw;
    justify-content: center;
}
.btn-text {
    font-size: large;
    color: white;
}
.btn-reset {
    margin:auto;
    text-align: center;
}
.lock-icon {
    font-size: 84pt;
    color: rgb(170, 170, 175);
    margin-left: 152px;
}
#basic-addon1{
    height: 53px;
    -webkit-border-radius: 0;
    -moz-border-radius: 0;
    border-radius: 0;
    width: 45px;
}
</style>