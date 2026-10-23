class Solution(object):
    def asteroidsDestroyed(self, mass, asteroids):
        asteroids.sort()
        for i in range(len(asteroids)):
            if asteroids[i] <= mass:
                mass += asteroids[i]
            else:
                return False
        return True
        """
        :type mass: int
        :type asteroids: List[int]
        :rtype: bool
        """
        