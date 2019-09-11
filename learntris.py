#!/usr/bin/env python


class Tetris:

	def __init__(self, matrix='', score=0, cleared_lines=0):
		self.matrix = matrix
		self.score = score
		self.cleared_lines = cleared_lines
		self.active_tetramino, self.tetramino_I, self.tetramino_O = None, None, None

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

	def draw_tetramino_I(self):
		self.tetramino_I = 'c c c c'
		self.active_tetramino = self.tetramino_I

	def draw_tetramino_O(self):
		self.tetramino_O = 'y y\ny y'
		self.active_tetramino = self.tetramino_O

	def display_active_tetramino(self):
		if self.active_tetramino == self.tetramino_I:
			print(f"{'. ' * 4}\n"
			      f"{self.active_tetramino}\n"
			      f"{'. ' * 4}\n"
			      f"{'. ' * 4}")
		elif self.active_tetramino == self.tetramino_O:
			print(self.tetramino_O)


tetris = Tetris()
option = input()

while option != 'q':
	if option == 'p':
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
		tetris.draw_tetramino_I()
	elif option == 'O':
		tetris.draw_tetramino_O()
	elif option == 't':
		tetris.display_active_tetramino()
	option = input()