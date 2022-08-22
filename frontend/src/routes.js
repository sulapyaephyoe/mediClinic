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
import DoctorsScheduleEditList from './views/doctors/DoctorsScheduleEditList.vue'
import UsersCreate from "./views/users/UsersCreate.vue";
import UsersLogin from "./views/users/UsersLogin.vue";
import UsersResetPassword from "./views/users/UsersResetPassword.vue";
import UsersConfirmPassword from "./views/users/UsersConfirmPassword.vue";
import UsersConfirmCode from "./views/users/UsersConfirmCode.vue";
import TimeTable from "./views/schedules/TimeTable.vue";
import HomePage from "./views/HomePage.vue";
import store from '@/store'
import BookingCreate from './views/booking/BookingCreate.vue'
import BookingList from './views/booking/BookingList.vue'

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
        meta: {
            requireLogin: true
        }
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
        path: '/hospitals/schedule_list',
        name: 'HospitalsScheduleList',
        component: HospitalsScheduleList, 
    },
    {
        path: '/hospitals/schedule_list/:id',
        name: 'DoctorsSchedule',
        component: DoctorsSchedule, 
    },
    {
        path: '/doctors_create',
        name: 'DoctorsCreate',
        component: DoctorsCreate, 
    },
    {
        path: '/doctors_edit/:id',
        name: 'DoctorsEdit',
        component: DoctorsEdit, 
    },
    {
        path: '/doctorslist',
        name: 'DoctorsList',
        component: DoctorsList, 
    },
    {
        path: '/schedule_create/:id',
        name: 'DoctorsScheduleCreate',
        component: DoctorsScheduleCreate, 
    },
    {
        path: '/schedule_list',
        name: 'DoctorsScheduleList',
        component: DoctorsScheduleList, 
    },
    {
        path: '/schedule_list/:id',
        name: 'DoctorsOneSchedule',
        component: DoctorsOneSchedule, 
    },
    {
        path: '/schedule_edit_list/:id',
        name: 'DoctorsScheduleEditList',
        component: DoctorsScheduleEditList, 
    },
    {
        path: '/schedule_edit_list/edit/:doctorid/:scheduleid',
        name: 'DoctorsScheduleEdit',
        component: DoctorsScheduleEdit, 
    },
    {
        path: "/login",
        name: "UsersLogin",
        component: UsersLogin,
        path: '/booking',
        name: 'BookingCreate',
        component: BookingCreate, 
    },
    {
        path: "/users/users_create",
        name: "UsersCreate",
        component: UsersCreate,
	},
        path: '/bookinglist',
        name: 'BookingList',
        component: BookingList, 
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
    {
        path: "/timetable",
        name: "TimeTable",
        component: TimeTable,
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