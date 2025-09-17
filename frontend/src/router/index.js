import { createRouter, createWebHistory } from 'vue-router'

import RootView from '../views/RootView.vue'
import DashboardView from '../views/DashboardView.vue'
import HomeView from '../views/HomeView.vue'
import ServersView from '../views/ServersView.vue'
import ServerView from '../views/ServerView.vue'

const router = createRouter({
  history: createWebHistory(import.meta.env.BASE_URL),
  routes: [
    {
      path: '/',
      name: 'root' /* TODO Either show login screen or navbar - Depends if user is logged in in the future */,
      component: RootView,
      children: [
        {
          path: '',
          name: 'dashboard',
          component: DashboardView,
          children: [
            {
              path: '',
              name: 'home',
              component: HomeView,
            },
            {
              path: 'servers',
              name: 'servers',
              component: ServersView,
            },
            {
              path: 'servers/:serverId',
              name: 'server',
              component: ServerView,
            },
          ],
        },
        {
          path: 'settings' /* TODO Add settings functionality */,
          name: 'settings',
        },
      ],
    },
  ],
})

export default router
