#!/usr/bin/env python


class Tetris:

	def __init__(self, matrix='', score=0, cleared_lines=0):
		self.matrix = matrix
		self.score = score
		self.cleared_lines = cleared_lines

	def set_matrix(self):
		self.matrix = ''
		for i in range(22):
			self.matrix += f'{ input() }\n'

	def print_matrix(self):
		if self.matrix:
			print(self.matrix.rstrip())  # remove last newline character
		else:
			self.matrix += f"{'. ' * 10}\n" * 22
			print(self.matrix)

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
		# only rows - requires creating new separate type (row) and changing
		# the way in which the matrix is created.
		rows = self.matrix.split('\n')
		self.matrix = ''
		for i in range(22):
			if '.' not in rows[i]:
				rows[i] = '. ' * 10
				self.score += 100
				self.cleared_lines += 1
			self.matrix += f'{rows[i]}\n'
		return self.matrix


answer = input()

tetris = Tetris()
while answer != 'q':
	if answer == 'p':  # print matrix
		tetris.print_matrix()
	elif answer == 'g':  # set the given matrix
		tetris.set_matrix()
	elif answer == 'c':  # clear the matrix
		tetris.clear_matrix()
	elif answer == '?s':
		tetris.show_score()
	elif answer == '?n':
		tetris.show_cleared_lines()
	elif answer == 's':
		tetris.check_for_full_rows()
	answer = input()


'''matrix = ''
score = 0
cleared_lines = 0
answer = input()

while answer != 'q':
	if answer == 'p':  # print matrix
		if matrix:
			print(matrix)
		else:
			for i in range(22):
				for x in range(10):
					matrix += '. '
				matrix += '\n'
			print(matrix)
	elif answer == 'g':  # set the given matrix
		matrix = ''
		for i in range(22):
			matrix += input()
			matrix += '\n'
	elif answer == 'c':  # clear the matrix
		matrix = ''
		for i in range(22):
			for x in range(10):
				matrix += '. '
			matrix += '\n'
	elif answer == '?s':
		print(score)
	elif answer == '?n':
		print(cleared_lines)
	answer = input()'''
