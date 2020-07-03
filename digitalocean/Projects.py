from .reqmethods import Req, Arrange

class Projects(Req, Arrange):
	slug = 'projects'

	def __init__(self, token):
		self.setToken(token)

	def storeProject(self, projectName, projectDesc, purpose, environment):
		body = {"name":f'{projectName}', 'description' : f'{projectDesc}', 'purpose' : f'{purpose}', 'environment' : f'{environment}'}
		data = self.post(self.slug, body)
		return data

	def updateProject(self, projectId, projectName, projectDesc, purpose, environment, isDefault):
		body = {"name":f'{projectName}', 'description' : f'{projectDesc}', 'purpose' : f'{purpose}', 'environment' : f'{environment}', 'is_default': f'{isDefault}'}
		data = self.put(f'{self.slug}/{projectId}', body)
		return data

	def updataDefaultProject(self, projectId, projectName, projectDesc, purpose, environment, isDefault):
		body = {"name":f'{projectName}', 'description' : f'{projectDesc}', 'purpose' : f'{purpose}', 'environment' : f'{environment}', 'is_default': f'{isDefault}'}
		data = self.put(f'{self.slug}/default', body)
		return data


	def updataPartPorject(self, projectId, body):
		data = self.patch(f'{self.slug}/{projectId}', body)
		return data

	def updatePartProject(self, body):
		data = self.patch(f'{self.slug}/default', body)
		return data

	def getAllPorjects(self):
		data = self.get(self.slug)
		if 'id' in data:
			return data
	
		return self.arrangeData(data)

	def getProjectById(self, projectId):
		data = self.get(f'{self.slug}/{projectId}')
		if 'id' in data:
			return data
	
		return self.arrangeData(data)

	def getDefaultProject(self):
		data = self.get(f'{self.slug}/default')
		if 'id' in data:
			return data
	
		return self.arrangeData(data)

	def deletePorject(self, projectId):
		data = self.delete(f'{self.slug}/{projectId}')
		return data