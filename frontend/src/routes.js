import { createRouter, createWebHistory} from 'vue-router' 
// import { createRouter, createWebHistory, RouteRecordRaw } from 'vue-router'
import Posts from './views/PostsData'
import Tests from './views/TestData'
import DoctorsCreate from './views/doctors/DoctorsCreate.vue'
import DoctorsEdit from './views/doctors/DoctorsEdit.vue'
import DoctorsScheduleCreate from './views/doctors/DoctorsScheduleCreate.vue'
import DoctorsList from './views/doctors/DoctorsList.vue'
import DoctorsScheduleList from './views/doctors/DoctorsScheduleList.vue'
import DoctorsOneSchedule from './views/doctors/DoctorsOneSchedule.vue'
import DoctorsScheduleEdit from './views/doctors/DoctorsScheduleEdit.vue'
import DoctorsScheduleEditList from './views/doctors/DoctorsScheduleEditList.vue'

const routes = [
    {
        path: '/posts',
        name: 'posts',
        component: Posts, 
    },
    {
        path: '/tests',
        name: 'tests',
        component: Tests, 
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
        name: 'DoctorsOneSchedule',
        component: DoctorsOneSchedule, 
    },
    {
        path: '/schedule_edit_list/:id',
        name: 'DoctorsScheduleEditList',
        component: DoctorsScheduleEditList, 
    },
]
const router = createRouter({
    history: createWebHistory(process.env.BASE_URL),
    routes
})

export default router