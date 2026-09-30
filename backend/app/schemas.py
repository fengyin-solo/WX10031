"""接口出入参模型：列表分页、动作结果与各模块的明细结构。"""
from __future__ import annotations

from typing import Any, Generic, TypeVar

from pydantic import BaseModel, Field

T = TypeVar("T")


class PageResult(BaseModel, Generic[T]):
    items: list[T]
    total: int
    page: int = 1
    size: int = 20


class ActionResult(BaseModel):
    ok: bool
    message: str
    entry: dict[str, Any] | None = None


class EntryPayload(BaseModel):
    """登记或修改一条业务记录时提交的字段集合。"""

    values: dict[str, Any] = Field(default_factory=dict)
    remark: str | None = None



class ProjectEntry(BaseModel):
    """人防工程明细结构。"""

    field_0: str | None = None  # 工程编号
    field_1: str | None = None  # 工程名称
    field_2: str | None = None  # 工程类型
    field_3: str | None = None  # 所在区域
    field_4: str | None = None  # 建筑面积
    field_5: str | None = None  # 防护等级
    field_6: str | None = None  # 建成时间
    field_7: str | None = None  # 工程状态

class DoorEntry(BaseModel):
    """防护门明细结构。"""

    field_0: str | None = None  # 防护门编号
    field_1: str | None = None  # 所属工程
    field_2: str | None = None  # 防护门类型
    field_3: str | None = None  # 安装位置
    field_4: str | None = None  # 设计抗力等级
    field_5: str | None = None  # 密封性能
    field_6: str | None = None  # 上次检测日期
    field_7: str | None = None  # 运行状态

class ValveEntry(BaseModel):
    """密闭阀门明细结构。"""

    field_0: str | None = None  # 阀门编号
    field_1: str | None = None  # 所属工程
    field_2: str | None = None  # 阀门类型
    field_3: str | None = None  # 安装位置
    field_4: str | None = None  # 公称直径
    field_5: str | None = None  # 上次启闭测试
    field_6: str | None = None  # 密封等级
    field_7: str | None = None  # 运行状态

class VentFilterEntry(BaseModel):
    """滤毒设备明细结构。"""

    field_0: str | None = None  # 设备编号
    field_1: str | None = None  # 设备型号
    field_2: str | None = None  # 所属工程
    field_3: str | None = None  # 安装位置
    field_4: str | None = None  # 额定风量
    field_5: str | None = None  # 滤毒效率
    field_6: str | None = None  # 上次更换日期
    field_7: str | None = None  # 运行状态

class WaterFireEntry(BaseModel):
    """消防设备明细结构。"""

    field_0: str | None = None  # 设备编号
    field_1: str | None = None  # 设备类型
    field_2: str | None = None  # 所属工程
    field_3: str | None = None  # 安装位置
    field_4: str | None = None  # 规格型号
    field_5: str | None = None  # 上次检测日期
    field_6: str | None = None  # 有效期至
    field_7: str | None = None  # 运行状态

class DrainageEntry(BaseModel):
    """排水泵明细结构。"""

    field_0: str | None = None  # 水泵编号
    field_1: str | None = None  # 水泵型号
    field_2: str | None = None  # 所属工程
    field_3: str | None = None  # 安装位置
    field_4: str | None = None  # 额定流量
    field_5: str | None = None  # 扬程
    field_6: str | None = None  # 上次试运行日期
    field_7: str | None = None  # 运行状态

class LightingEntry(BaseModel):
    """照明设备明细结构。"""

    field_0: str | None = None  # 设备编号
    field_1: str | None = None  # 设备类型
    field_2: str | None = None  # 所属工程
    field_3: str | None = None  # 安装位置
    field_4: str | None = None  # 额定功率
    field_5: str | None = None  # 紧急照明时长
    field_6: str | None = None  # 上次检测日期
    field_7: str | None = None  # 运行状态

