from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect, get_object_or_404
from loguru import logger

from .forms import SampleForm, SampleEditForm
from .models import Sample, SamplePhoto, SampleCategory
from .utils import save_sample, get_categories_content


def index(request):
    return render(request, "pathology/index.html")


def sample_form(request, form_class=SampleForm, template="pathology/sample_form.html"):
    logger.info(
        "{fun} received a {method} request", fun=sample_form.__name__, method=request.method
    )

    if request.method == "POST":
        form = form_class(request.POST, request.FILES)
        logger.debug("Images: {}", form.files)
        logger.debug("Form data: {}", form.data)

        if form.is_valid():
            logger.success("Form is valid, saving the sample")
            sample_id = save_sample(form.data, form.files.getlist("images"))
            return redirect(sample_view, sample_id=sample_id)
        else:
            logger.warning("Form is not valid")
            return render(
                request, template, {"form": form, "errors": form.errors}
            )

    else:
        form = form_class()

    return render(request, template, {"form": form})


def sample_view(request, sample_id: int, template="pathology/sample.html"):
    sample = get_object_or_404(Sample, pk=sample_id)
    images = SamplePhoto.objects.filter(sample=sample)
    return render(
        request,
        template,
        {"sample": sample, "images": images}
    )


@login_required
def sample_edit_view(
        request,
        sample_id: int,
        template="pathology/sample_edit_form.html",
        form_class=SampleEditForm
):
    logger.info(
        "{fun} received a {method} request", fun=sample_edit_view.__name__, method=request.method
    )
    sample = get_object_or_404(Sample, pk=sample_id)
    images = SamplePhoto.objects.filter(sample=sample)

    if request.method == "POST":
        form = form_class(request.POST)

        if form.is_valid():
            logger.success("Form is valid, saving the sample")
            form.save(sample_id=sample_id)
            return redirect(sample_view, sample_id=sample_id)
        else:
            logger.warning("Form is not valid")
            return render(
                request,
                template,
                {
                    "form": form, "errors": form.errors,
                    "sample_id": sample_id,
                    "images": images,
                }
            )

    else:
        form_fields_values = {
            "title": sample.title,
            "category": sample.category.name,
            "description": sample.description,
            "images": images,
        }
        form = form_class(initial=form_fields_values)

    return render(
        request,
        template,
        {
            "form": form,
            "sample_id": sample_id,
            "images": images,
        }
    )


@login_required
def sample_delete_view(request, sample_id: int, template="pathology/success_page.html"):
    sample = get_object_or_404(Sample, pk=sample_id)
    sample.delete()

    return render(
        request,
        template,
        {"message": "Препарат успешно удалён"}
    )


def samples_list(request, template="pathology/samples_list.html"):
    samples_dict = get_categories_content()
    return render(request, template, {"samples_dict": samples_dict})


def team(request, template="pathology/team.html"):
    return render(request, template)
