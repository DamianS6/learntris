#!/usr/bin/env python

import sys


class Tetris:

	def __init__(self):
		self.matrix = None
		self.score = 0
		self.cleared_lines = 0
		self.matrix_4x4 = [['.', '.', '.', '.', '\n'] for __ in range(4)]
		self.matrix_3x3 = [['.', '.', '.', '\n'] for __ in range(3)]

	def print_matrix(self):
		if self.matrix:
			print(' '.join(i for r in self.matrix for i in r).rstrip())
		else:
			self.matrix = [['.', '.', '.', '.', '.', '.', '.', '.', '.', '.', '\n']
			               for __ in range(22)]
			print(' '.join(i for r in self.matrix for i in r).rstrip())

	def set_matrix(self):
		self.matrix = []
		for __ in range(22):
			self.matrix.append(f'{input()}\n'.split(' '))

	def clear_matrix(self):
		self.matrix = None

	def show_score(self):
		print(self.score)

	def show_cleared_lines(self):
		print(self.cleared_lines)

	def check_for_full_rows(self):
		"""
		Check each item if it contains only letters, if yes replace it with empty row.
		"""
		for i in range(22):
			if '.' not in self.matrix[i]:
				self.matrix[i] = ['.', '.', '.', '.', '.', '.', '.', '.', '.', '.', '\n']
				self.score += 100
				self.cleared_lines += 1

	def draw_tetraminio(self, kind):
		if kind == 'I':
			tetris.draw_I()
		elif kind == 'O':
			tetris.draw_O()
		elif kind == 'Z':
			tetris.draw_Z()
		elif kind == 'S':
			tetris.draw_S()
		elif kind == 'J':
			tetris.draw_J()
		elif kind == 'L':
			tetris.draw_L()
		elif kind == 'T':
			tetris.draw_T()

	def draw_I(self):
		self.tetramino_I = self.matrix_4x4
		self.tetramino_I[1] = ['c', 'c', 'c', 'c', '\n']
		self.active_tetramino = self.tetramino_I

	def draw_O(self):
		self.tetramino_O = [['y', 'y', '\n']]*2
		self.active_tetramino = self.tetramino_O

	def draw_Z(self):
		self.tetramino_Z = self.matrix_3x3
		self.tetramino_Z[0][:2], self.tetramino_Z[1][1:3] = ('r', 'r'), ('r', 'r')
		self.active_tetramino = self.tetramino_Z

	def draw_S(self):
		self.tetramino_S = self.matrix_3x3
		self.tetramino_S[0][1:3], self.tetramino_S[1][:2] = ('g', 'g'), ('g', 'g')
		self.active_tetramino = self.tetramino_S

	def draw_J(self):
		self.tetramino_J = self.matrix_3x3
		self.tetramino_J[0][0], self.tetramino_J[1][:3] = 'b', ('b', 'b', 'b')
		self.active_tetramino = self.tetramino_J

	def draw_L(self):
		self.tetramino_L = self.matrix_3x3
		self.tetramino_L[0][2], self.tetramino_L[1][:3] = 'o', ('o', 'o', 'o')
		self.active_tetramino = self.tetramino_L

	def draw_T(self):
		self.tetramino_T = self.matrix_3x3
		self.tetramino_T[0][1], self.tetramino_T[1][:3] = 'm', ('m', 'm', 'm')
		self.active_tetramino = self.tetramino_T

	def display_active_tetramino(self):
		if self.active_tetramino is None:
			pass
		else:
			print(' '.join([i for r in self.active_tetramino for i in r]))

	def rotate_clockwise(self):
		self.active_tetramino = list(zip(*self.active_tetramino[::-1]))


tetris = Tetris()


def choose_option(option):
	if option == 'q':
		sys.exit()
	elif option == 'p':
		tetris.print_matrix()
	elif option == 'g':
		tetris.set_matrix()
	elif option == 'c':
		tetris.clear_matrix()
	elif option == '?s':
		tetris.show_score()
	elif option == '?n':
		tetris.show_cleared_lines()
	elif option == 's':
		tetris.check_for_full_rows()
	elif option.isupper():
		tetris.draw_tetraminio(option)
	elif option == 't':
		tetris.display_active_tetramino()
	elif option == ')':
		tetris.rotate_clockwise()

def choose_option_length(answer):
	if len(answer) > 2:
		answer_list = answer.split(' ')
		for i in range(len(answer_list)):
			option = answer_list[i]
			choose_option(option)
	else:
		choose_option(answer)
	choose_option_length(input())


choose_option_length(input())

