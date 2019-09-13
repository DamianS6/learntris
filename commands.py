#!/usr/bin/env python

# TODO: Split Tetris class into two (Matrix and Tetramino?) as it's getting long.


class Tetris:

	def __init__(self):
		self.matrix = None
		self.score = 0
		self.cleared_lines = 0
		self.matrix_4x4 = [['.', '.', '.', '.'] for __ in range(4)]  # For I tetramino
		self.matrix_3x3 = [['.', '.', '.'] for __ in range(3)]  # For most tetraminos
		self.replace = 0  # Variable to move tetraminos easier
		self.tetramino_Z, self. tetramino_I, self.tetramino_O, self.tetramino_J, \
		self.tetramino_L, self.tetramino_S, self.tetramino_T, self.active_tetramino =\
			[None] * 8

	def print_matrix(self):
		if self.matrix:
			for i in range(22):
				# No nested comprehension to avoid adding \n manually.
				print(' '.join(d for d in self.matrix[i]).rstrip())
		else:
			self.matrix = [['.', '.', '.', '.', '.', '.', '.', '.', '.', '.']
			               for __ in range(22)]
			for i in range(22):
				print(' '.join(d for d in self.matrix[i]).rstrip())

	def set_matrix(self):
		self.matrix = []
		for __ in range(22):
			# Split at the end to eliminate additional whitespace.
			self.matrix.append(f'{input()}'.split(' '))

	def clear_matrix(self):
		self.matrix = [['.', '.', '.', '.', '.', '.', '.', '.', '.', '.']
		               for __ in range(22)]

	def show_score(self):
		print(self.score)

	def show_cleared_lines(self):
		print(self.cleared_lines)

	def check_for_full_rows(self):
		"""Check each item if it contains only letters,
		if yes replace it with empty row.
		"""
		for i in range(22):
			if '.' not in self.matrix[i]:
				self.matrix[i] = ['.', '.', '.', '.', '.', '.', '.', '.', '.', '.']
				self.score += 100
				self.cleared_lines += 1

	# TODO: Maybe write one class with inheritance for all tetraminos?
	#  Not sure if it would make any sense here.
	def draw_I(self):
		self.tetramino_I = self.matrix_4x4
		self.tetramino_I[1] = ['C', 'C', 'C', 'C']
		self.active_tetramino = self.tetramino_I

	def draw_O(self):
		self.tetramino_O = [['Y', 'Y']]*2
		self.active_tetramino = self.tetramino_O

	def draw_Z(self):
		self.tetramino_Z = self.matrix_3x3
		self.tetramino_Z[0][:2], self.tetramino_Z[1][1:3] = ('R', 'R'), ('R', 'R')
		self.active_tetramino = self.tetramino_Z

	def draw_S(self):
		self.tetramino_S = self.matrix_3x3
		self.tetramino_S[0][1:3], self.tetramino_S[1][:2] = ('G', 'G'), ('G', 'G')
		self.active_tetramino = self.tetramino_S

	def draw_J(self):
		self.tetramino_J = self.matrix_3x3
		self.tetramino_J[0][0], self.tetramino_J[1][:3] = 'B', ('B', 'B', 'B')
		self.active_tetramino = self.tetramino_J

	def draw_L(self):
		self.tetramino_L = self.matrix_3x3
		self.tetramino_L[0][2], self.tetramino_L[1][:3] = 'O', ('O', 'O', 'O')
		self.active_tetramino = self.tetramino_L

	def draw_T(self):
		self.tetramino_T = self.matrix_3x3
		self.tetramino_T[0][1], self.tetramino_T[1][:3] = 'M', ('M', 'M', 'M')
		self.active_tetramino = self.tetramino_T

	def print_matrix_with_tetramino(self):
		tetra_len = len(self.active_tetramino)  # length of tetramino's matrix
		self.replace += int((10 - tetra_len)/2)  # place in row from which we draw tetramino
		for i in range(tetra_len):
			# in every row's middle replace dots with tetramino's letters
			self.matrix[i][self.replace:self.replace+tetra_len] = self.active_tetramino[i]
		Tetris.print_matrix(self)

	def display_active_tetramino(self):
		for i in range(len(self.active_tetramino)):
			print(' '.join([d for d in self.active_tetramino[i]]).lower())

	def rotate_clockwise(self):
		"""Rotate array by first reversing upper list (matrix),
		then unpacking it's items (rows) and in the end zipping them.
		"""
		self.active_tetramino = list(zip(*self.active_tetramino[::-1]))

	def nudge_left(self):
		"""Draw tetramino one place to the left..."""
		self.replace -= 1

	def nudge_right(self):
		"""...and one place to the right."""
		self.replace += 1

	def nudge_down(self):
		pass
