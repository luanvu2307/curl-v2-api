import logging
import os
from fastapi import FastAPI

from src.curl_impersonate.curl_chrome import call_api_via_curl_v2
from src.utils.basemodel import app_schemas as schemas
from src.utils.basemodel.response_schemas import create_response, ResponseModel


ai_logger = logging.getLogger("ai_logger")
app_logger = logging.getLogger("app_logger")

app = FastAPI(
        title="Curl Impersonate",
        description="Curl Impersonate - Chrome Version.",
        version="0.5.2-alpine"
    )


@app.post("/curl_chrome101", response_model=ResponseModel)
async def predict(input_map: schemas.AISchema) -> ResponseModel:
    response_str, stderr = call_api_via_curl_v2(input_map.proxy, input_map.url, input_map.header)
    result = {
        "stdout": response_str,
        "stderr": stderr
    }
    return create_response(status_code=200, content=result)

if __name__ == '__main__':
        app.run(debug=True, host='0.0.0.0', port=int(os.environ.get('PORT', 2307)))