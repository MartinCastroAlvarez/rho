""" Singleton applied to Python by martincastro.10.5@gmail.com """

class Singleton(object):

        __singleton = None

        def __new__(cls, *args, **kwargs):
                if not cls.__singleton:
                        cls.__singleton = object.__new__(cls, *args, **kwargs)
                return cls.__singleton
