# There are N gas stations along a circular route, where the amount of gas at station i is gas[i].
#
# You have a car with an unlimited gas tank and it costs cost[i] of gas to travel from station i to its next station (i+1). You begin the journey with an empty tank at one of the gas stations.
#
# Return the starting gas station's index if you can travel around the circuit once, otherwise return -1.
#
# Note:
# The solution is guaranteed to be unique.

class Solution(object):
    def canCompleteCircuit(self, gas, cost):
        """
        :type gas: List[int]
        :type cost: List[int]
        :rtype: int
        """

        if sum(gas) - sum(cost) < 0:
            return -1
        ac, start = 0, 0
        for idx in range(len(gas)):
            cur = gas[idx] - cost[idx]
            if ac + cur < 0:
                start = idx + 1
                ac = 0
            else:
                ac += cur
        return start
