__author__ = 'Ravil'

from pacman import *

from util import *

from search import *

# State is tuple where in [0] row and in [1] is column
class Succesor:

    def __init__(self, action, succesor_state):
        self.action = action

        self.succesor_state = succesor_state

class PacmanSearchProblem:

    def __init__(self, start_state, level, dots):
        self.start_state = start_state

        self.level = level

        self.dots = dots

    def get_start_state(self):
        return self.start_state

    def get_succesors(self, state):
        succesors = []

        if self.level.level[state[0]][state[1] + 1] != "-":
            row = state[0]
            column = state[1] + 1

            new_state = (row, column)

            succesors.append(Succesor(PACMAN_GO_RIGHT_ACTION, new_state))

        if self.level.level[state[0]][state[1] - 1] != "-":
            row = state[0]
            column = state[1] - 1

            new_state = (row, column)

            succesors.append(Succesor(PACMAN_GO_LEFT_ACTION, new_state))

        if self.level.level[state[0] - 1][state[1]] != "-":
            row = state[0] - 1
            column = state[1]

            new_state = (row, column)

            succesors.append(Succesor(PACMAN_GO_UP_ACTION, new_state))

        if self.level.level[state[0] + 1][state[1]] != "-":
            row = state[0] + 1
            column = state[1]

            new_state = (row, column)

            succesors.append(Succesor(PACMAN_GO_DOWN_ACTION, new_state))

        return succesors

    def is_goal_state(self, state):
        if state[0] == 15 and state[1] == 23:
            return True
        else:
            return False

    def get_actions_cost(self, actions):
        return len(actions)

class ProblemSolvingAgent:

    def __init__(self, pacman, level, dots):
        self.pacman = pacman

        self.dots = dots

        self.problem = PacmanSearchProblem((1, 1), level, dots)

        self.actions = deep_first_search(self.problem)


    def execute_next_action(self):
        if not self.actions.isEmpty():
            self.pacman.update(self.actions.pop(), [], self.dots)
