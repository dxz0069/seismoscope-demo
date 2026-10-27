class Book:
    class query:
        @staticmethod
        def filter_by(**kw):
            return _Q()
    class _Q:
        def first(self):
            return "demo"
