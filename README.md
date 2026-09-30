# 人防工程运维管理平台

面向人防工程台账、防护设备、通风滤毒、水电设施、消防系统、防汛排涝、维护保养与改建审批的一体化人防工程运维管理后台。

这是一个前后端分离的管理平台：前端 Vue 3 + Vite + TypeScript，后端 FastAPI（Python）。
两边各自独立启动，前端 dev server 已关掉自动打开页面，启动后按终端打印的地址手工打开。

## 目录结构

```text
.
├── frontend/                 Vue 3 + Vite + TypeScript 前端
│   ├── src/views/            每个业务模块一个页面
│   ├── src/api/              统一请求封装
│   ├── src/stores/           会话与筛选状态
│   └── vite.config.ts        dev server 配置（open: false）
├── backend/                  FastAPI（Python） 后端
│   ├── app/routers/          每个业务模块一组接口
│   ├── app/services/         业务规则与状态流转
│   └── app/store.py          内存数据仓库与示例数据
├── .gitignore
└── docker-compose.yml
```

## 启动

### 后端

```bash
cd backend
python3 -m venv .venv && .venv/bin/pip install -r requirements.txt
./run.sh
```

健康检查：`curl http://127.0.0.1:8000/api/health`

### 前端

```bash
cd frontend
npm install
npm run dev
```

前端默认监听 `http://127.0.0.1:5173/`，dev server 不会自动打开浏览器，
需要自己访问。`/api` 由 vite 代理到后端 `http://127.0.0.1:8000`。

## 业务模块

| 模块 | 目录 | 业务对象 | 主要字段 |
| --- | --- | --- | --- |
| 人防工程台账 | `project` | 人防工程 | 工程编号、工程名称、工程类型 |
| 防护门管理 | `door` | 防护门 | 防护门编号、所属工程、防护门类型 |
| 密闭阀门管理 | `valve` | 密闭阀门 | 阀门编号、所属工程、阀门类型 |
| 通风滤毒 | `vent_filter` | 滤毒设备 | 设备编号、设备型号、所属工程 |
| 消防设备 | `water_fire` | 消防设备 | 设备编号、设备类型、所属工程 |
| 排水系统 | `drainage` | 排水泵 | 水泵编号、水泵型号、所属工程 |
| 照明系统 | `lighting` | 照明设备 | 设备编号、设备类型、所属工程 |
| 维护保养 | `maintain` | 保养计划 | 计划编号、所属工程、保养类型 |
| 改建审批 | `modify` | 改建申请 | 申请编号、所属工程、改建内容 |
| 防汛排涝 | `flood` | 防汛物资 | 物资编号、物资名称、所属工程 |
| 空气质量监测 | `air_quality` | 空气质量记录 | 记录编号、所属工程、监测时间 |
| 供电系统 | `power_supply` | 供电设备 | 设备编号、设备类型、所属工程 |
| 平战转换演练 | `drill` | 演练记录 | 演练编号、所属工程、演练类型 |
| 日常巡查 | `patrol` | 巡查记录 | 巡查编号、所属工程、巡查人员 |
| 防护设备台账 | `equipment` | 防护设备 | 设备编号、设备名称、所属工程 |
| 标识标牌管理 | `signage` | 标识标牌 | 标牌编号、标牌类型、所属工程 |

## 约定

- 每个模块的前端页面在 `frontend/src/views/<模块>/index.vue`，后端接口在
  `backend/app/routers/<模块>.py`，业务规则在 `backend/app/services/<模块>.py`。
- 列表接口统一返回 `{ items, total, page, size }`，动作接口统一返回 `{ ok, message }`。
- 状态流转只允许在 `app/services` 里改，路由层不做业务判断。
