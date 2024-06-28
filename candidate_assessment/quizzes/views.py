from django.http import HttpRequest, HttpResponse, HttpResponseNotFound, Http404


def index(request: HttpRequest) -> HttpResponse:
    return HttpResponse('Main page of quizzes')


def types(request: HttpRequest, types_id: int) -> HttpResponse:
    if types_id == 1:
        raise Http404()
    return HttpResponse(f'types: {types_id}')


def types_by_slug(request: HttpRequest, types_slug: str) -> HttpResponse:
    return HttpResponse(f'types slug: {types_slug}')


def page_not_found(request: HttpRequest, exception):
    return HttpResponseNotFound('<h1>Страница не найдена</h1>')
