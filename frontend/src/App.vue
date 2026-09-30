<template>
  <div class="app-shell">
    <aside class="app-side">
      <h1 class="app-title">人防工程运维管理平台</h1>
      <nav class="nav-list">
        <RouterLink v-for="item in navItems" :key="item.path" :to="item.path" class="nav-item">
          {{ item.label }}
        </RouterLink>
      </nav>
    </aside>
    <main class="app-main">
      <header class="app-head">
        <span class="head-desc">面向人防工程台账、防护设备、通风滤毒、水电设施、消防系统、防汛排涝、维护保养与改建审批的一体化人防工程运维管理后台。</span>
        <span class="head-user">当前值班：{{ store.operator }} · {{ store.shiftLabel }}</span>
      </header>
      <RouterView />
    </main>
  </div>
</template>

<script setup lang="ts">
import { useSessionStore } from '@/stores/session'

const store = useSessionStore()

const navItems = [{ label: "运营概览", path: "/" }, { label: "人防工程台账", path: "/project" }, { label: "防护门管理", path: "/door" }, { label: "密闭阀门管理", path: "/valve" }, { label: "通风滤毒", path: "/vent_filter" }, { label: "消防设备", path: "/water_fire" }, { label: "排水系统", path: "/drainage" }, { label: "照明系统", path: "/lighting" }, { label: "维护保养", path: "/maintain" }, { label: "改建审批", path: "/modify" }, { label: "防汛排涝", path: "/flood" }, { label: "空气质量监测", path: "/air_quality" }, { label: "供电系统", path: "/power_supply" }, { label: "平战转换演练", path: "/drill" }, { label: "日常巡查", path: "/patrol" }, { label: "防护设备台账", path: "/equipment" }, { label: "标识标牌管理", path: "/signage" }]
</script>
