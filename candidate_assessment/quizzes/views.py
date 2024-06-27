from django.http import HttpRequest, HttpResponse


def index(request: HttpRequest) -> HttpResponse:
    return HttpResponse('Main page of quizzes')


def types(request: HttpRequest, types_id: int) -> HttpResponse:
    return HttpResponse(f'types: {types_id}')


def types_by_slug(request: HttpRequest, types_slug: str) -> HttpResponse:
    return HttpResponse(f'types slug: {types_slug}')
