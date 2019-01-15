# Given a robot cleaner in a room modeled as a grid.
#
# Each cell in the grid can be empty or blocked.
#
# The robot cleaner with 4 given APIs can move forward, turn left or turn right. Each turn it made is 90 degrees.
#
# When it tries to move into a blocked cell, its bumper sensor detects the obstacle and it stays on the current cell.
#
# Design an algorithm to clean the entire room using only the 4 given APIs shown below.
#
# interface Robot {
#   // returns true if next cell is open and robot moves into the cell.
#   // returns false if next cell is obstacle and robot stays on the current cell.
#   boolean move();
#
#   // Robot will stay on the same cell after calling turnLeft/turnRight.
#   // Each turn will be 90 degrees.
#   void turnLeft();
#   void turnRight();
#
#   // Clean the current cell.
#   void clean();
# }
# Example:
#
# Input:
# room = [
#   [1,1,1,1,1,0,1,1],
#   [1,1,1,1,1,0,1,1],
#   [1,0,1,1,1,1,1,1],
#   [0,0,0,1,0,0,0,0],
#   [1,1,1,1,1,1,1,1]
# ],
# row = 1,
# col = 3
#
# Explanation:
# All grids in the room are marked by either 0 or 1.
# 0 means the cell is blocked, while 1 means the cell is accessible.
# The robot initially starts at the position of row=1, col=3.
# From the top left corner, its position is one row below and three columns right.
# Notes:
#
# The input is only given to initialize the room and the robot's position internally. You must solve this problem "blindfolded". In other words, you must control the robot using only the mentioned 4 APIs, without knowing the room layout and the initial robot's position.
# The robot's initial position will always be in an accessible cell.
# The initial direction of the robot will be facing up.
# All accessible cells are connected, which means the all cells marked as 1 will be accessible by the robot.
# Assume all four edges of the grid are all surrounded by wall.

# """
# This is the robot's control interface.
# You should not implement it, or speculate about its implementation
# """
#class Robot:
#    def move(self):
#        """
#        Returns true if the cell in front is open and robot moves into the cell.
#        Returns false if the cell in front is blocked and robot stays in the current cell.
#        :rtype bool
#        """
#
#    def turnLeft(self):
#        """
#        Robot will stay in the same cell after calling turnLeft/turnRight.
#        Each turn will be 90 degrees.
#        :rtype void
#        """
#
#    def turnRight(self):
#        """
#        Robot will stay in the same cell after calling turnLeft/turnRight.
#        Each turn will be 90 degrees.
#        :rtype void
#        """
#
#    def clean(self):
#        """
#        Clean the current cell.
#        :rtype void
#        """

class Solution:
    def cleanRoom(self, robot):
        """
        :type robot: Robot
        :rtype: None
        """

        def addPos(pos, ori):
            return (pos[0] + ori[0], pos[1] + ori[1])

        class RobotWrapper(object):
            def __init__(self, robot):
                self.robot = robot
                self.orientation = (0, 1)
                self.ori = 0
                self.pos = (0, 0)
                self.possOrientations = [(0, 1), (1, 0), (0, -1), (-1, 0)]

            def move(self):
                if self.robot.move():
                    self.pos = addPos(self.pos, self.orientation)
                    return True
                return False

            def turnLeft(self):
                self.ori = (self.ori + 1) % 4
                self.orientation = self.possOrientations[self.ori]
                self.robot.turnLeft()

            def turnRight(self):
                self.ori = (self.ori - 1) % 4
                self.orientation = self.possOrientations[self.ori]
                self.robot.turnRight()

            def clean(self):
                self.robot.clean()

        def dfs(robot, visited):
            robot.clean()
            for i in range(4):
                robot.turnRight()
                newPos = addPos(robot.pos, robot.orientation)
                if newPos not in visited and robot.move():
                    visited.add(robot.pos)
                    dfs(robot, visited)
                    robot.turnLeft()
                    robot.turnLeft()
                    robot.move()
                    robot.turnLeft()
                    robot.turnLeft()

        robotWrapper = RobotWrapper(robot)
        dfs(robotWrapper, set([(0, 0)]))