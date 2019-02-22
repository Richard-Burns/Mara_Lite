import uuid

def GenerateID():
	uid = str(uuid.uuid4())
	uid = uid.replace("-", "_")
	return uid
	

class Main:
	"""
	Main description
	"""
	def __init__(self, ownerComp):
		self.ownerComp = ownerComp
		self.tbl = op('opfind_projectors')
		self.geos = op('folder_sets')
		self.sets = op('opfind_sets')
		return
		
	# projector functionality
	
	def CreateProjector(self, newProjName):
		newProj = parent().copy(op('base_templates/geo_projector1'))
		newProjID = GenerateID()
		newProj.name = "geo_projector_"+newProjID
		newProj.par.Id = newProjID
		newProj.par.Name = newProjName
		newProj.nodeX = (self.tbl.numRows-1)*200
		newProj.nodeY = 1000
		return

	def RemoveProjector(self, o):
		if op(o):
			op(o).destroy()	
		return
	
	# set functionality
	
	def CreateSet(self, newSetName, newSetFile):
		newSet = parent().copy(op('base_templates/geo_set1'))
		newSetID = GenerateID()
		newSet.name = "geo_set_"+newSetID
		newSet.par.Id = newSetID
		newSet.par.Name = newSetName
		newSetFile = str(newSetFile)
		newSet.par.Geometryfile = newSetFile
		newSet.nodeX = (self.sets.numRows-1)*200
		newSet.nodeY = 1200
		return
		
	def RemoveSet(self, o):
		if op(o):
			op(o).destroy()	
		return
	
	# menu update functionality

	def UpdateProjectorsMenu(self):
		labels = []
		names = []
		c = self.tbl
		for r in range(1,c.numRows):
				name = op(c[r,'name']).par.Name
				labels.append(name)
				names.append(c[r,'name'])

		self.ownerComp.par.Projectors.menuLabels = labels
		self.ownerComp.par.Projectors.menuNames = names
		return
		
	def UpdateSetsMenu(self):
		labels = []
		names = []
		c = self.sets
		for r in range(1,c.numRows):
				name = op(c[r,'name']).par.Name
				labels.append(name)
				names.append(c[r,'name'])

		self.ownerComp.par.Sets.menuLabels = labels
		self.ownerComp.par.Sets.menuNames = names
		return
		
	def UpdateGeometryFileMenu(self):
		labels = []
		names = []
		c = self.geos
		for r in range(1,c.numRows):
				labels.append(c[r,'name'].val)
				names.append(c[r,'relpath'].val)

		self.ownerComp.par.Geometryfile.menuLabels = labels
		self.ownerComp.par.Geometryfile.menuNames = names
		return