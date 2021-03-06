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
        path: '/categories',
        name: 'categories',
        meta: {
            layout: 'main'
        },
        component: () =>
            import ('../views/Categories.vue')
    },
    {
        path: '/historys',
        name: 'historys',
        meta: {
            layout: 'main'
        },
        component: () =>
            import ('../views/Historys.vue')
    },
    {
        path: '/detail',
        name: 'detail',
        meta: {
            layout: 'main'
        },
        component: () =>
            import ('../views/Detail.vue')
    },
    {
        path: '/planning',
        name: 'planning',
        meta: {
            layout: 'main'
        },
        component: () =>
            import ('../views/Planning.vue')
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
        path: '/djobsadd',
        name: 'djobsadd',
        meta: {
            layout: 'main',
            // requiresAuth: true
        },
        component: () =>
            import ('../views/DJobsAdd')
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