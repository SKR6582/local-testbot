import subprocess
import sys
import time

subprocess.run(["touch", ".env"])
subprocess.run("echo APIKEY='' > .env", shell=True)
print("t_openai/.env 파일에 \"YOUR_API_KEY\" 를 작성하세요.")
