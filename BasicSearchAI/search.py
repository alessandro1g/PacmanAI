# search.py
# ---------
# Licensing Information:  You are free to use or extend these projects for
# educational purposes provided that (1) you do not distribute or publish
# solutions, (2) you retain this notice, and (3) you provide clear
# attribution to UC Berkeley, including a link to http://ai.berkeley.edu.
# 
# Attribution Information: The Pacman AI projects were developed at UC Berkeley.
# The core projects and autograders were primarily created by John DeNero
# (denero@cs.berkeley.edu) and Dan Klein (klein@cs.berkeley.edu).
# Student side autograding was added by Brad Miller, Nick Hay, and
# Pieter Abbeel (pabbeel@cs.berkeley.edu).


"""
In search.py, you will implement generic search algorithms which are called by
Pacman agents (in searchAgents.py).
"""

import util

class SearchProblem:
    """
    This class outlines the structure of a search problem, but doesn't implement
    any of the methods (in object-oriented terminology: an abstract class).

    You do not need to change anything in this class, ever.
    """

    def getStartState(self):
        """
        Returns the start state for the search problem.
        """
        util.raiseNotDefined()

    def isGoalState(self, state):
        """
          state: Search state

        Returns True if and only if the state is a valid goal state.
        """
        util.raiseNotDefined()

    def getSuccessors(self, state):
        """
          state: Search state

        For a given state, this should return a list of triples, (successor,
        action, stepCost), where 'successor' is a successor to the current
        state, 'action' is the action required to get there, and 'stepCost' is
        the incremental cost of expanding to that successor.
        """
        util.raiseNotDefined()

    def getCostOfActions(self, actions):
        """
         actions: A list of actions to take

        This method returns the total cost of a particular sequence of actions.
        The sequence must be composed of legal moves.
        """
        util.raiseNotDefined()


def tinyMazeSearch(problem):
    """
    Returns a sequence of moves that solves tinyMaze.  For any other maze, the
    sequence of moves will be incorrect, so only use this for tinyMaze.
    """
    from game import Directions
    s = Directions.SOUTH
    w = Directions.WEST
    return  [s, s, w, s, w, w, s, w]
    


def depthFirstSearch(problem):
    """
    Search the deepest nodes in the search tree first.

    Your search algorithm needs to return a list of actions that reaches the
    goal. Make sure to implement a graph search algorithm.

    To get started, you might want to try some of these simple commands to
    understand the search problem that is being passed in:

    print("Start:", problem.getStartState())
    print("Is the start a goal?", problem.isGoalState(problem.getStartState()))
    print("Start's successors:", problem.getSuccessors(problem.getStartState()))
    """
    "*** YOUR CODE HERE ***"

    start = problem.getStartState()
    print(start)
    print("here")
    #pathStack = util.Stack() 
    pathStack = util.Stack()
    visited = set()
    retStack = [] 
    flag = [True]

    if problem.isGoalState(problem.getStartState()):
        flag = [False]
        return []

    pathStack.push((start,[]))

    #iteration, I tried doing it recursively but kept getting the same result as I would get if I were doing it in reverse
    #order, so imma try doing it iteratively

    while not pathStack.isEmpty():
        currentNode, actionList = pathStack.pop()
        if problem.isGoalState(currentNode):
            retStack = actionList
            break


        if currentNode not in visited:
            visited.add(currentNode)

            successors = problem.getSuccessors(currentNode)

            for successor, action, stepCost in successors:
                nActions = actionList + [action]
                pathStack.push((successor,nActions))

    return actionList


    

    """
    def dfsHelper(current):
        #print(currNode)
        visited.add(current)
        if problem.isGoalState(current):
            print("found spot")
            flag[0] = False

            return pathStack
        successors = problem.getSuccessors(current) 
        for successor, action, cost in successors:
            if successor not in visited and flag[0]:
                if flag[0]:
                    
                    pathStack.push(action) 
                    
                    dfsHelper(successor) 
                    #print(pathStack)
                    if flag[0]:
                        pathStack.pop()

        #print(successors)

    for val in pathStack:
        retStack.append(val)

        
    
    dfsHelper(start)
    print(retStack)
    """

def breadthFirstSearch(problem):
    """Search the shallowest nodes in the search tree first.""" 
    "*** YOUR CODE HERE ***" 
    pathQueue = util.Queue()
    start = problem.getStartState()
    visited = set()
    retStack = [] 
    flag = [True]

    #print("start: " + str(start))

    '''
    if problem.isGoalState(problem.getStartState()):
        flag = [False]
        return []
    '''

    pathQueue.push((start,[],0)) 
    #print("Queue: " + str(pathQueue))

    while not pathQueue.isEmpty(): 
        currNode,actionLst,cost = pathQueue.pop() 
        #print(currNode)
        if currNode not in visited: 
            visited.add(currNode) 
            if problem.isGoalState(currNode): 
                return actionLst 
            
            successors = problem.getSuccessors(currNode) 
            #print("successors:" + str(successors))

            for successor, action, stepCost in successors:
                #print(str(pathQueue))
                #print(successor)
                pathQueue.push((successor,actionLst + [action],stepCost+cost) )

    
    #print(visited)
    #print(actionLst)
    return actionLst
    

    

def uniformCostSearch(problem):
    """Search the node of least total cost first."""
    "*** YOUR CODE HERE ***"
    pqPath = util.PriorityQueue() 
    start = problem.getStartState()
    visited = set()

    if problem.isGoalState(problem.getStartState()):
        flag = [False]
        return []

    pqPath.push((start,1,[]),0) #coords, cost, path

    while not pqPath.isEmpty():
        currNode, cost, actionLst = pqPath.pop() 
        if problem.isGoalState(currNode): 
            
            return actionLst 
        
        print("visited: "+ str(visited))
        if currNode not in visited:
            visited.add(currNode)
            successors = problem.getSuccessors(currNode) 

            for successor, action, stepCost in successors:
                nAction = actionLst + [action]
                nCost = problem.getCostOfActions(nAction)
                pqPath.push((successor,nCost,actionLst + [action]),stepCost+cost)

    print(visited)
    return action



def nullHeuristic(state, problem=None):
    """
    A heuristic function estimates the cost from the current state to the nearest
    goal in the provided SearchProblem.  This heuristic is trivial.
    """
    return 0

def aStarSearch(problem, heuristic=nullHeuristic): 
    """Search the node that has the lowest combined cost and heuristic first."""
    "*** YOUR CODE HERE ***" 
    
    #from psuedocode
    pqPath = util.PriorityQueue() 
    start = problem.getStartState()
    visited = []
    actionList = []

    if problem.isGoalState(problem.getStartState()):
        flag = [False]
        return []

    pqPath.push((start,[]),heuristic(start,problem)) #coords, cost, path

    while not pqPath.isEmpty():
        curr, actions = pqPath.pop()
        if curr not in visited: 
            visited.append(curr) 
            if problem.isGoalState(curr):
                return actions

            successors = problem.getSuccessors(curr)
            for successor, action, stepCost in successors:
                nextActions = actions + [action] 
                nextCost = problem.getCostOfActions(nextActions) + heuristic(successor, problem)
                pqPath.push((successor, nextActions), nextCost)

    return actions 


    
# Abbreviations
bfs = breadthFirstSearch
dfs = depthFirstSearch
astar = aStarSearch
ucs = uniformCostSearch
