#!/usr/bin/env python3

from Lines import METRO, _6

class Station(object):
    def __init__(self, name, id, physical_ids, lines):
        self.name = name
        self.id = id
        self.physical_ids = physical_ids
        self.lines = lines

    def getPhysicalId(self, direction, line):
        if direction not in [1, 2]:
            raise ValueError(f"Expected direction to be either 1 or 2, got '{direction}'")
        if line not in self.lines:
            raise ValueError(f"Line '{line.name}' does not have this station.")
        index = self.lines.index(line)
        return self.physical_ids[index][direction - 1]

EUROPE = Station("europe", 209, ((100769, 100770), (100771, 100772)), (METRO, _6))

if __name__ == "__main__":
    print(EUROPE.getPhysicalId(1, METRO))
    print(EUROPE.getPhysicalId(1, _6))