class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        
        # temp = temperatures
        # result = [0] * len(temp)

        # stack = []

        # for i, t in enumerate(temp):
        #     while stack and stack[-1][0] < t:
        #         stack_t, stack_i = stack.pop()

        #         result[stack_i] = i - stack_i
            
        #     stack.append((t,i))
        
        # return result
                
        temp = temperatures
        result = [0]* len(temp)

        stack = []


        for i, t in enumerate(temp):
            while stack and stack[-1][0] < t:
                stack_t, stack_i = stack.pop()
                result[stack_i] = i - stack_i

            stack.append((t,i))
        return result 

