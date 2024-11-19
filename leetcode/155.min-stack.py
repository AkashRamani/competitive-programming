#
# @lc app=leetcode id=155 lang=python3
#
# [155] Min Stack
#

# @lc code=start
class MinStack:

    '''
    Time: O(1) ; Space: O(n) --> for stack

    Takeaways:
    1. Very careful when doing append especially as a stack.. when you pop and append again it will scew up your top-element logic
    2. I named this variable as `top` and it confilcted with the function top within this.. and took me a while to figure out xD. AVOID such silly mistakes!
    '''

    def __init__(self):
        self.stack = []
        self.stack_top = -1
        
    def push(self, val: int) -> None:
        min_val = val
        if self.stack_top > -1 :
            _, current_min = self.stack[self.stack_top]
            min_val = min(current_min, min_val) 

        self.stack_top +=1
        # if you simply append it will mess up stack values, since I am non deleting when popping
        if self.stack_top < len(self.stack):
            self.stack[self.stack_top] = (val, min_val)
        else:
            self.stack.append((val, min_val))

    def pop(self) -> None:
        self.stack_top -=1

    def top(self) -> int:
        val, _ = self.stack[self.stack_top]
        return val

    def getMin(self) -> int:
        _, min_val = self.stack[self.stack_top]
        return min_val
        
    '''
    #Alternatively you can also maintain a second stack for minimums! 
    # whenever you encounter a value <= min you store in the stack
    # when you pop; check if min_stack_top == stack_top; if yes pop from min_stack as well
    '''
    
    '''
    To further improve.. notice if 1 keeps on repeating {consecutively as a min value} too often in stack, we will store it as many times it appears.
    We can optimize that by storing a count next to it.. but it's Meh (not really reqd.)
    '''


# Your MinStack object will be instantiated and called as such:
# obj = MinStack()
# obj.push(val)
# obj.pop()
# param_3 = obj.top()
# param_4 = obj.getMin()

# @lc code=end

