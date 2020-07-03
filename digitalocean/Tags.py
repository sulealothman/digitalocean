from .reqmethods import Req, Arrange


class Tags(Req, Arrange):
	slug = 'tags'
	def __init__(self, token):
		self.setToken(token)

	def storeTags(self, tag):
		body = {"name":f'{tag}'}
		data = self.post(self.slug, body)
		return data

	def getTag(self, tag):
		data = self.get(f'{self.slug}/{tag}')
		return self.arrangeData(data)

	def getAllTags(self):
		data = self.get(self.slug)
		return self.arrangeData(data)

	def deleteTag(self, tag):
		body = {"name":f'{tag}'}
		data = self.delete(f'{self.slug}/{tag}')
		return data