from django.http import HttpResponse
from django.contrib.auth.decorators import login_required
from django.template import Template, Context


@login_required
def index(request):
    return HttpResponse(f"Hello, {request.user}. You're at the polls index.")

def login(request):
    return render_template(
        """{% if user.is_authenticated %}
  <p>Current user: {{ user.email }}</p>
  <form action="{% url 'oidc_logout' %}" method="post">
    {% csrf_token %}
    <input type="submit" value="logout">
  </form>
{% else %}
  <a href="{% url 'oidc_authentication_init' %}">Login</a>
{% endif %}
""")