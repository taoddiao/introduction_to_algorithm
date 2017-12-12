class heap(list):
	def __init__(self, inlist=None):
		if inlist == None:
			inlist = list()
		super(self).__init__(inlist)

	def parent(self, i):
		if i == 0:
			return None
		else:
			if i < 0:
				i += len(self)
			key = int((i - 1) / 2)
			return self.__getitem__(key)
