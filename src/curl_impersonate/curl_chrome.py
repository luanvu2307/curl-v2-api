import shlex
import subprocess


def call_api_via_curl_v2(proxy: str, url: str, header: str) -> dict[str]:
    cmd = f'''curl_chrome101 -x {proxy} -L {url} {header}'''
    args = shlex.split(cmd)
    process = subprocess.Popen(args, shell=False, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
    stdout, stderr = process.communicate()
    stdout_str = stdout.decode("utf-8")
    return stdout_str, stderr
