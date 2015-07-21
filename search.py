__author__ = 'Ravil'

from util import *

from pacman import *


class Node:
    def __init__(self, state, parent_node, action):
        self.state = state

        self.parent_node = parent_node

        #  Action which was executed for get state
        self.action = action


def deep_first_search(search_problem):
    closed = set()

    queue = Queue()
    queue.push(Node(search_problem.get_start_state(), None, None))

    while not queue.isEmpty():
        node = queue.pop()

        print(node.state)

        if search_problem.is_goal_state(node.state):
            return solution(node)

        if node.state not in closed:
            closed.add(node.state)

            expanded_nodes = expand_node(node, search_problem)

            for n in expanded_nodes:
                queue.push(n)


def expand_node(node, search_problem):
    nodes = []

    succesors = search_problem.get_succesors(node.state)

    for succesor in succesors:
        nodes.append(Node(succesor.succesor_state, node, succesor.action))

    return nodes


def solution(node):
    solution_actions = Stack()

    stepper = node

    while stepper is not None:
        i = 0

        while i < 4:
            solution_actions.push(stepper.action)
            i += 1

        stepper = stepper.parent_node

    return solution_actions
