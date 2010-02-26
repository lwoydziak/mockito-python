class Matcher:
  def matches(self, arg):
    pass
  
class Any(Matcher):     
  def __init__(self, wanted_type=None):
    self.wanted_type = wanted_type
    
  def matches(self, arg):     
    if self.wanted_type:
      return isinstance(arg, self.wanted_type)
    else:
      return True
  
  def __repr__(self):
    return "<Any: %s>" % self.wanted_type  

class Contains(Matcher):
  def __init__(self, sub):
    self.sub = sub
      
  def matches(self, arg):
    if not hasattr(arg, 'find'):
      return  
    return self.sub and len(self.sub) > 0 and arg.find(self.sub) > -1

  def __repr__(self):
    return "<Contains: '%s'>" % self.sub  