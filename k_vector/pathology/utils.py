from typing import List

from django.core.files import File
from django.core.files.uploadedfile import TemporaryUploadedFile
from django.db import transaction
from loguru import logger

from .models import SampleCategory, Sample, SamplePhoto


def save_sample(form_data, images):
    with transaction.atomic():
        category, created = SampleCategory.objects.get_or_create(name=form_data["category"])
        if created:
            category.save()

        sample = Sample(
            title=form_data["title"],
            category=category,
            description=form_data["description"]
        )
        sample.save()

        for i, photo in enumerate(images):
            logger.debug("Saving photo: {}", photo)
            sample_photo = SamplePhoto(
                image=photo,
                order=i,
                sample=sample
            )
            sample_photo.save()
            logger.debug("SamplePhoto object: {}", sample_photo)
            logger.debug("SamplePhoto path: {}", sample_photo.image.path)

    return sample.pk


def get_categories_content():
    """Return dict, which keys are categories and values are lists of samples"""
    categories = SampleCategory.objects.all()
    content = {}

    for category in categories:
        samples = Sample.objects.filter(category=category)
        if samples:
            content[category.name] = samples

    return content
