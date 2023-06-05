import Communication from '@/pages/index.vue'
export default {
    path: '/communication',
    component: Communication,
    children: [
        {
            path: '/props',
            // 路由组件懒加载
            component: () => import('@/pages/01_props/PropsTest.vue'),
        },
        {
            path: '/event',
            component: () => import('@/pages/02_custom-event/EventTest'),
        },
        {
            path: '/bus',
            component: () => import('@/pages/03_event-bus/EventBusTest'),
        },
        {
            path: '/model',
            component: () => import('@/pages/04_v-model/ModelTest'),
        },
        {
            path: '/sync',
            component: () => import('@/pages/05_sync/SyncTest'),
        },
        {
            path: '/attrs-listeners',
            component: () => import('@/pages/06_attrs-listeners/AttrsListenersTest'),
        },
        {
            path: '/ref-children-parent',
            component: () => import('@/pages/07_ref-children-parent/RefChildrenParentTest'),
        },
        {
            path: '/mixin',
            component: () => import('@/pages/08_mixin/MixinTest.vue'),
        },
        {
            path: '/provide-inject',
            component: () => import('@/pages/09_provide-inject/ProvideInjectTest'),
        },
        {
            path: '/vuex',
            component: () => import('@/pages/10_vuex/VuexTest'),
        },
        {
            path: '/slot',
            component: () => import('@/pages/11_slot/SlotTest'),
        },
        {
            path: '/pubsub',
            component: () => import('@/pages/12_pubsub/index'),
        },
    ]
}