'''
import sys


class Tetris:

	def __init__(self, matrix='', score=0, cleared_lines=0):
		self.matrix = matrix
		self.score = score
		self.cleared_lines = cleared_lines
		self.active_tetramino, self.tetramino_I, self.tetramino_O,\
		self.tetramino_Z, self.tetramino_S, self.tetramino_J, self.tetramino_L,\
		self.tetramino_T\
			= [None] * 8

	def set_matrix(self):
		self.matrix = ''
		for i in range(22):
			self.matrix += f'{ input() }\n'

	def print_matrix(self):
		if self.matrix:
			print(self.matrix.rstrip())  # remove last newline character
		else:
			self.matrix += f"{'. ' * 10}\n" * 22
			print(self.matrix.rstrip())

	def clear_matrix(self):
		self.matrix = f"{'. ' * 10}\n" * 22

	def show_score(self):
		print(self.score)

	def show_cleared_lines(self):
		print(self.cleared_lines)

	def check_for_full_rows(self):
		"""
		Split matrix into rows and check each one if it's full. Replace matrix
		with new one without full rows if found and with the same one if not.
		Increment score and cleared lines.
		"""
		# TODO: Instead of replacing whole matrix it would be better to replace
		#  only rows - requires creating new separate type (row) and changing
		#  the way in which the matrix is created (most likely with new classes
		#  and methods).
		rows = self.matrix.split('\n')
		self.matrix = ''
		for i in range(22):
			if '.' not in rows[i]:
				rows[i] = '. ' * 10
				self.score += 100
				self.cleared_lines += 1
			self.matrix += f'{rows[i]}\n'
		return self.matrix

	def draw_tetraminio(self, kind):
		if kind == 'I':
			tetris.draw_I()
		elif kind == 'O':
			tetris.draw_O()
		elif kind == 'Z':
			tetris.draw_Z()
		elif kind == 'S':
			tetris.draw_S()
		elif kind == 'J':
			tetris.draw_J()
		elif kind == 'L':
			tetris.draw_L()
		elif kind == 'T':
			tetris.draw_T()

	def draw_I(self):
		self.tetramino_I = (f"{'. ' * 4}\n"
			      f"c c c c\n"
			      f"{'. ' * 4}\n"
			      f"{'. ' * 4}")
		self.active_tetramino = self.tetramino_I

	def draw_O(self):
		self.tetramino_O = 'y y\ny y'
		self.active_tetramino = self.tetramino_O

	def draw_Z(self):
		self.tetramino_Z = 'r r .\n. r r'
		self.active_tetramino = self.tetramino_Z

	def draw_S(self):
		self.tetramino_S = '. g g\ng g .'
		self.active_tetramino = self.tetramino_S

	def draw_J(self):
		self.tetramino_J = 'b . .\nb b b'
		self.active_tetramino = self.tetramino_J

	def draw_L(self):
		self.tetramino_L = '. . o\no o o'
		self.active_tetramino = self.tetramino_L

	def draw_T(self):
		self.tetramino_T = '. m .\nm m m'
		self.active_tetramino = self.tetramino_T

	def display_active_tetramino(self):
		if self.active_tetramino is None:
			pass
		elif self.active_tetramino == self.tetramino_I:
			print(self.tetramino_I)
		elif self.active_tetramino == self.tetramino_O:
			print(self.tetramino_O)
		elif self.active_tetramino == self.tetramino_Z:
			print(f'{self.tetramino_Z}\n. . .')
		elif self.active_tetramino == self.tetramino_S:
			print(f'{self.tetramino_S}\n. . .')
		elif self.active_tetramino == self.tetramino_J:
			print(f'{self.tetramino_J}\n. . .')
		elif self.active_tetramino == self.tetramino_L:
			print(f'{self.tetramino_L}\n. . .')
		elif self.active_tetramino == self.tetramino_T:
			print(f'{self.tetramino_T}\n. . .')
		else:
			print(self.active_tetramino)

	def rotate_active_tetramino(self, count):
		if count == 0:
			self.active_tetramino = ('. . c .\n' * 4).rstrip()
		elif count == 1:
			self.active_tetramino = ('. . . .\n' * 2 + 'c c c c\n' + '. . . .').rstrip()
		elif count == 2:
			self.active_tetramino = ('. c . .\n' * 4).rstrip()
		elif count == 3:
			self.active_tetramino = ('. . . .\n' + 'c c c c\n' + '. . . .\n' * 2).rstrip()
		count += 1


tetris = Tetris()


def choose_option(option, count):
	if option == 'q':
		sys.exit()
	elif option == 'p':
		tetris.print_matrix()
	elif option == 'g':
		tetris.set_matrix()
	elif option == 'c':
		tetris.clear_matrix()
	elif option == '?s':
		tetris.show_score()
	elif option == '?n':
		tetris.show_cleared_lines()
	elif option == 's':
		tetris.check_for_full_rows()
	elif option.isupper():
		tetris.draw_tetraminio(option)
	elif option == 't':
		tetris.display_active_tetramino()
	elif option == ')':
		tetris.rotate_active_tetramino(count)


def choose_option_length(answer, count):
	if len(answer) > 2:
		answer_list = answer.split(' ')
		for i in range(len(answer_list)):
			option = answer_list[i]
			choose_option(option, count)
	else:
		choose_option(answer, count)
	count += 1
	choose_option_length(input(), count)


choose_option_length(input(), 0)
'''