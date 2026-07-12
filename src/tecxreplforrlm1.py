import code
import sys
import io

print("1. Running original primary script code standard routines...")

# Define the exact terminal commands you want to execute inside the REPL automatically.
# Crucial Step: The last line must be 'exit()' or 'quit()' followed by a newline!
repl_commands = """
print('-> Successfully automated inside the REPL namespace!')
x = 100 + 200
print(f'-> Value calculated inside REPL: {x}')
exit()
\n"""

# Backup your live terminal keyboard input stream
original_stdin = sys.stdin

try:
    # Redirect stdin to read directly from our pre-written string command block
    sys.stdin = io.StringIO(repl_commands)
    
    # Launch the code interactive console namespace
    code.interact(local=locals())

finally:
    # Restore your terminal keyboard input stream so the rest of your script behaves normally
    sys.stdin = original_stdin

print("2. Successfully returned back to original python code layout seamlessly!")

