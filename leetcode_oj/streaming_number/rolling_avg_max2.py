from collections import deque


class Solution(object):
    """Apply a moving window to an iterator, calculate max and average.

    Arguments:
      iter_ (iterator): The iterator to process.
      w (int): The length of the moving window to apply.

    Attributes:
      window (deque): The moving window.

    Example:

        >>> list(Solution(range(1, 7), 3))
        [(None, None), (None, None), (2, 3), (3, 4), (4, 5), (5, 6)]

    """

    def __init__(self, iter_, w):
        self.iter = iter(iter_)
        self.w = w
        self.window = deque(maxlen=w)

    def __iter__(self):
        return self

    def next(self):
        """Calculate the next value in the series.

        Notes:
          If the window isn't full, return (None, None). 

        """
        self.window.append(next(self.iter))
        if len(self.window) == self.w:
            return (self._avg(), self._max())
        return (None, None)

    def _max(self):
        """Calculate the maximum of the current window."""
        return max(self.window)

    def _avg(self):
        """Calculate the average of the current window."""
        return int(sum(self.window) / float(len(self.window)))


a = range(1,7)
w = 3
s = Solution(a,3)
for res in s:
	print res 
