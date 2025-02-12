import logging
import os
import sys

LOG_DIR = "/app/logs"
LOG_FILE = os.path.join(LOG_DIR, "app.log")
logger = logging.getLogger()

def setup_logging():
    # ログ保存用のディレクトリを作成
    os.makedirs(LOG_DIR, exist_ok=True)

    # ロガーの設定
    logging.basicConfig(
        level=logging.DEBUG,
        format="%(asctime)s - %(name)s - %(levelname)s - %(message)s",
        handlers=[
            logging.FileHandler(LOG_FILE),  # ファイル出力
            logging.StreamHandler(sys.stdout)         # コンソール出力
        ]
    )

    logger.info("Logging is set up.")
