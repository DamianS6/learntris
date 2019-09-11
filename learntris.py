#!/usr/bin/env python


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

	def draw_I(self):
		self.tetramino_I = 'c c c c'
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
			print(f"{'. ' * 4}\n"
			      f"{self.active_tetramino}\n"
			      f"{'. ' * 4}\n"
			      f"{'. ' * 4}")
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


tetris = Tetris()


# TODO: Put together two parts of this function to make it way shorter.
def choose_option(answer):
	if len(answer) > 2:
		answer_list = answer.split(' ')
		for i in range(len(answer_list)):
			option = answer_list[i]
			if option == 'q':
				return None
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
			# TODO: To shorten the code here, replace all below with one method
			#  (draw tetramino), transfer input to that method in the class
			#  and choose there what to draw.
			elif option == 'I':
				tetris.draw_I()
			elif option == 'O':
				tetris.draw_O()
			elif option == 'Z':
				tetris.draw_Z()
			elif option == 'S':
				tetris.draw_S()
			elif option == 'J':
				tetris.draw_J()
			elif option == 'L':
				tetris.draw_L()
			elif option == 'T':
				tetris.draw_T()
			elif option == 't':
				tetris.display_active_tetramino()
	else:
		if answer == 'q':
			return None
		elif answer == 'p':
			tetris.print_matrix()
		elif answer == 'g':
			tetris.set_matrix()
		elif answer == 'c':
			tetris.clear_matrix()
		elif answer == '?s':
			tetris.show_score()
		elif answer == '?n':
			tetris.show_cleared_lines()
		elif answer == 's':
			tetris.check_for_full_rows()
		# TODO: To shorten the code here, replace all below with one method
		#  (draw tetramino), transfer input to that method in the class
		#  and choose there what to draw.
		elif answer == 'I':
			tetris.draw_I()
		elif answer == 'O':
			tetris.draw_O()
		elif answer == 'Z':
			tetris.draw_Z()
		elif answer == 'S':
			tetris.draw_S()
		elif answer == 'J':
			tetris.draw_J()
		elif answer == 'L':
			tetris.draw_L()
		elif answer == 'T':
			tetris.draw_T()
		elif answer == 't':
			tetris.display_active_tetramino()
		choose_option(input())


choose_option(input())
