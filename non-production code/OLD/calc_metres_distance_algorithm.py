"""
Algorithm to calculate the distance covered in a route and all its
sub-routes.
This requires that a Route have its own Waypoint.
"""

# --------
# route.py
# --------
	def calc_metres_distance(self, next_segment=None):
	"""
	Selects two adjacent pathways and finds the distance between them.
	If the first pathway is actually a subroute, it recurses down to
	find that routes total distance, and adds that to this routes distance.
	Terminates at segments: 'seg' = length-1 and 'next_seg' = length
	"""
		cumulative = 0.0
		for i, seg in zip(range(len(pathway)-1), pathway):
			"""
			Loops over all elements in pathway except the last one.
			Using zip with the length of 'pathway-1' terminates the
			loops last 'segment' early - there is no 'next' at that point
			"""
			next_seg = pathway[i+1]
			if seg isinstance(Route):
				cumulative += seg.calc_metres_distance(None)
			else:
				"""
				if next_seg is a Route, find its 1st waypoint
				"""
				if next_seg isinstance(Route):
					x = next_seg.pathway[0]
				else:
					x = next_seg
				cumulative += seg.calc_metres_distance(x)
		return cumulative



# --------------
# description.py
# --------------
	def calc_metres_distance(self, next_segment=None):
	"""
	Simply calls GeoUtils to calculate the distance between two segments.
	"""
		dist = 0.0
		if next_segment is not None:
			dist = GeoUtils.calc_metres_distance(self.latitude,
						self.longitude, next_segment.latitude,
						next_segment.longitude)
		return dist

# ----------
# segment.py
# ----------
	"""technically this class doesn't exist because in python
	you can use duck typing"""
	def calc_metres_distance(self, next_segment=None):
		pass
