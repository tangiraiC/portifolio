import { createRouter, createWebHistory } from 'vue-router'
import Home from '../views/Home.vue'
import Login from '../views/Login.vue'
import Register from '../views/Register.vue'
import AdminDashboard from '../views/AdminDashboard.vue'
import BlogList from '../views/BlogList.vue'
import BlogPost from '../views/BlogPost.vue'
import ForgotPassword from '../views/ForgotPassword.vue'
import ResetPassword from '../views/ResetPassword.vue'
import ResumeView from '../views/ResumeView.vue'
import { applySeo } from '../utils/seo'

const routes = [
    {
        path: '/',
        component: Home,
        meta: {
            title: 'Lincoln | Full-Stack Data Scientist',
            description: 'Explore Lincoln’s portfolio of AI systems, full-stack apps, data tools, predictive analytics, NLP, and business analytics projects.'
        }
    },
    {
        path: '/login',
        component: Login,
        meta: {
            title: 'Login | Lincoln Portfolio',
            description: 'Admin login for Lincoln’s portfolio.',
            noindex: true
        }
    },
    {
        path: '/register',
        component: Register,
        meta: {
            title: 'Register | Lincoln Portfolio',
            description: 'Account registration for Lincoln’s portfolio.',
            noindex: true
        }
    },
    {
        path: '/admin',
        component: AdminDashboard,
        meta: {
            requiresAuth: true,
            title: 'Admin | Lincoln Portfolio',
            description: 'Portfolio admin dashboard.',
            noindex: true
        }
    },
    {
        path: '/blog',
        component: BlogList,
        meta: {
            title: 'Blog | Lincoln Portfolio',
            description: 'Notes and posts from Lincoln on software, AI, data science, analytics, and portfolio project work.'
        }
    },
    {
        path: '/blog/:slug',
        component: BlogPost,
        meta: {
            title: 'Blog Post | Lincoln Portfolio',
            description: 'Read a blog post from Lincoln’s portfolio.'
        }
    },
    {
        path: '/forgot-password',
        component: ForgotPassword,
        meta: {
            title: 'Forgot Password | Lincoln Portfolio',
            description: 'Password reset for Lincoln’s portfolio.',
            noindex: true
        }
    },
    {
        path: '/reset-password/:uid/:token',
        component: ResetPassword,
        meta: {
            title: 'Reset Password | Lincoln Portfolio',
            description: 'Password reset confirmation for Lincoln’s portfolio.',
            noindex: true
        }
    },
    {
        path: '/resume',
        component: ResumeView,
        meta: {
            title: 'Resume | Lincoln Portfolio',
            description: 'View and download Lincoln’s resume, experience, certifications, and portfolio credentials.'
        }
    }
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

router.afterEach((to) => {
    applySeo(to)
})

export default router
