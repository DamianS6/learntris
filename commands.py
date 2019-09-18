#!/usr/bin/env python

# TODO: Split Tetris class into two (Matrix and Tetramino?) as it's getting long.

# TODO: Fix moving tetramino - it should move only letters, not whole matrix
#  and automatically remove past trace. Still it needs small matrix to rotate
#  and display separately.

# TODO: Save matrix with dropped tetramino.

# TODO: Just stop dropping tetramino if next row is empty.


class Tetris:

	def __init__(self):
		self.matrix = [['.']*10 for __ in range(22)]
		self.matrix_3x3 = [['.']*3 for __ in range(3)]  # Matrix for most tetraminos.

		self.vertical, self.horizontal = 0, 0
		self.score, self.cleared_lines = 0, 0

		self.tetramino_Z, self.tetramino_I, self.tetramino_O, self.tetramino_J, \
		self.tetramino_L, self.tetramino_S, self.tetramino_T, self.active = \
			[None] * 8

	def prepare_matrix(self, option):
		if self.active:
			Tetris.move_tetramino(self)
			Tetris.print_matrix(self, option)
		elif self.matrix:
			Tetris.print_matrix(self, option)
		else:
			self.matrix = [['.']*10 for __ in range(22)]
			Tetris.print_matrix(self, option)

	def print_matrix(self, option):
		# No nested comprehension below to avoid adding newlines as list items.
		for i in range(22):
			if option == 'P':
				print(' '.join(d for d in self.matrix[i]).rstrip())
			else:
				print(' '.join(d for d in self.matrix[i]).rstrip().lower())

	def set_matrix(self):
		self.matrix = []
		for __ in range(22):
			# Split at the end to eliminate additional whitespace.
			self.matrix.append(f'{input()}'.split(' '))

	def clear_matrix(self):
		self.matrix = [['.']*10 for __ in range(22)]

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
				self.matrix[i] = ['.']*10
				self.score += 100
				self.cleared_lines += 1

	def active_tetramino_length(self):
		for row in self.active:
			count = 0
			for item in row:
				count += 1 if item != '.' else 0
			if count >= 2:
				return count

	def active_tetramino_height(self):
		count = 0
		for row in self.active:
			if row != ['.'] * len(self.active):
				count += 1

		# Deal with I which is drawn not on the top of the matrix which caused problems.
		if count == 1:
			count = 0
			for row in self.active:
				count += 1
				if row == ['c'] * 4 or row == ['C'] * 4:
					break

		return count

	def draw_I(self):
		self.tetramino_I = [['.']*4 for __ in range(4)]
		self.tetramino_I[1] = ['C']*4
		self.active = self.tetramino_I
		self.vertical, self.horizontal = 0, 3

	def draw_O(self):
		self.tetramino_O = [['Y', 'Y']] * 2
		self.active = self.tetramino_O
		self.vertical, self.horizontal = 0, 4

	def draw_Z(self):
		self.tetramino_Z = self.matrix_3x3
		self.tetramino_Z[0][:2], self.tetramino_Z[1][1:3] = ('R', 'R'), ('R', 'R')
		self.active = self.tetramino_Z
		self.vertical, self.horizontal = 0, 3

	def draw_S(self):
		self.tetramino_S = self.matrix_3x3
		self.tetramino_S[0][1:3], self.tetramino_S[1][:2] = ('G', 'G'), ('G', 'G')
		self.active = self.tetramino_S
		self.vertical, self.horizontal = 0, 3

	def draw_J(self):
		self.tetramino_J = self.matrix_3x3
		self.tetramino_J[0][0], self.tetramino_J[1][:3] = 'B', 'B'*3
		self.active = self.tetramino_J
		self.vertical, self.horizontal = 0, 3

	def draw_L(self):
		self.tetramino_L = self.matrix_3x3
		self.tetramino_L[0][2], self.tetramino_L[1][:3] = 'O', 'O'*3
		self.active = self.tetramino_L
		self.vertical, self.horizontal = 0, 3

	def draw_T(self):
		self.tetramino_T = self.matrix_3x3
		self.tetramino_T[0][1], self.tetramino_T[1][:3] = 'M', 'M'*3
		self.active = self.tetramino_T
		self.vertical, self.horizontal = 0, 3

	def move_tetramino(self):
		tetra_len = len(self.active)  # Length of tetramino's matrix.
		h, v = self.horizontal, self.vertical
		for i in range(tetra_len):
			# Replace dots with tetramino's letters.
			if self.active and h+tetra_len != 11 and i + v < 22:
				self.matrix[i+v][h: h+tetra_len] = self.active[i]
				# Delete any additional items in row if they somehow happen to exist.
				if len(self.matrix[i+v]) > 10:
					del self.matrix[i+v][-1]

	def display_active_tetramino(self):
		for i in range(len(self.active)):
			print(' '.join([d for d in self.active[i]]).lower())

	def rotate_clockwise(self):
		"""Rotate array by first reversing upper list (matrix),
		then unpacking it's items (rows), zipping them and in the end
		returning list of lists again.
		"""
		self.active = [list(a) for a in zip(*self.active[::-1])]

	def rotate_counterclockwise(self):
		self.active = list(reversed([list(a) for a in zip(*self.active[::-1])]))

	def nudge_left(self):
		"""Draw tetramino one place to the left (right, down, bottom for next functions).
		"""
		if self.horizontal > 0:  # If it doesn't hit left side of matrix yet.
			self.horizontal -= 1

	def nudge_right(self):
		if self.horizontal + Tetris.active_tetramino_length(self) <= 9:
			self.horizontal += 1

	def nudge_down(self):
		if self.vertical < 22 - Tetris.active_tetramino_height(self):
			self.vertical += 1

	def hard_drop(self):
		while self.vertical < 22 - Tetris.active_tetramino_height(self):
			Tetris.nudge_down(self)
