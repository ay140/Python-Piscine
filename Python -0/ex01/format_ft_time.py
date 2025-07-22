import time  # We use only the time module

def main():
    """
    Display the number of seconds since the Epoch (Jan 1, 1970)
    in both decimal and scientific notation, followed by current date.
    """

    now = time.time()
    # Get the current time in seconds since Jan 1, 1970 (Epoch time).
    # Example: 1696590902.9453

    print(f"Seconds since January 1, 1970: {now:,.4f} or {now:.2e} in scientific notation")    # Format the time in two ways:
    # - {now:.4f} → fixed-point notation with 4 decimal places (e.g., 1696590902.9453)
    # - {now:.2e} → scientific notation with 2 decimal places (e.g., 1.70e+09)

    print(time.strftime("%b %d %Y", time.localtime(now)))
    # Convert the timestamp to a human-readable date:
    # - %b = abbreviated month name (e.g., Oct)
    # - %d = day of the month (e.g., 06)
    # - %Y = full year (e.g., 2023)
    # Final output: Oct 06 2023

if __name__ == "__main__":
    main()
    # This ensures that the main() function runs only if the script is executed directly.
# 🕰️ What does epoch mean?
# In computing, epoch refers to a fixed point in time that computers use as a reference to calculate time.

# For most systems, especially Unix-based ones (like Linux, macOS, and even Python), the epoch is set to:

# January 1st, 1970, 00:00:00 UTC
# This date is known as the Unix Epoch. Time is counted as the number of seconds since that exact moment.
