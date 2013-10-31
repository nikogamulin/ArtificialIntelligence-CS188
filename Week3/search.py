# search.py
# ---------
# Licensing Information: Please do not distribute or publish solutions to this
# project. You are free to use and extend these projects for educational
# purposes. The Pacman AI projects were developed at UC Berkeley, primarily by
# John DeNero (denero@cs.berkeley.edu) and Dan Klein (klein@cs.berkeley.edu).
# Student side autograding was added by Brad Miller, Nick Hay, and Pieter 
# Abbeel in Spring 2013.
# For more info, see http://inst.eecs.berkeley.edu/~cs188/pacman/pacman.html

"""
In search.py, you will implement generic search algorithms which are called
by Pacman agents (in searchAgents.py).
"""

import util
import copy

class SearchProblem:
    """
    This class outlines the structure of a search problem, but doesn't implement
    any of the methods (in object-oriented terminology: an abstract class).

    You do not need to change anything in this class, ever.
    """

    def getStartState(self):
        """
        Returns the start state for the search problem
        """
        util.raiseNotDefined()

    def isGoalState(self, state):
        """
          state: Search state

        Returns True if and only if the state is a valid goal state
        """
        util.raiseNotDefined()

    def getSuccessors(self, state):
        """
          state: Search state

        For a given state, this should return a list of triples,
        (successor, action, stepCost), where 'successor' is a
        successor to the current state, 'action' is the action
        required to get there, and 'stepCost' is the incremental
        cost of expanding to that successor
        """
        util.raiseNotDefined()

    def getCostOfActions(self, actions):
        """
         actions: A list of actions to take

        This method returns the total cost of a particular sequence of actions.  The sequence must
        be composed of legal moves
        """
        util.raiseNotDefined()


def tinyMazeSearch(problem):
    """
    Returns a sequence of moves that solves tinyMaze.  For any other
    maze, the sequence of moves will be incorrect, so only use this for tinyMaze
    """
    from game import Directions
    s = Directions.SOUTH
    w = Directions.WEST
    return  [s,s,w,s,w,w,s,w]

def depthFirstSearch(problem):
    
    fringe = util.Stack()
    startState=problem.getStartState()
    fringe.push((startState, [],[]))
    
    while not fringe.isEmpty():
        node, actions, visited = fringe.pop()
        
        for coord, direction, steps in problem.getSuccessors(node):
            if not coord in visited:
                if problem.isGoalState(coord):
                    return actions + [direction]
                fringe.push((coord, actions + [direction], visited + [node]))
    return []
    

def breadthFirstSearch(problem):
    
    exploredNodes = []
    fringe = util.PriorityQueue()
    startState=problem.getStartState()
    fringe.push((startState, []), 1)
    exploredNodes.append(startState)
    
    while not fringe.isEmpty():
        node, actions = fringe.pop()
        if problem.isGoalState(node):
            return actions
        for coord, direction, steps in problem.getSuccessors(node):
            if not coord in exploredNodes:
                fringe.push((coord, actions + [direction]), len(actions) + 1)
                exploredNodes.append(coord)
        
        
        

def uniformCostSearch(problem):
    
    exploredNodes = []
    fringe = util.PriorityQueue()
    startState=problem.getStartState()
    fringe.push((startState, []), 1)
    #exploredNodes.append(startState)
    
    while not fringe.isEmpty():
        node, actions = fringe.pop()
        if problem.isGoalState(node):
            return actions
        exploredNodes.append(node)
        for coord, direction, steps in problem.getSuccessors(node):
            if not coord in exploredNodes:
                newActions = actions + [direction]
                newActionsCost = problem.getCostOfActions(newActions)
                fringe.push((coord, actions + [direction]), newActionsCost)
                exploredNodes.append(coord)
                
    return[]

def nullHeuristic(state, problem=None):
    """
    A heuristic function estimates the cost from the current state to the nearest
    goal in the provided SearchProblem.  This heuristic is trivial.
    """
    return 0

def aStarSearch(problem, heuristic=nullHeuristic):
    
    closedSet = []
    fringe = util.PriorityQueue()
    start = problem.getStartState()
    fringe.push((start, []), heuristic(start, problem))
    
    while not fringe.isEmpty():
        node, actions = fringe.pop()
        
        if problem.isGoalState(node):
            return actions
        closedSet.append(node)
        
        for coord, direction, cost in problem.getSuccessors(node):
            if not coord in closedSet:
                newActions = actions + [direction]
                score = problem.getCostOfActions(newActions) + heuristic(coord, problem)
                fringe.push((coord, newActions), score)


# Abbreviations
bfs = breadthFirstSearch
dfs = depthFirstSearch
astar = aStarSearch
ucs = uniformCostSearch
