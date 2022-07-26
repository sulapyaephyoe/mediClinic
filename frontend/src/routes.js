import { createRouter, createWebHistory} from 'vue-router' 
// import { createRouter, createWebHistory, RouteRecordRaw } from 'vue-router'
import Posts from './views/PostsData'
import Tests from './views/TestData'

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
const router = createRouter({
    history: createWebHistory(process.env.BASE_URL),
    routes
})

export default router