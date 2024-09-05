from rest_framework.pagination import PageNumberPagination
from rest_framework.response import Response


class CustomPageNumberPagination(PageNumberPagination):
    page_size = 2  # 1 sahifada 3 ta obyekt keladi
    page_size_query_param = 'page_size'
    max_page_size = 100

    def get_paginated_response(self, data):  # Bu response korinishi
        return Response(
            {
                "next": self.get_next_link(),
                "previous": self.get_previous_link(),
                "count": self.page.paginator.count,
                "results": data
            }
        )
