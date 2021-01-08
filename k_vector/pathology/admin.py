from django.contrib import admin

from .models import Sample, SamplePhoto, SampleCategory


admin.site.register(Sample)
admin.site.register(SamplePhoto)
admin.site.register(SampleCategory)
