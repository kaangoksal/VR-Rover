import abc

class Wheel(object):
    __metaclass__ = abc.ABCMeta
    @abc.abstractclassmethod
    def setspeed(self, thr):
        """set speed for the wheel"""
        return

