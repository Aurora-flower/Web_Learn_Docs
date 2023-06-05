// 所有路由配置

export default [
    {
        path: "/",
        redirect: "/props"
    },
    {
        path: '/props',
        component: () => import('@/pages/01_props/PropsTest.vue'),
    },
    {
        path: '/event',
        component: () => import('@/pages/02_custom-event/EventTest.vue'),
    },
    {
        path: '/bus',
        component: () => import('@/pages/03_pubsub/EventBusTest.vue'),
    },
    {
        path: '/model',
        component: () => import('@/pages/04_v-model/ModelTest.vue'),
    },
    {
        path: '/attrs',
        component: () => import('@/pages/05_attrs/AttrsTest.vue'),
    },
    {
        path: '/ref-parent',
        component: () => import('@/pages/06_ref-parent/RefParentTest.vue'),
    },
    {
        path: '/provide-inject',
        component: () => import('@/pages/07_provide-inject/ProvideInjectTest.vue'),
    },
    {
        path: '/slot',
        component: () => import('@/pages/08_slot/SlotTest.vue'),
    },
    {
        path: '/pinia',
        component: () => import('@/pages/09_pinia/PiniaTest.vue'),
    },
]
