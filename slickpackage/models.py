from django.db import models

class industryproduct(models.Model):
	class Meta:
		verbose_name_plural = 'Industry Categories'

	name = models.CharField(max_length=32)
	description = models.TextField()
	image01 = models.ImageField(blank=True, null=True)
	image02 = models.ImageField(blank=True, null=True)
	image03 = models.ImageField(blank=True, null=True)
	OrderQuantity = models.CharField(max_length=32)
	Dimensions = models.CharField(max_length=32)
	Printing = models.CharField(max_length=32)
	PaperStock = models.CharField(max_length=32)
	Finishing = models.CharField(max_length=32)
	Options	 = models.CharField(max_length=32)
	DefaultProcess = models.CharField(max_length=32)
	Proof = models.CharField(max_length=32)
	categories = models.ForeignKey('IndCategories',
    on_delete=models.CASCADE,)

	def __str__(self):
		return self.name



'''categories tables'''
class IndCategories(models.Model):
	class Meta:
		verbose_name_plural = 'Industries'


	name = models.CharField(max_length=32)
	description = models.TextField()
	image01 = models.ImageField(blank=True, null=True)
	image02 = models.ImageField(blank=True, null=True)
	image03 = models.ImageField(blank=True, null=True)
	
	def __str__(self):
		return self.name


'''categories tables'''
class Categories(models.Model):
	class Meta:
		verbose_name_plural = 'Packages'

	name = models.CharField(max_length=32)
	description = models.TextField()
	image01 = models.ImageField(blank=True, null=True)
	image02 = models.ImageField(blank=True, null=True)
	image03 = models.ImageField(blank=True, null=True)
	
	def __str__(self):
		return self.name



'''package class'''

class thepackage(models.Model):
	class Meta:
		verbose_name_plural = 'Package Categories'

	name = models.CharField(max_length=50)
	description = models.TextField()
	image01 = models.ImageField(blank=True, null=True)
	image02 = models.ImageField(blank=True, null=True)
	image03 = models.ImageField(blank=True, null=True)
	categories = models.ForeignKey('Categories',
    on_delete=models.CASCADE,)

	def __str__(self):
		return self.name


class packagesub(models.Model):
	class Meta:
		verbose_name_plural = 'Package Sub Categories'

	name = models.CharField(max_length=50)
	description = models.TextField()
	image01 = models.ImageField(blank=True, null=True)
	image02 = models.ImageField(blank=True, null=True)
	image03 = models.ImageField(blank=True, null=True)
	OrderQuantity = models.CharField(max_length=32)
	Dimensions = models.CharField(max_length=32)
	Printing = models.CharField(max_length=32)
	PaperStock = models.CharField(max_length=32)
	Finishing = models.CharField(max_length=32)
	Options	 = models.CharField(max_length=32)
	DefaultProcess = models.CharField(max_length=32)
	Proof = models.CharField(max_length=32)

	categories = models.ForeignKey('thepackage',
    on_delete=models.CASCADE,)

	def __str__(self):
		return self.name


'''package class'''

class featuredproducts(models.Model):
	class Meta:
		verbose_name_plural = 'Packages for Featuring'
	name = models.CharField(max_length=50)
	description = models.TextField()
	image = models.ImageField(blank=True, null=True)
	
	def __str__(self):
		return self.name



class Snippet(models.Model):
	class Meta:
		verbose_name_plural = '.Output Form Contact Form'

	name = models.CharField(max_length=50)
	subject = models.CharField(max_length=50)
	body = models.TextField()
	
	
	def __str__(self):
		return self.name





class Process(models.Model):
	class Meta:
		verbose_name_plural = 'Steps for OUR PROCESSES'
	step01 = models.CharField(max_length=20)
	detail01 = models.TextField()
	image01 = models.ImageField(blank=True, null=True)
	step02 = models.CharField(max_length=20)
	detail02 = models.TextField()
	image02 = models.ImageField(blank=True, null=True)
	step03 = models.CharField(max_length=20)
	detail03 = models.TextField()
	image03 = models.ImageField(blank=True, null=True)	

	def __str__(self):
		return self.step01

	def __str__(self):
		return self.step02

	def __str__(self):
		return self.step03



class Special(models.Model):
	class Meta:
		verbose_name_plural = 'Our Special Product'

	name = models.CharField(max_length=32)
	description = models.TextField()
	image = models.ImageField(blank=True, null=True)

	
	def __str__(self):
		return self.name


TITLE_CHOICES = (
	('a', 'Regular Slotted Container'),
	('b', 'Half Slotted Container'),
	('c', 'Overlap Slotted Container'),
	('d', 'Full Overlap Slotted Container'),
	('e', 'Center Special Slotted Container'),
	('f', 'Center Special Overlap Slotted Container'),
	('g', 'Center Special Full Overlap Slotted Container'),
	('h', 'Snap Lock'),
	('i', 'Bellow Style Top and Bottom Container'),
	('j', 'Integral Divider Container'),
	('k', 'Full Telescope Design Style Container'),
	('l', 'Design Style Container with Cover'),
	('m', 'Double Cover Container'),
	('n', 'Interlocking Double Cover Container'),
	('o', 'Octagonal Double Cover Container'),
	('p', 'Full Telescope Half Slotted Container'),
	('q', 'One Piece Folder'),
	('r', 'One Piece Folder with ‘Air Cell’'),
	('s', 'Five Panel Folder'),
	('t', 'Wrap Around Blank'),
	('u', 'One Piece Folder with Dust Flaps and Tuck Flaps'),
	('v', 'Roll End Tray'),
	('w', 'Display Tray/High Wall Tray'),
)




class Snippetquote(models.Model):
	class Meta:
		verbose_name_plural = '.Output of User GET Quote '


	Name = models.CharField(max_length=100)
	Email = models.EmailField()
	ContactNumber = models.CharField(max_length=100)
	PackageType = models.CharField(max_length=250, choices=TITLE_CHOICES, default='a')
	Dimensions = models.CharField(max_length=100)
	Quantity = models.CharField(max_length=100)
	Specification = models.TextField()
	
	def __str__(self):
		return self.Name


