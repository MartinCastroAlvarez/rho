""" Servant pattern applied to Python by martincastro.10.5@gmail.com """

class ArticleServant:
	
	def publish(self,article):
		assert isinstance(article,Article), "Invalid article instance"
		print ("Article '%s' is published!!" % article.name)

class Article:
	
	def __init__(self,n):
		self.name = n 

	def publish(self):
		raise Exception("Not implemented here") 

class LongArticle(Article):
	pass

class MediumArticle(Article):
	pass

class ShortArticle(Article):
	pass

p  = ArticleServant()
a1 = LongArticle("Deep Purple")
a2 = MediumArticle("Pink Floyd")
a3 = ShortArticle("Steve Vai")
p.publish(a1)
p.publish(a3)
p.publish(a2)
