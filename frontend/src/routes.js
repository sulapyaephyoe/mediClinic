import { createRouter, createWebHistory } from "vue-router";
// import { createRouter, createWebHistory, RouteRecordRaw } from 'vue-router'
import Posts from './views/PostsData'
import Tests from './views/TestData'
import Posts from './views/PostsData'
// import Postscreate from './views/PostsCreate'
import Tests from './views/TestData'
import Posts from "./views/PostsData";
import Tests from "./views/TestData";
import DoctorsCreate from "./views/doctors/DoctorsCreate.vue";
import DoctorsScheduleCreate from "./views/doctors/DoctorsScheduleCreate.vue";
import AddHospital from "./views/hospitals/AddHospital";

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
]
    {
        path: '/posts',
        name: 'posts',
        component: Posts, 
    },
    // {
    //     path: '/postscreate',
    //     name: 'postscreate',
    //     component: Postscreate, 
    // },
    {
        path: '/tests',
        name: 'tests',
        component: Tests, 
    },
]
  {
    path: "/posts",
    name: "posts",
    component: Posts,
  },
  {
    path: "/tests",
    name: "tests",
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
];

const router = createRouter({
  history: createWebHistory(process.env.BASE_URL),
  routes,
});

export default router;
