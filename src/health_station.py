# from person import Person

class HealthStation:
    
    def __init__(self):
        # what should be here?
      self.weighins = 0
      pass

    def weigh(self, person):
        # return the weight of the person passed as the parameter
      self.weighins +=1
      return person.get_weight()
    
    def feed(self,person):
      increaseWeight = person.set_weight(person.get_weight()+1)
      return increaseWeight

    def weighings(self):
      return self.weighins

if __name__ == '__main__':
  from person import Person  
else:
  from src.person import Person
