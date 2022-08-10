import { createRouter, createWebHistory } from "vue-router";
// import { createRouter, createWebHistory, RouteRecordRaw } from 'vue-router';
import Posts from './views/PostsData';
import DoctorsCreate from "./views/doctors/DoctorsCreate.vue";
import DoctorsScheduleCreate from "./views/doctors/DoctorsScheduleCreate.vue";
import AddHospital from "./views/hospitals/AddHospital";
import UsersCreate from "./views/users/UsersCreate.vue";
import UsersLogin from "./views/users/UsersLogin.vue";
import UsersForgetPassword from "./views/users/UsersForgetPassword.vue";
import UsersConfirmPassword from "./views/users/UsersConfirmPassword.vue";
import UsersConfirmCode from "./views/users/UsersConfirmCode.vue";
import store from '@/store'

const routes = [
    {
        path: '/posts',
        name: 'posts',
        component: Posts, 
    },
    {
        path: "/doctors/doctors_create",
        name: "DoctorsCreate",
        component: DoctorsCreate,
        meta: {
            requireLogin: false
        }
    },
    {
        path: "/doctors/schedule_create",
        name: "DoctorsScheduleCreate",
        component: DoctorsScheduleCreate,
    },
    {
        path: "/hospitals/add-hospital",
        name: "AddHospital",
        component: AddHospital,
        meta: {
            requireLogin: true,
        }
    },
    {
        path: "/login",
        name: "UsersLogin",
        component: UsersLogin,
    },
    {
        path: "/users/users_create",
        name: "UsersCreate",
        component: UsersCreate,
    },
    {
        path: "/users/forgetPassword",
        name: "UsersForgetPassword",
        component: UsersForgetPassword,
    },
    {
        path: "/users/confirmCode",
        name: "UsersConfirmCode",
        component: UsersConfirmCode,
    },
    {
        path: "/users/confirmPassword",
        name: "UsersConfirmPassword",
        component: UsersConfirmPassword,
    },
];

const router = createRouter({
    history: createWebHistory(process.env.BASE_URL),
    routes,
});

router.beforeEach((to, from, next) => {
    if (to.matched.some(record => record.meta.requireLogin) && !store.state.isAuthenticated) {
        console.log('---to in if-----'+to.fullPath)
        next('/login')
    } else {
        next()
    }
  })
export default router;
