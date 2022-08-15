import logging
import google.cloud.logging
import os
import time
from fastapi import FastAPI
from src.curl_impersonate.curl_chrome import call_api_via_curl_v2
from src.utils.basemodel import app_schemas as schemas
from src.utils.basemodel.response_schemas import create_response, ResponseModel


client = google.cloud.logging.Client()
service_key_path = 'luan-vu-service-account-brand-insight-testing-816c333cc0be.json'
client = google.cloud.logging.Client().from_service_account_json(service_key_path)
client.setup_logging()

app = FastAPI(
    title="Curl Impersonate",
    description="Curl Impersonate - Chrome Version.",
    version="0.5.2-alpine"
)


@app.post("/curl_chrome101", response_model=ResponseModel)
async def predict(input_map: schemas.AISchema) -> ResponseModel:
    s = time.time()
    logging.info('Start to execute curl v2')
    response_str, stderr = call_api_via_curl_v2(
        input_map.proxy, input_map.url, input_map.header)
    logging.info(f'Takes {time.time()- s} sec to finish curl api')
    result = {
        "stdout": response_str,
        "stderr": stderr
    }
    return create_response(status_code=200, content=result)

if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0', port=int(os.environ.get('PORT', 2307)))
