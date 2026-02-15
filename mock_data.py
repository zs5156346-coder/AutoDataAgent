"""
车企经营管理决策系统 - 模拟数据生成
"""
import random
import uuid
from datetime import datetime, timedelta

random.seed(42)

BRANDS = ["星途", "瑞虎", "艾瑞泽", "捷途", "欧萌达"]
REGIONS = ["华东", "华南", "华北", "西南", "华中", "东北", "西北"]
MONTHS = [f"2025-{str(i).zfill(2)}" for i in range(1, 13)]

# ========== 经营看板数据 ==========

def get_overview_kpis():
    return {
        "revenue": {"value": 4328.5, "unit": "亿元", "yoy": 12.3, "mom": 2.1, "target": 4500, "progress": 96.2},
        "sales_volume": {"value": 186.2, "unit": "万辆", "yoy": 15.7, "mom": 3.4, "target": 200, "progress": 93.1},
        "production_volume": {"value": 192.8, "unit": "万辆", "yoy": 14.2, "mom": 1.8, "target": 195, "progress": 98.9},
        "gross_margin": {"value": 22.6, "unit": "%", "yoy": 1.2, "mom": 0.3, "target": 23, "progress": 98.3},
        "inventory_days": {"value": 38, "unit": "天", "yoy": -5, "mom": -2, "target": 35, "progress": 91.4},
        "market_share": {"value": 8.7, "unit": "%", "yoy": 0.8, "mom": 0.1, "target": 9.0, "progress": 96.7},
        "customer_satisfaction": {"value": 92.3, "unit": "分", "yoy": 2.1, "mom": 0.5, "target": 95, "progress": 97.2},
        "nev_penetration": {"value": 56.8, "unit": "%", "yoy": 12.5, "mom": 1.2, "target": 60, "progress": 94.7},
    }


def get_monthly_trends():
    base_revenue = [320, 285, 340, 365, 380, 395, 358, 372, 388, 405, 420, 438]
    base_sales = [14.2, 12.8, 15.1, 16.3, 17.0, 17.5, 15.8, 16.5, 17.2, 18.0, 18.8, 19.5]
    base_production = [15.0, 13.5, 15.8, 16.8, 17.5, 18.0, 16.5, 17.0, 17.8, 18.5, 19.2, 20.0]
    base_margin = [21.2, 20.8, 21.5, 22.0, 22.3, 22.8, 21.8, 22.1, 22.5, 22.8, 23.1, 23.5]

    return {
        "months": MONTHS,
        "revenue": [round(v + random.uniform(-10, 10), 1) for v in base_revenue],
        "sales_volume": [round(v + random.uniform(-0.5, 0.5), 1) for v in base_sales],
        "production_volume": [round(v + random.uniform(-0.5, 0.5), 1) for v in base_production],
        "gross_margin": [round(v + random.uniform(-0.3, 0.3), 1) for v in base_margin],
    }


def get_brand_analysis():
    data = []
    brand_sales = [62.5, 45.2, 38.6, 28.4, 11.5]
    brand_revenue = [1520, 980, 850, 620, 358]
    for i, brand in enumerate(BRANDS):
        data.append({
            "brand": brand,
            "sales_volume": brand_sales[i],
            "revenue": brand_revenue[i],
            "yoy_growth": round(random.uniform(5, 25), 1),
            "market_share": round(brand_sales[i] / 186.2 * 100, 1),
            "gross_margin": round(random.uniform(18, 28), 1),
            "inventory_days": random.randint(25, 50),
        })
    return data


def get_regional_data():
    data = []
    region_sales = [52.3, 38.7, 35.2, 25.6, 18.4, 10.2, 5.8]
    for i, region in enumerate(REGIONS):
        data.append({
            "region": region,
            "sales_volume": region_sales[i],
            "revenue": round(region_sales[i] * 23.2 + random.uniform(-50, 50), 1),
            "yoy_growth": round(random.uniform(-5, 30), 1),
            "dealer_count": random.randint(80, 350),
            "satisfaction": round(random.uniform(88, 96), 1),
        })
    return data


# ========== 预警系统数据 ==========

