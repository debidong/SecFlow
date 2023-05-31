import { createWebHistory, createRouter } from 'vue-router'
import Login from '@/components/Login.vue'
import Index from '@/components/Index.vue'
import UserList from '@/components/userList.vue'
import Register from '@/components/Register.vue'


const routes = [{
        path: '/',
        name: 'Index',
        component: Index
    }, {
        path: '/login',
        name: 'Login',
        component: Login
    }, {
        path: '/userList',
        name: 'userList',
        component: UserList
    }, {
        path: '/login/register',
        name: 'register',
        component: Register
    }
]

const router = createRouter({
    history: createWebHistory(),
    routes
})

export default router
