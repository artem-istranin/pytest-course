import logging
import os
import time

from fastapi import FastAPI, UploadFile, File

app = FastAPI()

logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)


@app.get("/user/{user_id}/profile")
def user_profile(user_id: int):
    return {"user_id": user_id, "profile": "UserProfileData"}


@app.get("/user/{user_id}/files")
def user_files(user_id: int):
    return {"user_id": user_id, "files": ["file1.txt", "file2.txt"]}


@app.post("/user/{user_id}/file")
async def upload_file(user_id: int, file: UploadFile = File(...)):
    contents = await file.read()
    logger.info(f"Received file: {file.filename} from user {user_id}")
    return {
        "user_id": user_id,
        "filename": file.filename,
        "content": contents.decode()
    }


@app.get("/analytics/sales")
def analytics_sales():
    process_request_context()
    is_sales_db_enabled = os.environ.get("SALES_DB_ENABLED", "true").lower() in ['true', 'yes', '1']

    if is_sales_db_enabled:
        try:
            sales_data = {"sales": fetch_sales_from_db()}
        except RuntimeError:
            sales_data = {"sales": "sales_data_not_available"}
    else:
        sales_data = {"sales": "sales_db_disabled"}

    return sales_data


def fetch_sales_from_db() -> float:
    # Simulate a DB call (external API request)
    time.sleep(3)
    return 1000


@app.get("/analytics/stock")
def analytics_stock():
    process_request_context()
    return {"stock": 42}


def process_request_context():
    time.sleep(1)


if __name__ == "__main__":
    import uvicorn

    uvicorn.run("main:app", host="127.0.0.1", port=8000, reload=True)
