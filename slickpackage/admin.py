from django.contrib import admin

# Register your models here.
from slickpackage.models import Categories,Snippetquote, thepackage, packagesub, industryproduct, featuredproducts,IndCategories,Process,Snippet,Special
# Register your models here.

admin.site.register(Categories)
admin.site.register(thepackage)
admin.site.register(packagesub)
admin.site.register(industryproduct)
admin.site.register(featuredproducts)
admin.site.register(IndCategories)
admin.site.register(Snippet)
admin.site.register(Special)
admin.site.register(Process)
admin.site.register(Snippetquote)