WARNING_TYPES = [
    {"code": "SALES", "name": "销量预警", "icon": "chart-bar"},
    {"code": "INVENTORY", "name": "库存预警", "icon": "archive"},
    {"code": "PROFIT", "name": "利润预警", "icon": "currency-yen"},
    {"code": "QUALITY", "name": "质量预警", "icon": "shield-check"},
    {"code": "SUPPLY", "name": "供应链预警", "icon": "truck"},
]

_warnings_store = []

def _generate_warnings():
    global _warnings_store
    warnings = [
        {
            "id": "W20250201",
            "type": "SALES",
            "type_name": "销量预警",
            "severity": "high",
            "title": "星途品牌华北区销量连续3月下滑",
            "description": "星途品牌在华北区域2025年Q4销量环比持续下降，10月-12月分别下滑3.2%、5.1%、7.8%，累计偏离目标18.6%。",
            "metric": "月销量",
            "current_value": "3,280辆",
            "threshold": "4,000辆",
            "deviation": "-18.0%",
            "affected_region": "华北",
            "affected_brand": "星途",
            "created_at": "2025-12-15 09:30:00",
            "status": "active",
            "acknowledged": False,
        },
        {
            "id": "W20250202",
            "type": "INVENTORY",
            "type_name": "库存预警",
            "severity": "critical",
            "title": "瑞虎系列库存周转天数超标",
            "description": "瑞虎系列全国库存周转天数达到52天，超过警戒线(45天)，华东区尤为严重达到61天。需立即采取促销或减产措施。",
            "metric": "库存周转天数",
            "current_value": "52天",
            "threshold": "45天",
            "deviation": "+15.6%",
            "affected_region": "全国",
            "affected_brand": "瑞虎",
            "created_at": "2025-12-14 14:22:00",
            "status": "active",
            "acknowledged": True,
        },
        {
            "id": "W20250203",
            "type": "PROFIT",
            "type_name": "利润预警",
            "severity": "medium",
            "title": "艾瑞泽品牌毛利率持续走低",
            "description": "艾瑞泽品牌毛利率从年初的23.5%下降至当前的19.2%，主要受原材料成本上涨和终端价格竞争影响。",
            "metric": "毛利率",
            "current_value": "19.2%",
            "threshold": "20.0%",
            "deviation": "-4.0%",
            "affected_region": "全国",
            "affected_brand": "艾瑞泽",
            "created_at": "2025-12-13 11:15:00",
            "status": "active",
            "acknowledged": False,
        },
        {
            "id": "W20250204",
            "type": "QUALITY",
            "type_name": "质量预警",
            "severity": "high",
            "title": "捷途X70千车故障率异常升高",
            "description": "捷途X70近3个月千车故障率(PPH)从12.5上升至18.3，主要集中在变速箱异响和电子系统故障。",
            "metric": "千车故障率(PPH)",
            "current_value": "18.3",
            "threshold": "15.0",
            "deviation": "+22.0%",
            "affected_region": "全国",
            "affected_brand": "捷途",
            "created_at": "2025-12-12 16:45:00",
            "status": "active",
            "acknowledged": True,
        },
        {
            "id": "W20250205",
            "type": "SUPPLY",
            "type_name": "供应链预警",
            "severity": "critical",
            "title": "芯片供应商交付延迟风险",
            "description": "主力芯片供应商(瑞萨电子)通知Q1产能下调15%，预计影响1月份整车产量约8,000辆。需启动备选供应商切换方案。",
            "metric": "供应保障率",
            "current_value": "82%",
            "threshold": "95%",
            "deviation": "-13.7%",
            "affected_region": "全国",
            "affected_brand": "全品牌",
            "created_at": "2025-12-11 10:00:00",
            "status": "active",
            "acknowledged": False,
        },
        {
            "id": "W20250206",
            "type": "SALES",
            "type_name": "销量预警",
            "severity": "medium",
            "title": "欧萌达新能源车型市占率下降",
            "description": "欧萌达新能源车型市场占有率从3.2%下降至2.5%，竞品比亚迪、吉利新车型分流明显。",
            "metric": "市场占有率",
            "current_value": "2.5%",
            "threshold": "3.0%",
            "deviation": "-16.7%",
            "affected_region": "全国",
            "affected_brand": "欧萌达",
            "created_at": "2025-12-10 08:30:00",
            "status": "resolved",
            "acknowledged": True,
        },
        {
            "id": "W20250207",
            "type": "INVENTORY",
            "type_name": "库存预警",
            "severity": "low",
            "title": "西南区艾瑞泽库存偏低",
            "description": "西南区艾瑞泽系列库存深度仅为0.8个月，低于安全库存1.2个月，存在断供风险。",
            "metric": "库存深度",
            "current_value": "0.8个月",
            "threshold": "1.2个月",
            "deviation": "-33.3%",
            "affected_region": "西南",
            "affected_brand": "艾瑞泽",
            "created_at": "2025-12-09 15:20:00",
            "status": "active",
            "acknowledged": False,
        },
        {
            "id": "W20250208",
            "type": "PROFIT",
            "type_name": "利润预警",
            "severity": "high",
            "title": "终端优惠幅度超出预算",
            "description": "12月全品牌平均终端优惠达到1.8万元/辆，超出预算(1.5万元/辆)20%，预计影响当月利润约2.3亿元。",
            "metric": "单车优惠额",
            "current_value": "1.8万元",
            "threshold": "1.5万元",
            "deviation": "+20.0%",
            "affected_region": "全国",
            "affected_brand": "全品牌",
            "created_at": "2025-12-08 09:10:00",
            "status": "active",
            "acknowledged": True,
        },
    ]
    _warnings_store = warnings
    return warnings


