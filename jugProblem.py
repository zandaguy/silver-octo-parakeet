class TupleSearcher:
    def __init__(self, initial_state, goal_state, jug1size, jug2size):
        jug1 = Jug(jug1size)
        jug2 = Jug(jug2size)
        self.initial_state = (0, 0)
        self.current_state = self.initial_state
        self.goal_states = set()
        for num in range(jug1.size+1):
            self.goal_states.add((goal_state, num))
        for num in range(jug2.size+1):
            self.goal_states.add((num, goal_state))

    def display_goal_states(self):
        print self.goal_states

    def empty(jug):
        jug.size = 0

    def pour(jug1, jug2):
        self.current_state[jug2] = self.current_state[jug2] + (self.current_state[jug1] - self.current_state[jug2])

class Jug:
    def __init__(self, size):
        self.size = size

def main():
    searcher = TupleSearcher((0,0), 1, 3, 5)

    searcher.display_goal_states()

if __name__ == '__main__':
    main()
