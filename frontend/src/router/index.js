import { createRouter, createWebHistory } from 'vue-router'
import Home from '../views/Home.vue'
import Login from '../views/Login.vue'
import Register from '../views/Register.vue'
import AdminDashboard from '../views/AdminDashboard.vue'
import BlogList from '../views/BlogList.vue'
import BlogPost from '../views/BlogPost.vue'
import ForgotPassword from '../views/ForgotPassword.vue'
import ResetPassword from '../views/ResetPassword.vue'

const routes = [
    { path: '/', component: Home },
    { path: '/login', component: Login },
    { path: '/register', component: Register },
    {
        path: '/admin',
        component: AdminDashboard,
        meta: { requiresAuth: true }
    },
    { path: '/blog', component: BlogList },
    { path: '/blog/:slug', component: BlogPost },
    { path: '/forgot-password', component: ForgotPassword },
    { path: '/reset-password/:uid/:token', component: ResetPassword }
]

const router = createRouter({
    history: createWebHistory(),
    routes
})

router.beforeEach((to, from, next) => {
    if (to.meta.requiresAuth && !localStorage.getItem('token')) {
        next('/login')
    } else {
        next()
    }
})

export default router
