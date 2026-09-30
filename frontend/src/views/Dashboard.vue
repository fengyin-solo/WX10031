<template>
  <section class="page">
    <header class="page-head">
      <div>
        <h2>运营概览</h2>
        <p class="page-desc">汇总各业务模块的关键指标，先看总量再看异常。</p>
      </div>
    </header>
    <div class="stat-row">
      <article v-for="card in cards" :key="card.label" class="stat-card">
        <span class="stat-label">{{ card.label }}</span>
        <strong class="stat-value">{{ card.value }}</strong>
      </article>
    </div>
    <table class="data-table">
      <thead>
        <tr><th>业务模块</th><th>今日新增</th><th>待处理</th><th>异常量</th></tr>
      </thead>
      <tbody>
        <tr v-for="row in moduleRows" :key="row.name">
          <td>{{ row.name }}</td>
          <td>{{ row.created }}</td>
          <td>{{ row.pending }}</td>
          <td>{{ row.abnormal }}</td>
        </tr>
      </tbody>
    </table>
  </section>
</template>

<script setup lang="ts">
import { onMounted, ref } from 'vue'

import { fetchJson } from '@/api/client'

type Overview = {
  cards: { label: string; value: number }[]
  modules: { name: string; created: number; pending: number; abnormal: number }[]
}

const cards = ref<Overview['cards']>([])
const moduleRows = ref<Overview['modules']>([])

onMounted(async () => {
  try {
    const payload = await fetchJson<Overview>('/api/overview')
    cards.value = payload.cards
    moduleRows.value = payload.modules
  } catch {
    cards.value = [{"label": "业务模块", "value": 0}, {"label": "今日新增", "value": 0}]
    moduleRows.value = [{"name": "人防工程台账", "created": 0, "pending": 0, "abnormal": 0}, {"name": "防护门管理", "created": 0, "pending": 0, "abnormal": 0}, {"name": "密闭阀门管理", "created": 0, "pending": 0, "abnormal": 0}, {"name": "通风滤毒", "created": 0, "pending": 0, "abnormal": 0}, {"name": "消防设备", "created": 0, "pending": 0, "abnormal": 0}, {"name": "排水系统", "created": 0, "pending": 0, "abnormal": 0}, {"name": "照明系统", "created": 0, "pending": 0, "abnormal": 0}, {"name": "维护保养", "created": 0, "pending": 0, "abnormal": 0}, {"name": "改建审批", "created": 0, "pending": 0, "abnormal": 0}, {"name": "防汛排涝", "created": 0, "pending": 0, "abnormal": 0}, {"name": "空气质量监测", "created": 0, "pending": 0, "abnormal": 0}, {"name": "供电系统", "created": 0, "pending": 0, "abnormal": 0}, {"name": "平战转换演练", "created": 0, "pending": 0, "abnormal": 0}, {"name": "日常巡查", "created": 0, "pending": 0, "abnormal": 0}, {"name": "防护设备台账", "created": 0, "pending": 0, "abnormal": 0}, {"name": "标识标牌管理", "created": 0, "pending": 0, "abnormal": 0}]
  }
})
</script>
