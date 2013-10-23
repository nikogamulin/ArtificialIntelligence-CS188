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
    """
    Search the deepest nodes in the search tree first

    Your search algorithm needs to return a list of actions that reaches
    the goal.  Make sure to implement a graph search algorithm

    To get started, you might want to try some of these simple commands to
    understand the search problem that is being passed in:
    """

    print "Start:", problem.getStartState()
    print "Is the start a goal?", problem.isGoalState(problem.getStartState())
    print "Start's successors:", problem.getSuccessors(problem.getStartState())
    
    reachedGoal=False
    exploredAll=False
    
    priorityQueue = util.PriorityQueue()
    exploredPaths = []
    potentialPaths = []
    actionPlan = []
    exploredNodes = []
    startState=problem.getStartState()
    priorityQueue.push([startState], -1)
    potentialPaths.append([startState])
    while reachedGoal == False:
        
        #fill priority queue
        #for path in potentialPaths:
        #    pathAlreadyExplored = path in exploredPaths
        #    if pathAlreadyExplored == False:
        #        priorityQueue.push(path, len(path)*(-1))
        #pick the item with highest priority from the queue
        pathWithHighestPriority = priorityQueue.pop()
        exploredNodes[:] = []
        actionPlan[:] = []
        exploredNodes.append(startState)
        #check if path contains goal state
        iterPathWithHighestPriority = iter(pathWithHighestPriority)
        next(iterPathWithHighestPriority)
        for node in iterPathWithHighestPriority:
            reachedGoal = problem.isGoalState(node[0])
            actionPlan.append(node[1])
            if reachedGoal == True:
                #get action states
                return actionPlan
            exploredNodes.append(node[0])
        
        #if goal hasn't been reached keep searching
        lastNode = pathWithHighestPriority[-1]
        if lastNode == startState:
            successorNodes = problem.getSuccessors(lastNode)
        else:
            successorNodes = problem.getSuccessors(lastNode[0])
        nodesToExplore = []
        for currentNode in successorNodes:
            currentNodeInExploredNodes = currentNode[0] in exploredNodes
            #Don't allow to go backwards
            if currentNodeInExploredNodes == False:
                    nodesToExplore.append(currentNode)
        if len(nodesToExplore) > 0:
            for currentNode in nodesToExplore:
                potentialPath = pathWithHighestPriority[:]
                potentialPath.append(currentNode)
                if nodesToExplore.index(currentNode) == 0:
                    #priorityQueue.heap.remove(pathWithHighestPriority)
                    priorityQueue.push(potentialPath, len(potentialPath) * (-1))
                else:
                    potentialPaths.append(potentialPath)
        else:
            exploredPaths.append(pathWithHighestPriority)
            for currentPath in potentialPaths:
                priorityQueue.push(currentPath, len(currentPath) * (-1))
                #priorityQueue.heap.remove(pathWithHighestPriority)
        
    
  
    
    
    #util.raiseNotDefined()
    

def breadthFirstSearch(problem):
    """
    Search the shallowest nodes in the search tree first.
    """
    "*** YOUR CODE HERE ***"
    util.raiseNotDefined()

def uniformCostSearch(problem):
    "Search the node of least total cost first. "
    "*** YOUR CODE HERE ***"
    util.raiseNotDefined()

def nullHeuristic(state, problem=None):
    """
    A heuristic function estimates the cost from the current state to the nearest
    goal in the provided SearchProblem.  This heuristic is trivial.
    """
    return 0

def aStarSearch(problem, heuristic=nullHeuristic):
    "Search the node that has the lowest combined cost and heuristic first."
    "*** YOUR CODE HERE ***"
    util.raiseNotDefined()


# Abbreviations
bfs = breadthFirstSearch
dfs = depthFirstSearch
astar = aStarSearch
ucs = uniformCostSearch
