import { createRouter, createWebHistory } from "vue-router";
// import { createRouter, createWebHistory, RouteRecordRaw } from 'vue-router';
import AddHospital from "./views/hospitals/AddHospital";
import ViewHospital from "./views/hospitals/ViewHospital";
import DoctorsCreate from './views/doctors/DoctorsCreate.vue'
import DoctorsEdit from './views/doctors/DoctorsEdit.vue'
import DoctorsScheduleCreate from './views/doctors/DoctorsScheduleCreate.vue'
import DoctorsList from './views/doctors/DoctorsList.vue'
import DoctorsScheduleList from './views/doctors/DoctorsScheduleList.vue'
import DoctorsOneSchedule from './views/doctors/DoctorsOneSchedule.vue'
import DoctorsScheduleEdit from './views/doctors/DoctorsScheduleEdit.vue'
import UsersCreate from "./views/users/UsersCreate.vue";
import UsersLogin from "./views/users/UsersLogin.vue";
import UsersResetPassword from "./views/users/UsersResetPassword.vue";
import UsersConfirmPassword from "./views/users/UsersConfirmPassword.vue";
import UsersConfirmCode from "./views/users/UsersConfirmCode.vue";
import HomePage from "./views/HomePage.vue";
import store from '@/store'

const routes = [
    {
        path: "/",
        name: "HomePage",
        component: HomePage,
    },
    {
        path: "/hospitals/add-hospital",
        name: "AddHospital",
        component: AddHospital,
        // meta: {
        //     requireLogin: true
        // }
    },
    {
        path: "/hospitals/view-hospital",
        name: "ViewHospital",
        component: ViewHospital,
        // meta: {
        //     requireLogin: true
        // }       
    },
    {
        path: '/doctors_create',
        name: 'DoctorsCreate',
        component: DoctorsCreate,
        // meta: {
        //     requireLogin: true
        // }
    },
    {
        path: '/doctors_edit/:id',
        name: 'DoctorsEdit',
        component: DoctorsEdit,
        meta: {
            requireLogin: true
        } 
    },
    {
        path: '/doctorslist',
        name: 'DoctorsList',
        component: DoctorsList, 
        meta: {
            requireLogin: true
        }
    },
    {
        path: '/schedule_create/:id',
        name: 'DoctorsScheduleCreate',
        component: DoctorsScheduleCreate, 
        meta: {
            requireLogin: true
        }
    },
    {
        path: '/schedule_edit/:id',
        name: 'DoctorsScheduleEdit',
        component: DoctorsScheduleEdit,
        meta: {
            requireLogin: true
        } 
    },
    {
        path: '/schedule_list',
        name: 'DoctorsScheduleList',
        component: DoctorsScheduleList, 
        // meta: {
        //     requireLogin: true
        // }
    },
    {
        path: '/schedule_list/:id',
        name: 'DoctorsOneSchedule',
        component: DoctorsOneSchedule,
        meta: {
            requireLogin: true
        } 
    },
    {
        path: '/schedule_list/:id',
        name: 'DoctorsOneSchedule',
        component: DoctorsOneSchedule,
        // meta: {
        //     requireLogin: true
        // } 
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
        name: "UsersResetPassword",
        component: UsersResetPassword,
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
    routes
})

router.beforeEach((to, from, next) => {
    if (to.matched.some(record => record.meta.requireLogin) && !store.state.isAuthenticated) {
        console.log('---to in if-----'+to.fullPath)
        next('/login')
    } else {
        next()
    }
  })
export default router;
