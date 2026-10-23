class Solution(object):
    def asteroidsDestroyed(self, mass, asteroids):
        asteroids.sort()
        for a in asteroids:
            if a <= mass:
                mass += a
            else:
                return False
        return True
        """
        :type mass: int
        :type asteroids: List[int]
        :rtype: bool
        """
        