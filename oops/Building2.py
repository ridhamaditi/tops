class Building:
	"""docstring for Building"""
	def __init__(self, area, floor):
		self.area = area
		self.floor = floor
		self.lift = 1
	def construct_floor(self, n):
		self.floor += n
		return f"Current no of floor: {self.floor}"
		
apex = Building(500, 3)
print(apex.floor)
print(apex.construct_floor(2))
print(apex.floor)