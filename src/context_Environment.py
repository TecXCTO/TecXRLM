# Context Environment
import model as model
class ContextEnvironment:
  def __init__(self,**args,*arg,model):
    self.huge_doc=[]
    self.model=model
  def prompt(self,user_input):
    self.huge_doc=user_input

# print(huge_doc[5000:7000]))

# context_file

# i=0
# chunk= []
# while len(full_text)>4000 :
   # if len(full_text)/4000>i:
     # chunk[i] = full_text[4000*i:4000*i+1]
   # elif len(full_text)/4000=<i:
     # chunk[i] = full_text[4000*i:]
   # i++




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
      
