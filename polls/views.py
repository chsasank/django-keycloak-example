from django.http import HttpResponse
from django.contrib.auth.decorators import login_required


@login_required
def index(request):
    return HttpResponse(
        f"Welcome {request.user.first_name} {request.user.last_name}. Hello, world. You're at the polls index."
    )
