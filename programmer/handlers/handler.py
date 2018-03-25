import abc


class Handler(object):
    __metaclass__ = abc.ABCMeta

    def __init__(self, successor=None):
        self._successor = successor

    def handle(self, *args, **kwargs):
        res = self._handle(*args, **kwargs)
        if not res:
            res = self._successor.handle(*args, **kwargs)

        return res

    @abc.abstractmethod
    def _handle(self, *args, **kwargs):
        raise NotImplementedError('Must provide implementation in subclass.')
