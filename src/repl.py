
print(huge_doc[5000:7000]))

context_file


while len(full_text)>4000 :
  chunk = full_text[0:4000]




def recursive_summarize(text, model):
    # If text is small enough, just answer
    if len(text) < 4000:
        return model.generate(f"Summarize this: {text}")
    
    # Recursive Step: Split and call itself
    mid = len(text) // 2
    left_summary = recursive_summarize(text[:mid], model)
    right_summary = recursive_summarize(text[mid:], model)
    
    # Aggregation Step
    return model.generate(f"Combine these two summaries: {left_summary} and {right_summary}")
