from fastapi import FastAPI
from app.database import Base, engine
from app.routers import user, health
from app.logger import setup_logging
from prometheus_fastapi_instrumentator import Instrumentator


# ロギング設定
setup_logging()

# DB のテーブル作成
Base.metadata.create_all(bind=engine)

# FastAPI インスタンス作成
app = FastAPI(title="FastAPI CRUD App")

# ルーター追加
app.include_router(user.router)
app.include_router(health.router)

# Instrumentator で Prometheus 用のエンドポイントを追加
Instrumentator(
    excluded_handlers=["/metrics"],
).instrument(app).expose(app=app, endpoint="/metrics")

