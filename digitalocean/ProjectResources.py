from .reqmethods import Req, Arrange

class ProjectsResources(Req, Arrange):
	slug = 'projects'

	def __init__(self, token):
		self.setToken(token)

	def updateProject(self, projectId, projectName, projectDesc, purpose, environment, isDefault):
		body = {"name":f'{projectName}', 'description' : f'{projectDesc}', 'purpose' : f'{purpose}', 'environment' : f'{environment}', 'is_default': f'{isDefault}'}
		data = self.put(f'{self.slug}/{projectId}', body)
		return data

	def updataDefaultProject(self, projectId, projectName, projectDesc, purpose, environment, isDefault):
		body = {"name":f'{projectName}', 'description' : f'{projectDesc}', 'purpose' : f'{purpose}', 'environment' : f'{environment}', 'is_default': f'{isDefault}'}
		data = self.put(f'{self.slug}/default', body)
		return data

	def assignResourcesPorject(self, projectId, body):
		data = self.post(f'{self.slug}/{projectId}/resources', body)
		return data

	def assignResourcesDefaultProject(self, body):
		data = self.post(f'{self.slug}/resources/default', body)
		return data

	def getResourcesProject(self, projectId):
		data = self.get(f'{self.slug}/{projectId}/resources')
		if 'id' in data:
			return data
	
		return self.arrangeData(data)

	def getResourcesDefaultProject(self):
		data = self.get(f'{self.slug}/default/resources')
		if 'id' in data:
			return data
	
		return self.arrangeData(data)