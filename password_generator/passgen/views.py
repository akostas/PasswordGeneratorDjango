from django.http import JsonResponse, HttpRequest
from .utils import generate_password


# Create your views here.
def password_view(request: HttpRequest) -> JsonResponse:
    """
    Generate a random password based on user-defined options and return it as a JSON.

    :param request: HttpRequest: A request which contains the user-defined options.

    :return: JsonResponse: A JSON object containing the generated password.
    """
    length = int(request.GET.get("length", 12))
    use_numbers = request.GET.get("numbers", "false").lower() == "true"
    use_symbols = request.GET.get("symbols", "false").lower() == "true"

    password = generate_password(length, use_numbers, use_symbols)

    return JsonResponse({"password": password})