def get_warnings(severity=None, warning_type=None, status=None):
    if not _warnings_store:
        _generate_warnings()
    result = _warnings_store[:]
    if severity:
        result = [w for w in result if w["severity"] == severity]
    if warning_type:
        result = [w for w in result if w["type"] == warning_type]
    if status:
        result = [w for w in result if w["status"] == status]
    return result


def get_warning_stats():
    if not _warnings_store:
        _generate_warnings()
    total = len(_warnings_store)
    active = len([w for w in _warnings_store if w["status"] == "active"])
    critical = len([w for w in _warnings_store if w["severity"] == "critical" and w["status"] == "active"])
    high = len([w for w in _warnings_store if w["severity"] == "high" and w["status"] == "active"])
    return {"total": total, "active": active, "critical": critical, "high": high, "resolved": total - active}


# ========== AI 诊断数据 ==========

DIAGNOSIS_TEMPLATES = {
    "sales_decline": {
        "title": "销量下滑根因分析",
        "summary": "经AI多维度分析，星途品牌华北区销量下滑主要由以下因素驱动：",
        "root_causes": [
            {"factor": "竞品冲击", "weight": 35, "detail": "比亚迪宋Pro、吉利银河L7在同价位区间推出高性价比车型，分流了约35%的潜在客户"},
            {"factor": "终端执行力不足", "weight": 25, "detail": "华北区经销商网络覆盖密度低于竞品，北京、天津核心商圈展厅进店量下降22%"},
            {"factor": "产品竞争力下降", "weight": 20, "detail": "星途揽月、追风等主力车型上市已超18个月未改款，智能化配置落后于竞品"},
            {"factor": "季节性因素", "weight": 12, "detail": "Q4为传统购车旺季，但今年消费信心指数偏低，购车决策周期延长"},
            {"factor": "营销投放不足", "weight": 8, "detail": "华北区线上营销预算同比减少15%，线索获取成本上升23%"},
        ],
        "recommendations": [
            {"priority": "高", "action": "加速星途揽月中期改款上市，重点强化智能驾驶和座舱配置"},
            {"priority": "高", "action": "华北区增加20家二网覆盖，重点布局三四线城市"},
            {"priority": "中", "action": "推出限时金融补贴方案，降低购车门槛"},
            {"priority": "中", "action": "加大华北区短视频和直播带货投入，预算增加30%"},
            {"priority": "低", "action": "建立竞品动态监控机制，每周输出竞品价格和政策变动报告"},
        ],
        "predicted_impact": "预计采取上述措施后，华北区销量将在2-3个月内恢复至目标水平的90%以上",
        "confidence": 87,
    },
    "inventory_excess": {
        "title": "库存积压根因分析",
        "summary": "瑞虎系列库存周转异常的核心驱动因素分析如下：",
        "root_causes": [
            {"factor": "产销不匹配", "weight": 40, "detail": "Q4生产计划未根据市场需求及时调整，瑞虎8 Pro产量超出需求约2,500辆/月"},
            {"factor": "区域分布不均", "weight": 25, "detail": "华东区库存占全国42%，但销量仅占28%，存在严重的区域库存错配"},
            {"factor": "老款车型滞销", "weight": 20, "detail": "2024款瑞虎7库存占比达35%，新老款切换期间去化速度低于预期"},
            {"factor": "经销商信心不足", "weight": 15, "detail": "部分经销商因盈利压力主动控制进货量，导致库存集中在主机厂端"},
        ],
        "recommendations": [
            {"priority": "高", "action": "立即下调瑞虎8 Pro 1月产量15%，同步启动华东区向西南、西北区的库存调拨"},
            {"priority": "高", "action": "针对2024款瑞虎7推出清库专项政策，终端补贴增加5,000元/辆"},
            {"priority": "中", "action": "优化DMS系统库存预警算法，实现区域间智能调拨建议"},
            {"priority": "低", "action": "建立月度产销联席会议机制，提升需求预测准确率"},
        ],
        "predicted_impact": "预计30天内库存周转天数可降至45天以内，60天内恢复至正常水平(35天)",
        "confidence": 92,
    },
    "profit_decline": {
        "title": "利润下滑根因分析",
        "summary": "艾瑞泽品牌毛利率下降的多因素归因分析：",
        "root_causes": [
            {"factor": "原材料成本上涨", "weight": 30, "detail": "碳酸锂价格Q4反弹18%，电池包成本上升约3,200元/辆；钢材价格同比上涨8%"},
            {"factor": "价格战影响", "weight": 30, "detail": "为应对比亚迪秦Plus降价，艾瑞泽5终端指导价下调8,000元，直接侵蚀毛利"},
            {"factor": "产能利用率不足", "weight": 22, "detail": "芜湖工厂产能利用率仅72%，固定成本分摊导致单车制造成本偏高"},
            {"factor": "售后收入下降", "weight": 18, "detail": "新能源车型占比提升后，保养收入和配件收入同比下降12%"},
        ],
        "recommendations": [
            {"priority": "高", "action": "启动电池供应商谈判，争取Q1锁价协议，目标降本3%-5%"},
            {"priority": "高", "action": "推动艾瑞泽平台零部件通用化率提升至75%，降低采购成本"},
            {"priority": "中", "action": "调整产品结构，增加高配车型占比，提升单车利润"},
            {"priority": "中", "action": "拓展汽车金融和延保业务，增加高毛利后市场收入"},
        ],
        "predicted_impact": "综合措施实施后，预计Q2毛利率可回升至21%以上",
        "confidence": 78,
    },
}


