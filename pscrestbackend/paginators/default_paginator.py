from rest_framework.pagination import PageNumberPagination
from rest_framework.response import Response

class TenPerPagination(PageNumberPagination):
    page_size = 10
    page_size_query_param = 'page_size'
    max_page_size = 1000
    def get_paginated_response(self, data):
        response= super().get_paginated_response(data)
        next_page_number=0
        previous_page_number=0
        if self.page.has_next():
            next_page_number = self.page.next_page_number()
        if self.page.has_previous():
            previous_page_number = self.page.previous_page_number()
        body = {
            'count' : self.page.paginator.count,
            'next' : next_page_number,
            'previous': previous_page_number,
            'results': data,
            'pageSize': self.get_page_size(self.request)
        }
        
        return Response(body)