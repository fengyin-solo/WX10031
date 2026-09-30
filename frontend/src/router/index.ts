import { createRouter, createWebHistory } from 'vue-router'

import Dashboard from '@/views/Dashboard.vue'
const Project = () => import('@/views/project/index.vue')
const Door = () => import('@/views/door/index.vue')
const Valve = () => import('@/views/valve/index.vue')
const VentFilter = () => import('@/views/vent_filter/index.vue')
const WaterFire = () => import('@/views/water_fire/index.vue')
const Drainage = () => import('@/views/drainage/index.vue')
const Lighting = () => import('@/views/lighting/index.vue')
const Maintain = () => import('@/views/maintain/index.vue')
const Modify = () => import('@/views/modify/index.vue')
const Flood = () => import('@/views/flood/index.vue')
const AirQuality = () => import('@/views/air_quality/index.vue')
const PowerSupply = () => import('@/views/power_supply/index.vue')
const Drill = () => import('@/views/drill/index.vue')
const Patrol = () => import('@/views/patrol/index.vue')
const Equipment = () => import('@/views/equipment/index.vue')
const Signage = () => import('@/views/signage/index.vue')

const router = createRouter({
  history: createWebHistory(),
  routes: [
    { path: '/', name: 'dashboard', component: Dashboard },
    { path: '/project', name: 'project', component: Project },
    { path: '/door', name: 'door', component: Door },
    { path: '/valve', name: 'valve', component: Valve },
    { path: '/vent_filter', name: 'vent_filter', component: VentFilter },
    { path: '/water_fire', name: 'water_fire', component: WaterFire },
    { path: '/drainage', name: 'drainage', component: Drainage },
    { path: '/lighting', name: 'lighting', component: Lighting },
    { path: '/maintain', name: 'maintain', component: Maintain },
    { path: '/modify', name: 'modify', component: Modify },
    { path: '/flood', name: 'flood', component: Flood },
    { path: '/air_quality', name: 'air_quality', component: AirQuality },
    { path: '/power_supply', name: 'power_supply', component: PowerSupply },
    { path: '/drill', name: 'drill', component: Drill },
    { path: '/patrol', name: 'patrol', component: Patrol },
    { path: '/equipment', name: 'equipment', component: Equipment },
    { path: '/signage', name: 'signage', component: Signage },
  ],
})

export default router
