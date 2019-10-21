import numpy
import pylab
import random


class g_o_l:

    def __init__(self, N=100, G=100):

        # N*N start board
        # 1s are alive and 0s are dead
        self.N = N
        self.ex_board = numpy.zeros(N * N, dtype='i').reshape(N, N)
        self.board = numpy.zeros(N * N, dtype='i').reshape(N, N)
        self.G = G  # number of gens

        # Setting up start board
        for i in range(0, self.N):
            for j in range(0, self.N):
                if random.randint(0, 100) < 10:
                    self.ex_board[i][j] = 1
                else:
                    self.ex_board[i][j] = 0

    def neighbours_count(self, i, j):

            count_of_neighbours = 0
            for x in [i - 1, i, i + 1]:
                for y in [j - 1, j, j + 1]:
                    # dont count point's itself but just its neighbours
                    if x == i and y == j:
                        continue
                    if x != self.N and y != self.N:
                        count_of_neighbours += self.ex_board[x][y]

                    elif x == self.N and y != self.N:
                        count_of_neighbours += self.ex_board[0][y]
                    elif x != self.N and y == self.N:
                        count_of_neighbours += self.ex_board[x][0]
                    else:
                        count_of_neighbours += self.ex_board[0][0]
            return count_of_neighbours

    def autorun(self):

        pylab.pcolormesh(self.ex_board)
        pylab.colorbar()
        pylab.savefig("time0.png")

        g = 1
        # if you need every time's picture just set write_frequency to 1
        write_frequency = 3
        while g <= self.G:
            print("At time level %d" % g)

            # Main LOOP for game
            for i in range(self.N):
                for j in range(self.N):
                    numberOfNeighbours = self.neighbours_count(i, j)
                    if self.ex_board[i][j] == 1 and numberOfNeighbours < 2:
                        self.board[i][j] = 0
                    elif self.ex_board[i][j] == 1 and (numberOfNeighbours == 2 or numberOfNeighbours == 3):
                        self.board[i][j] = 1
                    elif self.ex_board[i][j] == 1 and numberOfNeighbours > 3:
                        self.board[i][j] = 0
                    elif self.ex_board[i][j] == 0 and numberOfNeighbours == 3:
                        self.board[i][j] = 1

            if g % write_frequency == 0:
                pylab.pcolormesh(self.board)
                pylab.savefig("time%d.png" % g)

            self.ex_board = self.board.copy()

            # go next
            g += 1


if __name__ == "__main__":
    game_of_life = g_o_l(N=100, G=100)
    game_of_life.autorun()