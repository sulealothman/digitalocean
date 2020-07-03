from .reqmethods import Req, Arrange

class Images(Req, Arrange):
	slug = 'images'

	def __init__(self, token):
		self.setToken(token)

	def getAllImages(self):
		data = self.get(self.slug)
		if 'id' in data:
			return data
	
		return self.arrangeData(data)

	def getAlldistImages(self):
		data = self.get(f'{self.slug}?type=distribution')
		if 'id' in data:
			return data
	
		return self.arrangeData(data)

	def getAllAppImages(self):
		data = self.get(f'{self.slug}?type=application')
		if 'id' in data:
			return data
	
		return self.arrangeData(data)

	def getUserImages(self):
		data = self.get(f'{self.slug}?private=true')
		if 'id' in data:
			return data
	
		return self.arrangeData(data)

	def getImagesByTag(self, tagName):
		data = self.get(f'{self.slug}?tag_name={tagName}')
		if 'id' in data:
			return data
	
		return self.arrangeData(data)

	def getImageBySlug(self, slug):
		data = self.get(f'{self.slug}/{slug}')
		if 'id' in data:
			return data
	
		return self.arrangeData(data)

	def getImageById(self, imageId):
		data = self.get(f'{self.slug}/{imageId}')
		if 'id' in data:
			return data
	
		return self.arrangeData(data)

	def getAllImageActions(self, imageId):
		data = self.get(f'{self.slug}/{imageId}/actions')
		if 'id' in data:
			return data
	
		return self.arrangeData(data)

	def storeImage(self, body):
		data = self.post(f'{self.slug}', body)
		return data

	def updateImage(self,imageId, body):
		data = self.put(f'{self.slug}/{imageId}', body)
		return data

	def deleteImage(self, imageId):
		data = self.delete(f'{self.slug}/{imageId}')
		return data
