# https://leetcode.com/problems/fruit-into-baskets/

class Solution(object):
    def totalFruit(self, fruits):
        """
        :type fruits: List[int]
        :rtype: int
        """
        fruitType = Counter()
        maxFruits = distinct = 0
        left = right = 0
        
        while right < len(fruits):
            #check if it is a new fruit & update the counter
            if fruitType[fruits[right]] == 0:
                distinct += 1
            fruitType[fruits[right]] += 1
            
            #too many different fruits, start shrinking the window
            while distinct > 2:
                #reduce the count of the fruit in the left pointer
                fruitType[fruits[left]] -= 1
                if fruitType[fruits[left]] == 0:
                    distinct -= 1
                left += 1
            
            #set max fruits to the max window size
            maxFruits = max(maxFruits, right-left+1)
            right += 1
            
        return maxFruits
      
