import Vue from "vue";
import VueRouter from "vue-router";
import Home from "../views/Home.vue";
import ExpenseEditor from "../components/Expenses/ExpenseEditor.vue";
import ExpenseAdd from "../components/Expenses/ExpenseAdd.vue";

Vue.use(VueRouter);

const routes = [
  {
    path: "/",
    name: "home",
    component: Home
  },
  {
    path: "/expenses/:id/",
    name: "expenses.edit",
    component: ExpenseEditor,
    props: true
  },
  {
    path: "/expenses/add/",
    name: "expenses.add",
    component: ExpenseAdd,
  },
  {
    path: "/about",
    name: "about",
    // route level code-splitting
    // this generates a separate chunk (about.[hash].js) for this route
    // which is lazy-loaded when the route is visited.
    component: () =>
      import(/* webpackChunkName: "about" */ "../views/About.vue")
  }
];

const router = new VueRouter({
  mode: "history",
  // base: process.env.BASE_URL,
  routes
});

export default router;
