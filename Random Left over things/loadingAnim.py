import time

def animate_loading_sign(text,delay=0.1):
  loading_chars = ["-", "/", "|", "\\"]
  while True:
    for char in loading_chars:
      print(f"\r{text} {char}", end="")
      time.sleep(delay)
print("Test. ")
# Example usage:

animate_loading_sign("load")