class Building:
	"""docstring for Building"""
	def __init__(self, area, floor):
		self.area = area
		self.floor = floor
		self.lift = 1
		
apex = Building(500, 3)
print(apex.area)
print(apex.floor)
print(apex.lift)
apex.lift = 0
print(apex.lift)