def get_ai_diagnosis(indicator_type: str):
    mapping = {
        "sales_decline": "sales_decline",
        "inventory_excess": "inventory_excess",
        "profit_decline": "profit_decline",
    }
    template_key = mapping.get(indicator_type, "sales_decline")
    return DIAGNOSIS_TEMPLATES[template_key]


# ========== 问题跟踪数据 ==========

_issues_store = []

def _generate_issues():
    global _issues_store
    issues = [
        {
            "id": "ISS-2025-001",
            "title": "华北区星途销量恢复专项",
            "source_warning": "W20250201",
            "status": "in_progress",
            "priority": "high",
            "owner": "张明 (华北区总经理)",
            "department": "销售管理部",
            "created_at": "2025-12-15 10:00:00",
            "due_date": "2026-02-28",
            "progress": 35,
            "description": "针对星途品牌华北区销量连续下滑问题，制定并执行恢复计划",
            "action_items": [
                {"task": "完成华北区经销商走访和问题诊断", "status": "completed", "due": "2025-12-25"},
                {"task": "制定Q1销量恢复专项方案", "status": "completed", "due": "2025-12-30"},
                {"task": "落实二网扩展计划(新增20家)", "status": "in_progress", "due": "2026-01-31"},
                {"task": "启动限时金融补贴活动", "status": "in_progress", "due": "2026-01-15"},
                {"task": "月度效果评估和方案迭代", "status": "pending", "due": "2026-02-28"},
            ],
            "timeline": [
                {"time": "2025-12-15 10:00", "event": "问题工单创建", "user": "系统", "type": "create"},
                {"time": "2025-12-15 14:30", "event": "指派给张明(华北区总经理)", "user": "李总", "type": "assign"},
                {"time": "2025-12-20 09:00", "event": "添加评论: 已启动经销商走访，预计12月25日前完成", "user": "张明", "type": "comment"},
                {"time": "2025-12-26 16:00", "event": "完成经销商走访，发现3家经销商运营存在严重问题", "user": "张明", "type": "update"},
                {"time": "2025-12-30 11:00", "event": "Q1恢复方案已提交审批", "user": "张明", "type": "update"},
                {"time": "2026-01-03 09:30", "event": "方案审批通过，开始执行", "user": "李总", "type": "approve"},
            ],
        },
        {
            "id": "ISS-2025-002",
            "title": "瑞虎系列库存专项治理",
            "source_warning": "W20250202",
            "status": "in_progress",
            "priority": "critical",
            "owner": "王芳 (供应链总监)",
            "department": "供应链管理部",
            "created_at": "2025-12-14 15:00:00",
            "due_date": "2026-01-31",
            "progress": 55,
            "description": "瑞虎系列库存周转天数超标，需快速降库存至安全水位",
            "action_items": [
                {"task": "完成全国库存盘点和区域分布分析", "status": "completed", "due": "2025-12-18"},
                {"task": "制定华东区库存调拨方案", "status": "completed", "due": "2025-12-20"},
                {"task": "下调1月瑞虎8 Pro产量计划", "status": "completed", "due": "2025-12-22"},
                {"task": "执行2024款瑞虎7清库政策", "status": "in_progress", "due": "2026-01-15"},
                {"task": "库存恢复至目标水位", "status": "pending", "due": "2026-01-31"},
            ],
            "timeline": [
                {"time": "2025-12-14 15:00", "event": "问题工单创建(系统自动)", "user": "系统", "type": "create"},
                {"time": "2025-12-14 16:00", "event": "升级为紧急工单", "user": "系统", "type": "escalate"},
                {"time": "2025-12-15 09:00", "event": "指派给王芳(供应链总监)", "user": "刘副总", "type": "assign"},
                {"time": "2025-12-18 17:00", "event": "库存盘点完成，华东占比42%严重超标", "user": "王芳", "type": "update"},
                {"time": "2025-12-20 10:00", "event": "调拨方案已制定: 华东→西南800辆，华东→西北500辆", "user": "王芳", "type": "update"},
                {"time": "2025-12-22 14:00", "event": "1月产量计划已下调15%，获批执行", "user": "王芳", "type": "update"},
                {"time": "2025-12-28 09:00", "event": "库存调拨已启动物流，预计1月5日到达", "user": "物流部", "type": "update"},
            ],
        },
        {
            "id": "ISS-2025-003",
            "title": "捷途X70质量问题整改",
            "source_warning": "W20250204",
            "status": "in_progress",
            "priority": "high",
            "owner": "陈刚 (质量总监)",
            "department": "质量管理部",
            "created_at": "2025-12-12 17:00:00",
            "due_date": "2026-03-15",
            "progress": 25,
            "description": "捷途X70千车故障率异常升高，需进行质量整改",
            "action_items": [
                {"task": "完成故障数据采集和Top问题分析", "status": "completed", "due": "2025-12-18"},
                {"task": "供应商质量审核(变速箱+电子系统)", "status": "in_progress", "due": "2026-01-10"},
                {"task": "制定并实施纠正措施", "status": "pending", "due": "2026-02-15"},
                {"task": "验证改进效果(PPH降至15以下)", "status": "pending", "due": "2026-03-15"},
            ],
            "timeline": [
                {"time": "2025-12-12 17:00", "event": "问题工单创建", "user": "系统", "type": "create"},
                {"time": "2025-12-13 09:00", "event": "指派给陈刚(质量总监)", "user": "李总", "type": "assign"},
                {"time": "2025-12-18 16:00", "event": "Top3故障模式已确认: 变速箱异响(38%)、中控死机(25%)、电动尾门故障(18%)", "user": "陈刚", "type": "update"},
            ],
        },
        {
            "id": "ISS-2025-004",
            "title": "芯片供应替代方案落地",
            "source_warning": "W20250205",
            "status": "pending",
            "priority": "critical",
            "owner": "赵伟 (采购总监)",
            "department": "采购部",
            "created_at": "2025-12-11 10:30:00",
            "due_date": "2026-01-15",
            "progress": 10,
            "description": "应对瑞萨芯片供应缩减，启动备选供应商方案",
            "action_items": [
                {"task": "评估瑞萨产能缩减对各车型的影响", "status": "completed", "due": "2025-12-13"},
                {"task": "筛选并联系备选芯片供应商", "status": "in_progress", "due": "2025-12-20"},
                {"task": "完成备选芯片验证测试", "status": "pending", "due": "2026-01-05"},
                {"task": "签订备选供应合同并切换产线", "status": "pending", "due": "2026-01-15"},
            ],
            "timeline": [
                {"time": "2025-12-11 10:30", "event": "问题工单创建(紧急)", "user": "系统", "type": "create"},
                {"time": "2025-12-11 11:00", "event": "指派给赵伟(采购总监)", "user": "刘副总", "type": "assign"},
                {"time": "2025-12-13 14:00", "event": "影响评估完成: 预计影响1月星途+瑞虎产量共8,000辆", "user": "赵伟", "type": "update"},
            ],
        },
        {
            "id": "ISS-2025-005",
            "title": "艾瑞泽毛利率改善计划",
            "source_warning": "W20250203",
            "status": "completed",
            "priority": "medium",
            "owner": "孙丽 (财务总监)",
            "department": "财务部",
            "created_at": "2025-12-13 12:00:00",
            "due_date": "2026-03-31",
            "progress": 100,
            "description": "制定艾瑞泽品牌毛利率改善方案",
            "action_items": [
                {"task": "完成成本分解和对标分析", "status": "completed", "due": "2025-12-20"},
                {"task": "制定降本增效方案", "status": "completed", "due": "2025-12-28"},
                {"task": "方案审批通过", "status": "completed", "due": "2026-01-05"},
            ],
            "timeline": [
                {"time": "2025-12-13 12:00", "event": "问题工单创建", "user": "系统", "type": "create"},
                {"time": "2025-12-13 14:00", "event": "指派给孙丽(财务总监)", "user": "李总", "type": "assign"},
                {"time": "2025-12-20 11:00", "event": "成本分析完成，识别5项主要降本空间", "user": "孙丽", "type": "update"},
                {"time": "2025-12-28 15:00", "event": "降本方案制定完成，预计可提升毛利率1.8个百分点", "user": "孙丽", "type": "update"},
                {"time": "2026-01-05 10:00", "event": "方案获总经理办公会审批通过", "user": "李总", "type": "approve"},
                {"time": "2026-01-05 10:30", "event": "工单关闭", "user": "系统", "type": "close"},
            ],
        },
    ]
    _issues_store = issues
    return issues


def get_issues(status=None, priority=None):
    if not _issues_store:
        _generate_issues()
    result = _issues_store[:]
    if status:
        result = [i for i in result if i["status"] == status]
    if priority:
        result = [i for i in result if i["priority"] == priority]
    return result


def get_issue_detail(issue_id: str):
    if not _issues_store:
        _generate_issues()
    for issue in _issues_store:
        if issue["id"] == issue_id:
            return issue
    return None


def get_issue_stats():
    if not _issues_store:
        _generate_issues()
    total = len(_issues_store)
    pending = len([i for i in _issues_store if i["status"] == "pending"])
    in_progress = len([i for i in _issues_store if i["status"] == "in_progress"])
    completed = len([i for i in _issues_store if i["status"] == "completed"])
    critical = len([i for i in _issues_store if i["priority"] == "critical"])
    overdue = 1  # mock
    return {
        "total": total, "pending": pending, "in_progress": in_progress,
        "completed": completed, "critical": critical, "overdue": overdue,
    }
