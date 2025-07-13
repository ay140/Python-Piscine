import time # module to get the current time in seconds since the epoch
from datetime import datetime # import the datetime class from the datetime module

epoch_time = time.time() # get the current time in seconds since the epoch
print(f"Seconds since January 1, 1970: {epoch_time:.4f} or {epoch_time:.2e}") # print the time in seconds or in scientific notation
print(datetime.fromtimestamp(epoch_time).strftime('%b %d %Y')) # print the time in the format of month day year

# %b → Short month name (e.g. Jul)

# %d → Day of the month (e.g. 13)

# %Y → Year (e.g. 2025)


# 🕰️ What does epoch mean?
# In computing, epoch refers to a fixed point in time that computers use as a reference to calculate time.

# For most systems, especially Unix-based ones (like Linux, macOS, and even Python), the epoch is set to:

# January 1st, 1970, 00:00:00 UTC
# This date is known as the Unix Epoch. Time is counted as the number of seconds since that exact moment.
