#!/usr/bin/env python

# TODO: Split Tetris class into two (Matrix and Tetramino?) as it's getting long.


class Tetris:

	def __init__(self):
		self.matrix = [['.', '.', '.', '.', '.', '.', '.', '.', '.', '.']
		               for __ in range(22)]
		self.matrix_4x4 = [['.', '.', '.', '.'] for __ in range(4)]  # For I tetramino.
		self.matrix_3x3 = [['.', '.', '.'] for __ in range(3)]  # For most tetraminos.

		self.score, self.cleared_lines = 0, 0
		self.horizontal, self.vertical = 0, 0  # Tetraminos position variables.

		self.tetramino_Z, self. tetramino_I, self.tetramino_O, self.tetramino_J, \
		self.tetramino_L, self.tetramino_S, self.tetramino_T, self.active_tetramino =\
			[None] * 8

	def prepare_matrix(self, option):
		if self.active_tetramino:
			Tetris.clear_matrix(self)
			tetra_len = len(self.active_tetramino)  # Length of tetramino's matrix.
			h, v = self.horizontal, self.vertical
			for i in range(tetra_len):
				# In every row's middle replace dots with tetramino's letters.
				if i + v < 22:
					self.matrix[i + v][h:h + tetra_len] = self.active_tetramino[i]
					# Delete any additional items in row if they somehow happen to exist.
					if len(self.matrix[i + v]) > 10:
						del self.matrix[i + v][-1]
			Tetris.print_matrix(self, option)
		elif self.matrix:
			Tetris.print_matrix(self, option)
		else:
			self.matrix = [['.', '.', '.', '.', '.', '.', '.', '.', '.', '.']
			               for __ in range(22)]
			Tetris.print_matrix(self, option)

	def print_matrix(self, option):
		for i in range(22):
			# No nested comprehension to avoid adding newlines as list items.
			if option == 'up':
				print(' '.join(d for d in self.matrix[i]).rstrip())
			else:
				print(' '.join(d for d in self.matrix[i]).rstrip().lower())

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
	#  However not sure if it makes any sense here.

	def draw_I(self):
		self.tetramino_I = self.matrix_4x4
		self.tetramino_I[1] = ['C', 'C', 'C', 'C']
		self.active_tetramino = self.tetramino_I
		self.horizontal = 3

	def draw_O(self):
		self.tetramino_O = [['Y', 'Y']] * 2
		self.active_tetramino = self.tetramino_O
		self.horizontal = 4

	def draw_Z(self):
		self.tetramino_Z = self.matrix_3x3
		self.tetramino_Z[0][:2], self.tetramino_Z[1][1:3] = ('R', 'R'), ('R', 'R')
		self.active_tetramino = self.tetramino_Z
		self.horizontal = 3

	def draw_S(self):
		self.tetramino_S = self.matrix_3x3
		self.tetramino_S[0][1:3], self.tetramino_S[1][:2] = ('G', 'G'), ('G', 'G')
		self.active_tetramino = self.tetramino_S
		self.horizontal = 3

	def draw_J(self):
		self.tetramino_J = self.matrix_3x3
		self.tetramino_J[0][0], self.tetramino_J[1][:3] = 'B', ('B', 'B', 'B')
		self.active_tetramino = self.tetramino_J
		self.horizontal = 3

	def draw_L(self):
		self.tetramino_L = self.matrix_3x3
		self.tetramino_L[0][2], self.tetramino_L[1][:3] = 'O', ('O', 'O', 'O')
		self.active_tetramino = self.tetramino_L
		self.horizontal = 3

	def draw_T(self):
		self.tetramino_T = self.matrix_3x3
		self.tetramino_T[0][1], self.tetramino_T[1][:3] = 'M', ('M', 'M', 'M')
		self.active_tetramino = self.tetramino_T
		self.horizontal = 3

	def active_tetramino_length(self):
		for row in self.active_tetramino:
			count = 0
			for item in row:
				count += 1 if item != '.' else 0
			if count >= 2:
				return count

	def active_tetramino_height(self):
		count = 0
		for row in self.active_tetramino:
			if row != ['.'] * len(self.active_tetramino):
				count += 1
		return count

	def display_active_tetramino(self):
		for i in range(len(self.active_tetramino)):
			print(' '.join([d for d in self.active_tetramino[i]]).lower())

	def rotate_clockwise(self):
		"""Rotate array by first reversing upper list (matrix),
		then unpacking it's items (rows) and in the end zipping them.
		"""
		self.active_tetramino = list(zip(*self.active_tetramino[::-1]))

	def rotate_counterclockwise(self):
		self.active_tetramino = list(reversed(list(zip(*self.active_tetramino))))

	def nudge_left(self):
		"""Draw tetramino one place to the left..."""
		if self.horizontal > 0:  # If it doesn't hit left side of matrix yet.
			self.horizontal -= 1

	def nudge_right(self):
		"""...and one place to the right."""
		if self.horizontal + Tetris.active_tetramino_length(self) <= 9:
			self.horizontal += 1

	def nudge_down(self):
		if self.vertical < 20:
			self.vertical += 1

	def hard_drop(self):
		self.vertical = 22 - Tetris.active_tetramino_height(self)
