'''A car travels from a starting position to a destination which is target miles east of the starting position.

Along the way, there are gas stations.  Each station[i] represents a gas station that is station[i][0] miles east of the starting position, and has station[i][1] liters of gas.

The car starts with an infinite tank of gas, which initially has startFuel liters of fuel in it.  It uses 1 liter of gas per 1 mile that it drives.

When the car reaches a gas station, it may stop and refuel, transferring all the gas from the station into the car.

What is the least number of refueling stops the car must make in order to reach its destination?  If it cannot reach the destination, return -1.

Note that if the car reaches a gas station with 0 fuel left, the car can still refuel there.  If the car reaches the destination with 0 fuel left, it is still considered to have arrived.'''
def minRefuelStops(self, target, startFuel, stations):
    """
    :type target: int
    :type startFuel: int
    :type stations: List[List[int]]
    :rtype: int
    """
    if not stations: return 0 if target <= startFuel else -1
    dp = [startFuel] + [0] * len(stations) 
    # dp[t] = the furthest distance we can go if we refuel t times
    
    for i,(pos,fuel) in enumerate(stations): # in the first i stations
        
        for t in xrange(i,-1,-1):
            # refuel t + 1 times in the first i stations
            if dp[t] >= pos:
                #we can reach station i
                dp[t+1] = max(dp[t+1],dp[t] + fuel) #the furthest distance we can go
    
    for i in xrange(len(dp)):
        if dp[i] >= target:
            return i
    return -1
        