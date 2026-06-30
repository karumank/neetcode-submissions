class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:
        
        fleet_time = 0
        fleet_count = 0
        postion_map = {}
        for i in range(len(position)):
            postion_map[position[i]] = speed[i]

        position.sort()
        for i in reversed(range(len(position))):
            curr_fleet_time = (target - position[i]) / postion_map[position[i]]
            if curr_fleet_time <= fleet_time:
                continue
            else:
                fleet_count += 1
                fleet_time = curr_fleet_time
        
        return fleet_count




