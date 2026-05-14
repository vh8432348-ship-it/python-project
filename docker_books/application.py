import random
import time

from settings import settings


while True:
    line_length = random.randint(settings.min_len, settings.max_len)

    print(settings.symbol * line_length)

    time.sleep(settings.delay)
