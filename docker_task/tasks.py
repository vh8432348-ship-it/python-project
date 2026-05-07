import time
import platform
import datetime

import pydantic


start_time = datetime.datetime.now()

while True:
    print(f"Python version: {platform.python_version()}")
    print("hello")
    print(f"Pydantic version: {pydantic.__version__}")
    print(f"Program start time: {start_time}")

    print("-" * 30)

    time.sleep(2)
