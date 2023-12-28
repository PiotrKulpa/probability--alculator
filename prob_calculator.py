import copy
import random
# Consider using the modules imported above.


class Hat:

  def __init__(self, **balls):
    self.contents = []
    for key, value in balls.items():
      self.contents += value * [key]

    self.__initial_contents = copy.copy(self.contents)

  def draw(self, balls_draw_number):
    try:
      draw = random.sample(self.contents, balls_draw_number)
    except:
      draw = copy.copy(self.contents)
    for ball in draw:
      self.contents.remove(ball)

    if len(self.contents) == 0:
      self.contents = copy.copy(self.__initial_contents)
    
    return draw
   

  def reset(self):
    self.contents = copy.copy(self.__initial_contents)

def experiment(hat, expected_balls, num_balls_drawn, num_experiments):
  expected_balls_number = 0
  
  for x in range(num_experiments):
    hat.reset()
    drawned_balls = hat.draw(num_balls_drawn)
    if all(drawned_balls.count(k) >= v for k, v in expected_balls.items()):
      expected_balls_number += 1
        
  return expected_balls_number / num_experiments
