<template>
<div class="container mt-5 mb-5">
    <div id="alert-panel" :class="alert_class" role="alert" v-if="alert_show">
        {{alert_message}}
        <button type="button" class="btn-close" aria-label="Close" @click="alert_show = false"></button>
    </div>
    <form class="pass-form" @submit.prevent="submitForm">
        <!-- <div>
            <span class="lock-icon"><i class="bi bi-lock-fill"></i></span>
        </div> -->
        <div class="row mb-3">
            <label><h3 class="text-center">We sent a code to your email</h3></label>
            <label>Enter the 6-digit verification code send to you mail.</label>
        </div>
        <div class="input-group mt-4 mr-3 ml-3" style="width:300px !important; margin-left: 100px !important;">
            <input type="text" class="form-control" placeholder="6 digit code" v-model="code" required>
        </div>
        <div class="row mb-3 mt-3" style="margin-left: 100px; margin-right: 100px;">
            <button type="submit" class="btn-style-one mb-3" style="width:300px !important;">Submit</button>
        </div>
    </form>
</div>

</template>

<script>
//import { getAPI } from '../../axios-api'

export default {
    name:'UsersForgetPassword',
    data () {
        return {
            code: '',
            alert_show: false,
            alert_message: '',
            alert_class: '',
        }
    },
    methods: {
        async submitForm() {
            if(this.code == localStorage.getItem('code')) {
                console.log('ok')
                this.$router.push('/users/confirmPassword')
            } else {
                console.log(localStorage.getItem('code'))
                this.alert_show=true;
                this.alert_class = "alert alert-danger alert-dismissible fade show";
                this.alert_message = "The verification code you entered isn't valide. Please check the code and try again.";
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
}
</style>