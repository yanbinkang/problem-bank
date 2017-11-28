"""
https://community.topcoder.com/stat?c=problem_statement&pm=7921




 Problem Statement for RoadReconstruction


Problem Statement
    There are several cities in the country, and some of them are connected by bidirectional roads. Unfortunately, some of the roads are damaged and cannot be used right now. Your goal is to rebuild enough of the damaged roads that there is a functional path between every pair of cities.

    You are given String[] roads, each element of which describes a single road. Damaged roads are formatted as "id city1 city2 cost" and non-damaged roads are formatted as "id city1 city2" (all quotes for clarity). In this notation, id is the unique identifier of the road, and city1 and city2 are the case-sensitive names of the two cities directly connected by that road. If the road is damaged, cost represents the price of rebuilding that road. Each id will be formatted "Cx" (quotes for clarity), where C is an uppercase letter and x is a digit. Every city in the country will appear at least once in roads.

    Return a String containing a single space separated list of the identifiers of the roads that must be rebuilt to achieve your goal. If there are multiple possibilities, select the one with the minimal total reconstruction cost. If a tie still exists, return the String that comes first lexicographically. If it is impossible to achieve your goal, return "IMPOSSIBLE" (quotes for clarity only).

Definition
    Class:  RoadReconstruction
    Method: selectReconstruction
    Parameters: String[]
    Returns:    String
    Method signature:   String selectReconstruction(String[] roads)
    (be sure your method is public)

Notes
-   There can be more than one road between a pair of cities.


Examples
0)
    {"M1 Moscow Kiev 1", "M2 Minsk Kiev", "M3 Minsk Warsaw"}
    Returns: "M1"
    Rebuilding road M1 will make all three cities connected to each other.
1)
    {"R1 NY Washington", "M1 Moscow StPetersburg 1000"}
    Returns: "IMPOSSIBLE"
    Even after reconstuction of the road M1, the resulting road network won't be connected. So, the answer is "IMPOSSIBLE".
2)
    {"B1 Bratislava Havka"}
    Returns: ""
3)
    {"M1 Moscow StPetersburg 1", "M2 Moscow Saratov 2", "S0 Saratov StPetersburg"}}
    Returns: "M1"
4)
    {"O1 Beetown Fearnot 6","N7 Fearnot Hornytown","M8 Hornytown Belcher 10",
     "L5 Belcher Fearnot 8","C7 Fearnot Beetown 4","K7 Quiggleville Beetown 12",
     "H4 Beetown DryFork 6","Z0 Hornytown Belcher 1","O5 Belcher Quiggleville 10",
     "U7 Quiggleville Fearnot 2","A8 Fearnot Quiggleville 8","T6 Beetown DryFork 17",
     "E8 Quiggleville DryFork 8","Y4 DryFork Quiggleville 4","Q8 Hornytown DryFork 2",
     "J9 Quiggleville DryFork 19","M4 DryFork Quiggleville 7","T1 DryFork Fearnot 9",
     "G4 Fearnot DryFork 6","V9 Hornytown Beetown 5","O6 Quiggleville Beetown 4",
     "L8 Beetown Roachtown 5","D5 Belcher DryFork 8","W5 Belcher DryFork 1"}
    Returns: "C7 L8 U7 W5 Z0"

    # C7 Fearnot Beetown 4, L8 Beetown Roachtown 5, U7 Quiggleville Fearnot 2
    # W5 Belcher DryFork 1, Z0 Hornytown Belcher 1
"""
from disjoint_set import *
def select_reconstruction(roads):
    ds = DisjointSet()

    if len(roads) == 1: return ''

    roads_with_cost, roads_without_cost, all_cities = [], [], []
    all_costs = []

    for road in roads:
        if len(road.split()) == 4:
            roads_with_cost.append(road)
        else:
            roads_without_cost.append(road)

    for road in roads_without_cost:
        id, city1, city2 = road.split()

        all_cities.append(city1)
        all_cities.append(city2)

    for road in roads_with_cost:
        id, city1, city2, cost = road.split()

        all_costs.append(cost)

        all_cities.append(city1)
        all_cities.append(city2)

    all_cities = set(all_cities)

    least_cost = min(all_costs)

    # print roads_with_cost
    # print roads_without_cost
    # print all_cities



    for city in all_cities:
        ds.make_set(city)

    for road in roads_without_cost:
        id, city1, city2 = road.split()

        ds.union(city1, city2)

    for road in roads_with_cost:
        id, city1, city2, cost = road.split()

        ds.union(city1, city2)

    if ds.num_sets > 1:
        return "IMPOSSIBLE"
    elif ds.num_sets == 1:
        result = []
        for road in roads_with_cost:
            id, city1, city2, cost = road.split()

            if cost == least_cost:
                result.append(road)

        if len(result) == 1:
            id, city1, city2, cost = result[0].split()
            return id
            # return [road.split()[0] for raod in result][0]
        else:
            return result



if __name__ == '__main__':
    # print select_reconstruction(["M1 Moscow Kiev 1", "M2 Minsk Kiev", "M3 Minsk Warsaw"])
    # print('\n')
    # print select_reconstruction(["R1 NY Washington", "M1 Moscow StPetersburg 1000"])
    # print('\n')
    # print select_reconstruction(["B1 Bratislava Havka"])
    # print('\n')
    print select_reconstruction(["M1 Moscow StPetersburg 1", "M2 Moscow Saratov 2", "S0 Saratov StPetersburg"])
    print select_reconstruction(["O1 Beetown Fearnot 6","N7 Fearnot Hornytown","M8 Hornytown Belcher 10",
 "L5 Belcher Fearnot 8","C7 Fearnot Beetown 4","K7 Quiggleville Beetown 12",
 "H4 Beetown DryFork 6","Z0 Hornytown Belcher 1","O5 Belcher Quiggleville 10",
 "U7 Quiggleville Fearnot 2","A8 Fearnot Quiggleville 8","T6 Beetown DryFork 17",
 "E8 Quiggleville DryFork 8","Y4 DryFork Quiggleville 4","Q8 Hornytown DryFork 2",
 "J9 Quiggleville DryFork 19","M4 DryFork Quiggleville 7","T1 DryFork Fearnot 9",
 "G4 Fearnot DryFork 6","V9 Hornytown Beetown 5","O6 Quiggleville Beetown 4",
 "L8 Beetown Roachtown 5","D5 Belcher DryFork 8","W5 Belcher DryFork 1"])




