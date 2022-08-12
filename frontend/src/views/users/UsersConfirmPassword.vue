<template>
<div class="container">
    <div id="alert-panel" :class="alert_class" role="alert" v-if="alert_show">
        {{alert_message}}
        <button type="button" class="btn-close" aria-label="Close" @click="alert_show = false"></button>
    </div>
    <form class="pass-form" @submit.prevent="submitForm">
        <div>
            <span class="lock-icon"><i class="bi bi-lock-fill"></i></span>
        </div>
        
        <div class="row pass-text">
            <div class="col">
            <label for="password1" style="text-align: right !important;">New Password</label></div>
            <div class="col">
            <input type="password" class="form-control text-box" placeholder="Password" v-model="password1" required></div>
        </div>
        <div class="row pass-text">
            <div class="col">
            <label for="password1">Confirm New Password</label></div>
            <div class="col">
            <input type="password" class="form-control text-box" placeholder="Password" v-model="password2" required></div>
        </div>
        <div class="row mb-3" style="margin-left: 100px; margin-right: 100px;">
            <button type="submit" class="btn btn-info mb-3 btn-reset" style="width:300px !important;"><span class="btn-text">Submit</span></button>
        </div>
    </form>
</div>

</template>

<script>
import { getAPI } from '../../axios-api'

export default {
    name:'UsersForgetPassword',
    data () {
        return {
            uid: localStorage.getItem('uid'),
            password1:'',
            password2:'',
            alert_show: false,
            alert_message: '',
            alert_class: '',
        }
    },
    methods: {
        async submitForm() {
            if(this.password1 == this.password2) {
                const dataArray = {
                    username: localStorage.getItem('username'),
                    email: localStorage.getItem('email'),
                    password: this.password1,
                }
                getAPI.put(`users/updateInfo/${this.uid}`,dataArray)
                .then(response => {
                    this.APIData = response.data
                    console.log('reached to then')
                    this.$router.push('/login')                             
                })
            } else {
                this.alert_show=true;
                this.alert_class = "alert alert-danger alert-dismissible fade show";
                this.alert_message = "The passwords not match.";
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

.text-box {
    width: 200px!important;
}

label {
    display:block;
    width: 200px;
    text-align:right;
    
}
.pass-text {
    /* display: flex; */
    /* margin: 20px 50px 20px 50px; */
    align-items: center;
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
}
</style>