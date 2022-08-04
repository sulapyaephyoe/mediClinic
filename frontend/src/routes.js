import { createRouter, createWebHistory } from "vue-router";
// import { createRouter, createWebHistory, RouteRecordRaw } from 'vue-router';
import Posts from './views/PostsData';
import Tests from './views/TestData';
import DoctorsCreate from "./views/doctors/DoctorsCreate.vue";
import DoctorsScheduleCreate from "./views/doctors/DoctorsScheduleCreate.vue";
import AddHospital from "./views/hospitals/AddHospital";
import ViewHospital from "./views/hospitals/ViewHospital";

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
        path: "/doctors_create",
        name: "DoctorsCreate",
        component: DoctorsCreate,
    },
    {
        path: "/schedule_create",
        name: "DoctorsScheduleCreate",
        component: DoctorsScheduleCreate,
    },
    {
        path: "/hospitals/add-hospital",
        name: "AddHospital",
        component: AddHospital,
    },
    {
        path: "/hospitals/view-hospital",
        name: "ViewHospital",
        component: ViewHospital,
    },
];

const router = createRouter({
    history: createWebHistory(process.env.BASE_URL),
    routes,
});

export default router;
