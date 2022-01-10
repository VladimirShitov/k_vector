from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.forms import AuthenticationForm
from django.shortcuts import render
from django.http import HttpResponseRedirect
from loguru import logger


def logout_view(request):
    logger.info(
        "{fun} received a {method} request", fun=logout_view.__name__, method=request.method
    )
    logout(request)

    redirect_url = request.GET.get("next", "/")
    logger.info("User logged out. Redirecting to: {}", redirect_url)
    return HttpResponseRedirect(redirect_url)


def login_view(
        request, template_name="authentication/login_form.html", form_class=AuthenticationForm
):
    logger.info(
        "{fun} received a {method} request", fun=login_view.__name__, method=request.method
    )
    if request.method == "POST":
        form = form_class(request.POST)

        username = request.POST.get("username", "")
        password = request.POST.get("password", "")

        if not username or not password:
            return render(
                request,
                template_name,
                {"form": form, "errors": ["Пожалуйста, введите логин и пароль"]}
            )

        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            return HttpResponseRedirect(request.GET.get("next", "/"))
        else:
            return render(
                request,
                template_name,
                {"form": form, "errors": ["Пожалуйста, введите корректный логин и пароль"]}
            )

    else:
        form = form_class()
    return render(request, template_name, {"form": form})

