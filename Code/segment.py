from abc import ABC, abstractmethod
"""
Segment.py
"""


class Segment(ABC):

    @abstractmethod
    def calc_metres_dist(self):
        pass

