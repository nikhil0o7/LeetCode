class Solution:
    def asteroidCollision(self, asteroids: List[int]) -> List[int]:
        new_asteroids = []

        for a in asteroids:
            while new_asteroids and a < 0 < new_asteroids[-1]:
                if abs(a) > new_asteroids[-1]:
                    new_asteroids.pop()
                elif abs(a) == new_asteroids[-1]:
                    new_asteroids.pop()
                    break
                else:
                    break
            else:
                new_asteroids.append(a)
        return new_asteroids