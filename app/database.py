from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker
import os
from dotenv import load_dotenv
from app.logger import logger

# 環境変数読み込み
load_dotenv()

DATABASE_URL = os.getenv("DATABASE_URL")

# SQLAlchemy のエンジン作成
engine = create_engine(DATABASE_URL)

# セッション作成
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

# ベースクラス
Base = declarative_base()

logger.info("DB is set up.")
