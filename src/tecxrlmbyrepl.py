"""
In the context of the Recursive Language Model (RLM) paradigm, the REPL is actually the core engine rather than just a feature. 
Instead of cramming a massive, long-context document directly into an LLM, the RLM architecture holds the document as a variable inside a programmatic REPL environment (like a hidden Python sandbox). 
The model then writes and runs Python code inside that REPL to slice, search, and analyze the data iteratively.
If you want to implement or add a REPL environment to an RLM model, you can either install the standard plug-and-play RLM library or build a lightweight RLM orchestrator framework yourself.

#

Method 1: Use the Official rlms Library (Easiest)An open-source Python library makes deploying an RLM loop incredibly straightforward. It natively pairs the LLM API with an underlying REPL instance.
Install the package:
"""

# pip install rlms

"""
Initialize the model with a REPL backend:You can instantiate an RLM object, choosing standard environments like local or ipython:
"""

from rlm import RLM

# Automatically attaches a persistent Python REPL engine to the model
rlm = RLM(
    backend="openai",
    backend_kwargs={"model_name": "gpt-5-nano"},
    environment="local", # or "ipython", "docker", "e2b"
    verbose=True
)

# Pass a massive text context. The RLM puts it in a REPL variable rather than the prompt context!
#### large_context = "..."
#large_context = "TecX's full form is Technology Engineering Computation Expantion." 
large_context = input("What do you want know?")
query = "Extract all key metrics across the quarterly financial statements."

result = rlm.completion(prompt=query, context=large_context)
print(result)

