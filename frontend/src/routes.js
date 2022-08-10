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

const routes = [
    {
        path: "/hospitals/add-hospital",
        name: "AddHospital",
        component: AddHospital,
    {
       path: '/schedule_create',
        name: 'DoctorsScheduleCreate',
        component: DoctorsScheduleCreatewHospi
	{
        path: '/doctors_create',
        name: 'DoctorsCreate',
        component: DoctorsCreate, 
    },tal,
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
        path: '/schedule_crreate',
        component: DoctorsScheduleCreate, 
    },
    {
        path: '/schedule_edit/:id',
        name: 'DoctorsScheduleEdit',
        component: DoctorsScheduleEdit, 
    },
    {
        path: '/schedule_list',
        name: 'DoctorsScheduleList',
        component: DoctorsScheduleList, 
    },
    {
        path: '/schedule_list/:id',
        name: 'DoctorsOneSc
const router = createRouter({
    history: createWebHistory(process.env.BASE_URL),
    routes
})
hedule',
        component: DoctorsOneSchedule, 
    },
]
const router = createRouter({
    history: createWebHistory(process.env.BASE_URL),
    routes,
});

export default router
