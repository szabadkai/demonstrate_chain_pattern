class Handler(object):

    def __init__(self, successor=None):
        self._successor = successor

    def from_row(self, *args, **kwargs):
        res = self._handle(*args, **kwargs)
        if not res:
            res = self._successor.from_row(*args, **kwargs)

        return res

    def _handle(self, *args, **kwargs):
        raise NotImplementedError('Must provide implementation in subclass.')
