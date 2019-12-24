from rest_framework.pagination import LimitOffsetPagination

class LimitOffsetPaginationWithUpperBound(LimitOffsetPagination):
	"""docstring for ClassName"""
	max_limit = 8
	