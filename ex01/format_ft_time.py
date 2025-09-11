#! /usr/bin/env python3

import time

actual_time = time.time()

print("Seconds since January 1, 1970: " + f"{actual_time:,.4f}" +" or " f"{actual_time:.2e}" + " in scientific notation")
print(time.strftime("%b %d %Y", time.localtime()))