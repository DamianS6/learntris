#!/usr/bin/env python

# TODO: Split Tetris class into two (Matrix and Tetramino?) as it's getting long.


class Tetris:

	def __init__(self):
		self.matrix = [['.']*10 for __ in range(22)]
		self.score, self.cleared_lines = 0, 0
		self.horizontal, self.vertical = 0, 0  # Tetraminos position placeholders.
		self.active = None  # Placeholder for active tetramino.

	def prepare_matrix(self, option):
		if self.active:
			Tetris.clear_matrix(self)
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
		return count

	def draw_tetramino(self, option):
		self.active = [['.']*3 for __ in range(3)]  # Basic matrix.
		self.horizontal = 3  # Basic place in row to start drawing.

		if option == 'I':
			self.active = [['.']*4 for __ in range(4)]
			self.active[1] = ['C']*4
		elif option == 'O':
			self.horizontal = 4
			self.active = [['Y', 'Y']] * 2
		elif option == 'Z':
			self.active[0][:2], self.active[1][1:3] = ('R', 'R'), ('R', 'R')
		elif option == 'S':
			self.active[0][1:3], self.active[1][:2] = ('G', 'G'), ('G', 'G')
		elif option == 'J':
			self.active[0][0], self.active[1][:3] = 'B', 'B'*3
		elif option == 'L':
			self.active[0][2], self.active[1][:3] = 'O', 'O'*3
		elif option == 'T':
			self.active[0][1], self.active[1][:3] = 'M', 'M'*3

	def move_tetramino(self):
		tetra_len = len(self.active)  # Length of tetramino's matrix.
		h, v = self.horizontal, self.vertical
		for i in range(tetra_len):
			# In every row's middle replace dots with tetramino's letters.
			if i + v < 22:
				self.matrix[i+v][h: h+tetra_len] = self.active[i]
				# Delete any additional items in row if they somehow happen to exist.
				if len(self.matrix[i+v]) > 10:
					del self.matrix[i+v][-1]

	def display_active_tetramino(self):
		for i in range(len(self.active)):
			print(' '.join([d for d in self.active[i]]).lower())

	def rotate_clockwise(self):
		"""Rotate array by first reversing upper list (matrix),
		then unpacking it's items (rows) and in the end zipping them.
		"""
		self.active = list(zip(*self.active[::-1]))

	def rotate_counterclockwise(self):
		self.active = list(reversed(list(zip(*self.active))))

	def nudge_left(self):
		"""Draw tetramino one place to the left (right, down, bottom for next functions).
		"""
		if self.horizontal > 0:  # If it doesn't hit left side of matrix yet.
			self.horizontal -= 1

	def nudge_right(self):
		if self.horizontal + Tetris.active_tetramino_length(self) <= 9:
			self.horizontal += 1

	def nudge_down(self):
		if self.vertical < 20:
			self.vertical += 1

	def hard_drop(self):
		for i in range(22 - Tetris.active_tetramino_height(self)):
			self.vertical += 1
