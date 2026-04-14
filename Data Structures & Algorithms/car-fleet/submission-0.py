class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:
        car = []

        for i in range(len(position)):
            car.append((position[i],speed[i]))
        car.sort(reverse = True)

        stack = []

        for pos, spd in car:
            time = (target - pos)/spd

            if not stack or time > stack[-1]:
                stack.append(time)
        return len(stack) 