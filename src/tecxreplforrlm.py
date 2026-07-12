import code

class AutomatedConsole(code.InteractiveConsole):
    def raw_input(self, prompt=""):
        # Call the normal prompt loop line
        try:
            line = super().raw_input(prompt)
        except EOFError:
            return ""
            
        # AUTOMATION CRITERIA:
        # If the user types 'done', we intercept it and simulate a clean Ctrl+D (EOFError)
        # to cleanly step backwards in the stack instead of crashing via exit()
        if line.strip().lower() == 'done':
            raise EOFError
            
        return line

print("1. Initializing original code execution paths...")

# Launch your custom console engine instance
console = AutomatedConsole(locals())
print("💡 TYPE 'done' TO AUTOMATICALLY EXIT AND CONTINUE SCRIPT RUNS")
console.interact(banner="--- ENTERING REPL MODE ---")

print("2. Clean escape achieved! Resuming normal program execution sequence.")

