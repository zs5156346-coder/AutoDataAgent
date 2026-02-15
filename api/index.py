"""
Vercel Serverless 入口 - 包装 FastAPI 应用
"""
import os
import sys

# 确保项目根目录在 Python 路径中
ROOT_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
sys.path.insert(0, ROOT_DIR)

from fastapi import FastAPI, Query
from fastapi.staticfiles import StaticFiles
from fastapi.responses import FileResponse, HTMLResponse
from typing import Optional

from mock_data import (
    get_overview_kpis, get_monthly_trends, get_brand_analysis, get_regional_data,
    get_warnings, get_warning_stats, WARNING_TYPES,
    get_ai_diagnosis,
    get_issues, get_issue_detail, get_issue_stats,
)

app = FastAPI(title="车企经营管理决策系统", version="1.0.0")

STATIC_DIR = os.path.join(ROOT_DIR, "static")


# ==================== 经营看板 API ====================

@app.get("/api/dashboard/overview")
async def dashboard_overview():
    return {"code": 0, "data": get_overview_kpis()}


@app.get("/api/dashboard/trends")
async def dashboard_trends():
    return {"code": 0, "data": get_monthly_trends()}


@app.get("/api/dashboard/brands")
async def dashboard_brands():
    return {"code": 0, "data": get_brand_analysis()}


@app.get("/api/dashboard/regions")
async def dashboard_regions():
    return {"code": 0, "data": get_regional_data()}


# ==================== 预警系统 API ====================

@app.get("/api/warnings")
async def list_warnings(
    severity: Optional[str] = Query(None),
    type: Optional[str] = Query(None),
    status: Optional[str] = Query(None),
):
    return {"code": 0, "data": get_warnings(severity, type, status)}


@app.get("/api/warnings/stats")
async def warning_stats():
    return {"code": 0, "data": get_warning_stats()}


@app.get("/api/warnings/types")
async def warning_types():
    return {"code": 0, "data": WARNING_TYPES}


@app.post("/api/warnings/{warning_id}/acknowledge")
async def acknowledge_warning(warning_id: str):
    return {"code": 0, "message": "预警已确认"}


# ==================== AI 诊断 API ====================

@app.post("/api/diagnosis/analyze")
async def run_diagnosis(body: dict):
    indicator_type = body.get("indicator_type", "sales_decline")
    return {"code": 0, "data": get_ai_diagnosis(indicator_type)}


@app.get("/api/diagnosis/types")
async def diagnosis_types():
    return {
        "code": 0,
        "data": [
            {"key": "sales_decline", "label": "销量下滑分析", "icon": "trending-down"},
            {"key": "inventory_excess", "label": "库存积压分析", "icon": "archive"},
            {"key": "profit_decline", "label": "利润下滑分析", "icon": "dollar-sign"},
        ],
    }


# ==================== 问题跟踪 API ====================

@app.get("/api/issues")
async def list_issues(
    status: Optional[str] = Query(None),
    priority: Optional[str] = Query(None),
):
    return {"code": 0, "data": get_issues(status, priority)}


@app.get("/api/issues/stats")
async def issue_stats():
    return {"code": 0, "data": get_issue_stats()}


@app.get("/api/issues/{issue_id}")
async def issue_detail(issue_id: str):
    detail = get_issue_detail(issue_id)
    if detail:
        return {"code": 0, "data": detail}
    return {"code": 404, "message": "问题不存在"}


# ==================== 静态文件 & 首页 ====================

@app.get("/static/{file_path:path}")
async def serve_static(file_path: str):
    full_path = os.path.join(STATIC_DIR, file_path)
    if os.path.isfile(full_path):
        return FileResponse(full_path)
    return {"code": 404, "message": "文件不存在"}


@app.get("/")
async def index():
    index_path = os.path.join(STATIC_DIR, "index.html")
    return FileResponse(index_path)
