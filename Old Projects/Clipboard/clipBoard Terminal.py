import pyperclip
import os
history = ['']
n = 0

def clear_screen():
  """Clears the terminal screen."""
  os.system('cls' if os.name == 'nt' else 'clear')


while True:
   try:
      lastPasted = pyperclip.paste()
      if lastPasted == history[-1]:
         pass
      else:
         history.append(lastPasted)
         if history[0] == '': 
            del history[0]
         clear_screen()
         print(history)
   except KeyboardInterrupt:
      print("interuput called")
      user_input = input("Enter a command (e.g., 'clear'): ")
      if user_input == 'clear' or user_input == 'cls':
         history = ['']
         print("Cleared!")
      else:
         pass



    