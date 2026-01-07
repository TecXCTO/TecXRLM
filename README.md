# TecXRLM
Technology Engineering Computation 


The Environment (REPL): The prompt P is loaded as a string variable context inside a Python Read-Eval-Print Loop.

The Interface: The Model is given a system prompt explaining it has access to context and a special function llm_query(sub_prompt).




The Recursive Trajectory
Phase 1: Probing, The model writes Python code (e.g, regex, slice) to inspect the structure of the data (e.g, "Is this a CSV? Let me check the first 5 lines."”).
Phase 2: Decomposition. The model writes a loop in Python to iterate over the context.
Phase 3: Recursion, Inside the loop, it calls llm_query. This spawns a fresh instance of the model (with an empty context window). This sto-instance reads the specific chunk and returns a compressed insight or answer.
Phase 4: Aggregation. The root model
