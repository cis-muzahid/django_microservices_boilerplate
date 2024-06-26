from rest_framework.pagination import PageNumberPagination
from collections import OrderedDict
from rest_framework.response import Response

class PageLinkPagination(PageNumberPagination):
    '''
    Get App Products Pagination
    '''
    page_size = 10
    page_size_query_param = 'page_size'
    def get_paginated_response(self, data):
        next_page = int(self.page.number) + 1 if self.page.has_next() else None
        previous_page = int(self.page.number) - 1 if self.page.has_previous() else None
        return Response(OrderedDict([
            ('next', next_page),
            ('previous', previous_page),
            ('total_count', self.page.paginator.count),
            ('num_pages',self.page.paginator.num_pages),
            ('results', data)
        ]))

class UserPageLinkPagination(PageNumberPagination):
    '''
    Get App Products Pagination
    '''
    page_size = 50
    page_size_query_param = 'page_size'
    def get_paginated_response(self, data):
        next_page = int(self.page.number) + 1 if self.page.has_next() else None
        previous_page = int(self.page.number) - 1 if self.page.has_previous() else None
        return Response(OrderedDict([
            ('next', next_page),
            ('previous', previous_page),
            ('total_count', self.page.paginator.count),
            ('num_pages',self.page.paginator.num_pages),
            ('results', data)
        ]))