class MaintainEntry(BaseModel):
    """保养计划明细结构。"""

    field_0: str | None = None  # 计划编号
    field_1: str | None = None  # 所属工程
    field_2: str | None = None  # 保养类型
    field_3: str | None = None  # 保养项目清单
    field_4: str | None = None  # 计划日期
    field_5: str | None = None  # 保养负责人
    field_6: str | None = None  # 保养单位
    field_7: str | None = None  # 计划状态

class ModifyEntry(BaseModel):
    """改建申请明细结构。"""

    field_0: str | None = None  # 申请编号
    field_1: str | None = None  # 所属工程
    field_2: str | None = None  # 改建内容
    field_3: str | None = None  # 设计单位
    field_4: str | None = None  # 承建单位
    field_5: str | None = None  # 申请日期
    field_6: str | None = None  # 审批人
    field_7: str | None = None  # 审批状态

class FloodEntry(BaseModel):
    """防汛物资明细结构。"""

    field_0: str | None = None  # 物资编号
    field_1: str | None = None  # 物资名称
    field_2: str | None = None  # 所属工程
    field_3: str | None = None  # 存放位置
    field_4: str | None = None  # 规格型号
    field_5: str | None = None  # 现有数量
    field_6: str | None = None  # 上次检查日期
    field_7: str | None = None  # 物资状态

class AirQualityEntry(BaseModel):
    """空气质量记录明细结构。"""

    field_0: str | None = None  # 记录编号
    field_1: str | None = None  # 所属工程
    field_2: str | None = None  # 监测时间
    field_3: str | None = None  # 温度
    field_4: str | None = None  # 湿度
    field_5: str | None = None  # 二氧化碳浓度
    field_6: str | None = None  # 氧气含量
    field_7: str | None = None  # 评定结果

class PowerSupplyEntry(BaseModel):
    """供电设备明细结构。"""

    field_0: str | None = None  # 设备编号
    field_1: str | None = None  # 设备类型
    field_2: str | None = None  # 所属工程
    field_3: str | None = None  # 安装位置
    field_4: str | None = None  # 额定容量
    field_5: str | None = None  # 备电时长
    field_6: str | None = None  # 上次检修日期
    field_7: str | None = None  # 运行状态

class DrillEntry(BaseModel):
    """演练记录明细结构。"""

    field_0: str | None = None  # 演练编号
    field_1: str | None = None  # 所属工程
    field_2: str | None = None  # 演练类型
    field_3: str | None = None  # 参演人数
    field_4: str | None = None  # 演练日期
    field_5: str | None = None  # 转换耗时
    field_6: str | None = None  # 评估结果
    field_7: str | None = None  # 演练状态

class PatrolEntry(BaseModel):
    """巡查记录明细结构。"""

    field_0: str | None = None  # 巡查编号
    field_1: str | None = None  # 所属工程
    field_2: str | None = None  # 巡查人员
    field_3: str | None = None  # 巡查日期
    field_4: str | None = None  # 巡查区域
    field_5: str | None = None  # 发现隐患
    field_6: str | None = None  # 隐患等级
    field_7: str | None = None  # 巡查状态

class EquipmentEntry(BaseModel):
    """防护设备明细结构。"""

    field_0: str | None = None  # 设备编号
    field_1: str | None = None  # 设备名称
    field_2: str | None = None  # 所属工程
    field_3: str | None = None  # 设备类型
    field_4: str | None = None  # 规格型号
    field_5: str | None = None  # 生产厂家
    field_6: str | None = None  # 安装日期
    field_7: str | None = None  # 设备状态

class SignageEntry(BaseModel):
    """标识标牌明细结构。"""

    field_0: str | None = None  # 标牌编号
    field_1: str | None = None  # 标牌类型
    field_2: str | None = None  # 所属工程
    field_3: str | None = None  # 安装位置
    field_4: str | None = None  # 标牌内容
    field_5: str | None = None  # 安装日期
    field_6: str | None = None  # 上次检查日期
    field_7: str | None = None  # 标牌状态
