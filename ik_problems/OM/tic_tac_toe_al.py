from os import system
import random

class Board:

    def __init__(self):
        self.winning_lines = [[1, 2, 3], [4, 5, 6], [7, 8, 9], [2, 5, 8], [3, 6, 9], [1, 5, 9], [3, 5, 7]]
        self.data = {}
        for position in range(1, 10):
            self.data[position] = Square(' ')

    def get_empty_squares(self):
        return [v for k, v in self.data.iteritems() if v.check_empty_value()]

    def get_empty_positions(self):
        return [k for k, v in self.data.iteritems() if v.check_empty_value()]

    def all_squares_marked(self):
        return len(self.get_empty_squares()) == 0

    def find_winner(self, marker):
        for winning_line in self.winning_lines:
            if self.data[winning_line[0]].get_value() == marker and self.data[winning_line[1]].get_value() == marker and self.data[winning_line[2]].get_value() == marker:
                return True
            else:
                return False

    def mark_sqaure(self, pos, marker):
        self.data[pos].set_value(marker)

    def draw(self):
        system("clear")
        print ""
        print "     |     |"
        print "  %s  |  %s  |  %s  " % (self.data[1], self.data[2], self.data[3])
        print "     |     |"
        print "-----+-----+-----"
        print "     |     |"
        print "  %s  |  %s  |  %s  " % (self.data[4], self.data[4], self.data[6])
        print "     |     |"
        print "-----+-----+-----"
        print "  %s  |  %s  |  %s  " % (self.data[7], self.data[8], self.data[9])
        print "     |     |"
        print ""



class Player:
    def __init__(self, name, marker):
        self.name = name
        self.marker = marker

    def get_marker(self):
        return self.marker

    def get_name(self):
        return self.name


class Square:
    def __init__(self, value):
        self.value = value

    def get_value(self):
        return self.value

    def check_empty_value(self):
        return self.value == ' '

    def set_value(self, marker):
        self.value = marker

    def __str__(self):
        return str(self.value)

class Game:
    def __init__(self):
        self.board = Board()
        self.human = Player("James", "X")
        self.computer = Player("R2D2", "O")
        self.current_player = self.human

    def make_move(self):
        if self.current_player == self.human:
            print "Choose a position %s to place a piece:" % (self.board.get_empty_positions())
            position = int(raw_input())
            while position not in self.board.get_empty_positions():
                break
        else:
            position = random.choice(self.board.get_empty_positions())
        self.board.mark_sqaure(position, self.current_player.get_marker())

    def alternate_player(self):
        if self.current_player == self.human:
            self.current_player = self.computer
        else:
            self.current_player = self.human

    def declare_winner(self):
        return self.board.find_winner(self.current_player.get_marker())




    def play(self):
        self.board.draw()
        while True:
            self.make_move()
            self.board.draw()
            if self.declare_winner():
                print "The winner is %s!" % (self.current_player.get_name())
                break
            elif self.board.all_squares_marked():
                print "It's a tie"
                break
            else:
                self.alternate_player()
        print "Bye!"

g = Game()
g.play()
