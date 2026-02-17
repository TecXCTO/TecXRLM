# Context Environment

class ContextEnvironment:
  def __init__(self,**args,*arg,model):
    self.huge_doc=[]
    self.model=model
  def prompt(self,user_input):
    self.huge_doc=user_input
