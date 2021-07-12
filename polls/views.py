from django.http import HttpResponse
from django.contrib.auth.decorators import login_required


@login_required()
def index(request):
    return HttpResponse(f"Hello, {request.user}. You're at the polls index.")