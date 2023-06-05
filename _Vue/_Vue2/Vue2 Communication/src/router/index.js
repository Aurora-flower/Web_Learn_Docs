import Vue from "vue";
import VueRouter from "vue-router";
Vue.use(VueRouter);

import communicationRoute from "@/router/communication-route";

export default  new VueRouter({
    routes:[
        communicationRoute,
    ],
});