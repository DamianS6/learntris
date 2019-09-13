class Tetris:

	def __init__(self):
		self.matrix = None
		self.score = 0
		self.cleared_lines = 0
		self.matrix_4x4 = [['.', '.', '.', '.'] for __ in range(4)]
		self.matrix_3x3 = [['.', '.', '.'] for __ in range(3)]

	def print_matrix(self):
		if self.matrix:
			print(' '.join(i for r in self.matrix for i in r).rstrip())
		else:
			self.matrix = [['.', '.', '.', '.', '.', '.', '.', '.', '.', '.', '\n']
			               for __ in range(22)]
			print(' '.join(i for r in self.matrix for i in r).rstrip())

	def print_matrix_with_tetramino(self):
		tetra_len = len(self.active_tetramino)
		replace = int((10 - tetra_len)/2)
		for i in range(tetra_len):
			self.matrix[i][replace:replace+tetra_len] = self.active_tetramino[i]
		Tetris.print_matrix(self)

	def set_matrix(self):
		self.matrix = []
		for __ in range(22):
			self.matrix.append(f'{input()}\n'.split(' '))

	def clear_matrix(self):
		self.matrix = self.matrix = [['.', '.', '.', '.', '.', '.', '.', '.', '.', '.', '\n']
			               for __ in range(22)]

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

	def display_active_tetramino(self):
		if self.active_tetramino is None:
			pass
		else:
			for i in range(len(self.active_tetramino)):
				print(' '.join([d for d in self.active_tetramino[i]]).lower())

	def rotate_clockwise(self):
		self.active_tetramino = list(zip(*self.active_tetramino[::-1]))
