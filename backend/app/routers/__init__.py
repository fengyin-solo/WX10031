"""业务模块路由汇总。

这里统一按别名导入再暴露 ROUTERS：模块名有可能和内置名撞车（某个业务模块就叫 dict、list
这种名字时），按名字直接 import 会把内置类型覆盖掉，函数注解在运行时求值就会报
'module' object is not subscriptable。
"""
from __future__ import annotations

from app.routers import project as router_project
from app.routers import door as router_door
from app.routers import valve as router_valve
from app.routers import vent_filter as router_vent_filter
from app.routers import water_fire as router_water_fire
from app.routers import drainage as router_drainage
from app.routers import lighting as router_lighting
from app.routers import maintain as router_maintain
from app.routers import modify as router_modify
from app.routers import flood as router_flood
from app.routers import air_quality as router_air_quality
from app.routers import power_supply as router_power_supply
from app.routers import drill as router_drill
from app.routers import patrol as router_patrol
from app.routers import equipment as router_equipment
from app.routers import signage as router_signage

ROUTERS = [router_project, router_door, router_valve, router_vent_filter, router_water_fire, router_drainage, router_lighting, router_maintain, router_modify, router_flood, router_air_quality, router_power_supply, router_drill, router_patrol, router_equipment, router_signage]
