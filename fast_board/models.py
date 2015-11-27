from django.db import models
from django.core.urlresolvers import reverse

# Create your models here.
class Post(models.Model):
	
	# uuid = models.UUIDField() 
	# uuid.hax
	title = models.CharField(max_length = 100)
	content = models.TextField(blank=True)
	created_at = models.DateTimeField(auto_now_add=True)
	updated_at = models.DateTimeField(auto_now=True)
	category = models.ForeignKey('Category')
	tags = models.ManyToManyField('Tag')
	
	def __str__(self):
		return '<Post pk:{}, title: {}, comments : {}'.format( self.pk, self.title, self.comment_set.count())

	def get_absolute_url(self):
		return reverse('myblog:view', kwargs={'pk':self.pk})

class Category(models.Model):
	name = models.CharField(max_length = 200)
	created_at = models.DateTimeField(auto_now_add=True)
	updated_at = models.DateTimeField(auto_now=True)

	def __str__(self):
		return '<Category pk:{}, name:{}>'.format(self.pk, self.name)

class Comment(models.Model):
	post = models.ForeignKey(Post)
	content = models.TextField(null=False, blank=False)
	created_at = models.DateTimeField(auto_now_add=True)
	updated_at = models.DateTimeField(auto_now=True)

	def __str__(self):
		return '<Comment pk:{}>'.format(self.pk)

class Tag(models.Model):
	name = models.CharField(max_length=40)
	created_at = models.DateTimeField(auto_now_add=True)
	updated_at = models.DateTimeField(auto_now=True)

	def __str__(self):
		return '<Tag pk:{}, name:{}>'.format(self.pk, self.name)