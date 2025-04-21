class Solution:
    #sort the peopl array
    #for the weight that is >= limit, from the ele to the end all requires one boat
    #for weight < limit, since each boat carries two poeple at the same time, try to match the r pointer with the left pointer(which is the heaviest and lightest 2)
    def numRescueBoats(self, people: List[int], limit: int) -> int:
        people.sort()
        count = 0
        l, r = 0, len(people) - 1

        while l <= r:
            #shrink the people array into weight all < limit
            if people[r] >= limit:
                count += 1
                r -= 1
                continue
   
            # pair the people[l] + people[r], if it's below the limit, increase count, move both r and l pointer inward, 
            # else increase the count, move the r pointer inward
            sum = people[l] + people[r]
            # means the r and l can fit in one boat! shift both pointers
            if sum <= limit:
                count += 1
                l += 1
                r -= 1
            # means sum exceed the limit, so only put r in one boat, and shift just the right poniter
            else: 
                count += 1
                r -= 1
        return count