import shlex
import subprocess
import logging
import google.cloud.logging
import time


client = google.cloud.logging.Client()
service_key_path = 'luan-vu-service-account-brand-insight-testing-816c333cc0be.json'
client = google.cloud.logging.Client().from_service_account_json(service_key_path)
client.setup_logging()


def call_api_via_curl_v2(proxy: str, url: str, header: str) -> dict[str]:
    cmd = f'''curl_chrome101 -x {proxy} -L {url} {header}'''
    s = time.time()
    args = shlex.split(cmd)
    logging.info(f"Time of split cmd with shlex lib: {time.time()-s} sec")
    s = time.time()
    process = subprocess.Popen(
        args, shell=False, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
    stdout, stderr = process.communicate()
    logging.info(f"Time of process and communicate to get stdout, stderr: {time.time()-s} sec")
    s = time.time()
    stdout_str = stdout.decode("utf-8")
    logging.info(f"Time of decoding stdout to stdout_str: {time.time()-s} sec")
    return stdout_str, stderr
