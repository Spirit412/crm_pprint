import Vue from 'vue'
import VueRouter from 'vue-router'

Vue.use(VueRouter)

const routes = [{
    path: '/',
    name: 'home',
    meta: {
        layout: 'main',
        auth: true
    },
    component: () =>
        import ('../views/Home.vue')
},
    {
        path: '/login',
        name: 'login',
        meta: {
            layout: 'empty'
        },
        component: () =>
            import ('../views/Login.vue')
    },
    {
        path: '/register',
        name: 'register',
        meta: {
            layout: 'empty'
        },
        component: () =>
            import ('../views/Register.vue')
    },
    {
        path: '/profile',
        name: 'profile',
        meta: {
            layout: 'main'
        },
        component: () =>
            import ('../views/Profile.vue')
    },
    {
        path: '/record',
        name: 'record',
        meta: {
            layout: 'main'
        },
        component: () =>
            import ('../views/Record.vue')
    },
    {
        path: '/zubs',
        name: 'zubs',
        meta: {
            layout: 'main',
            requiresAuth: true,
            auth: true
        },
        component: () =>
            import ('../views/Zubs.vue')
    },
    {
        path: '/zubadd',
        name: 'zubadd',
        meta: {
            layout: 'main',
            requiresAuth: true,
            auth: true
        },
        component: () =>
            import ('../views/ZubAdd.vue')
    },
    {
        path: '/diecuts',
        name: 'diecuts',
        meta: {
            layout: 'main',
            // requiresAuth: true
        },
        component: () =>
            import ('../views/Diecuts')
    },
    {
        path: '/diecutadd',
        name: 'diecutadd',
        meta: {
            layout: 'main',
            // requiresAuth: true
        },
        component: () =>
            import ('../views/DiecutAdd')
    },
    {
        path: '/test_ui',
        name: 'test_ui',
        meta: {
            layout: 'main',
            // requiresAuth: true
        },
        component: () =>
            import ('../views/Test_UI')
    },
    {
        path: '/djobs',
        name: 'djobs',
        meta: {
            layout: 'main',
            // requiresAuth: true
        },
        component: () =>
            import ('../views/DJobs')
    },
    {
        path: '/djobadd',
        name: 'djobadd',
        meta: {
            layout: 'main',
            // requiresAuth: true
        },
        component: () =>
            import ('../views/DJobAdd')
    },
    {
        path: '/customers',
        name: 'customers',
        meta: {
            layout: 'main',
            // requiresAuth: true
        },
        component: () =>
            import ('../views/Customers')
    }
]

const router = new VueRouter({
    mode: 'history',
    base: process.env.BASE_URL,
    routes
})


export default router