class Car(object):
  """
    blueprint for car
  """

  def __init__(self, model, color, company, speed_limit):
    self.model = model
    self.company = company
    self.color = color
    self.speed_limit = speed_limit

  def start(self):
    print("started")

  def stop(self):
    print("stopped")

  def accelerate(self):
    print("accelerating...")
    "accelarator funcionality here"

  def chang_gear(self, gear_type):
    print("gear changed")
    " gear related functionality here"

audi = Car("A6", "red", "audi", 80)

print(audi.start())