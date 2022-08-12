<template>
    <div id="alert-panel" :class="alert_class" role="alert" v-if="alert_show">
        {{alert_message}}
        <button type="button" class="btn-close" aria-label="Close" @click="alert_show = false"></button>
    </div>
    <div class="wrapper">
        <div class="logo">
            <img src="https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcQU7vh6d9dU-8YKojjRcLrVnJoWzv-HEYLSpwYymRH4T521wZwzOkdnYBGRXs4ECPITYIM&usqp=CAU" alt="">
        </div>
        <div class="text-center mt-4 name">
            Log In
        </div>
        <form class="p-3 mt-3" @submit.prevent="submitForm">
            <div class="form-field d-flex align-items-center">
                <span class="far fa-user"></span>
                <input type="text" name="userName" id="userName" placeholder="Username" v-model="username">
            </div>
            <div class="form-field d-flex align-items-center">
                <span class="fas fa-key"></span>
                <input type="password" name="password" id="pwd" placeholder="Password" v-model="password">
            </div>
            <button class="btn mt-3">Login</button>
        </form>
        <div class="text-center fs-6">
            <router-link to="/users/forgetPassword">Forget password?</router-link> or <router-link to="/users/users_create">Sign Up</router-link>
        </div>
    </div>
</template>

<script>
import { getAPI } from '../../axios-api'
export default {
    name: 'UsersLogin',
    data() {
        return {
            username: '',
            password: '',
            errors: [],
            alert_show: false,
            alert_message: '',
            alert_class: '',
        }
    },
    methods: {
        async submitForm() {
            const dataArray = {
                username: this.username,
                password: this.password,
            }
            getAPI.post('dj-rest-auth/login/',dataArray)
            .then(response => {
                this.chkAdminStatus(this.username)
                const token = response.data.key
                this.$store.commit('setToken', token)
                getAPI.defaults.headers.common['Authorization'] = 'Token '+token
                localStorage.setItem('token', token)      
                this.$router.push('hospitals/add-hospital')                  
            })
            .catch(error => {
                console.log(error)
                this.username = '';
                this.password = '';
                this.alert_show=true;
               this.alert_class = "alert alert-danger alert-dismissible fade show";
               this.alert_message = "Username or password not match.";  
            })
        },

        async chkAdminStatus(admin_username) {
            getAPI.get(`users/get_user/${admin_username}`)
            .then(response => {
               // store.state.isAdmin = response.data['is_superuser']
                this.$store.commit('adminRole',response.data['is_superuser'])
               // console.log('reached to chkAdmin---'+store.state.isAdmin)
            })
            .catch(err => {
                console.log(err)
            })
        }
    }
}
</script>

<style scoped>
/* Importing fonts from Google */
@import url('https://fonts.googleapis.com/css2?family=Poppins:wght@300;400;500;600;700;800;900&display=swap');

/* Reseting */
* {
    margin: 0 ;
    margin-top: 0 !important;
    padding: 0;
    box-sizing: border-box;
    font-family: 'Poppins', sans-serif;
}

body {
    background: #ecf0f3;
}

.wrapper {
    max-width: 350px;
    min-height: 500px;
    margin: 80px auto;
    padding: 40px 30px 30px 30px;
    background-color: #ecf0f3;
    border-radius: 15px;
    box-shadow: 13px 13px 20px #cbced1, -13px -13px 20px #fff;
}

.logo {
    width: 80px;
    margin: auto;
}

.logo img {
    width: 100%;
    height: 80px;
    object-fit: cover;
    border-radius: 50%;
    box-shadow: 0px 0px 3px #5f5f5f,
        0px 0px 0px 5px #ecf0f3,
        8px 8px 15px #a7aaa7,
        -8px -8px 15px #fff;
}

.wrapper .name {
    font-weight: 600;
    font-size: 1.4rem;
    letter-spacing: 1.3px;
    padding-left: 10px;
    color: #555;
}

.wrapper .form-field input {
    width: 100%;
    display: block;
    border: none;
    outline: none;
    background: none;
    font-size: 1.2rem;
    color: #666;
    padding: 10px 15px 10px 10px;
    /* border: 1px solid red; */
}

.wrapper .form-field {
    padding-left: 10px;
    margin-bottom: 20px;
    border-radius: 20px;
    box-shadow: inset 8px 8px 8px #cbced1, inset -8px -8px 8px #fff;
}

.wrapper .form-field .fas {
    color: #555;
}

.wrapper .btn {
    box-shadow: none;
    width: 100%;
    height: 40px;
    background-color: #03A9F4;
    color: #fff;
    border-radius: 25px;
    box-shadow: 3px 3px 3px #b1b1b1,
        -3px -3px 3px #fff;
    letter-spacing: 1.3px;
}

.wrapper .btn:hover {
    background-color: #039BE5;
}

.wrapper a {
    text-decoration: none;
    font-size: 0.8rem;
    color: #03A9F4;
}

.wrapper a:hover {
    color: #039BE5;
}

@media(max-width: 380px) {
    .wrapper {
        margin: 30px 20px;
        padding: 40px 15px 15px 15px;
    }
}
</style>