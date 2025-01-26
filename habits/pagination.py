from rest_framework.pagination import PageNumberPagination

class HabitPagination(PageNumberPagination):
    """
    Настройка пагинации для списка привычек.

    Атрибуты:
        page_size: Количество элементов на одной странице по умолчанию (5).
        page_size_query_param: Параметр запроса для изменения количества элементов на странице ('page_size').
        max_page_size: Максимально допустимое количество элементов на странице (10).
        ordering: Порядок сортировки элементов по умолчанию ('-id').
    """
    page_size = 5
    page_size_query_param = 'page_size'
    max_page_size = 10
    ordering = '-id'
