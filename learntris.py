#!/usr/bin/env python

import sys
from commands import Tetris


tetris = Tetris()


def choose_option(option):
	if option == 'q':
		sys.exit()
	elif option in ('p', 'P'):
		tetris.prepare_matrix(option)
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
	elif option == 't':
		tetris.display_active_tetramino()
	elif option == ')':
		tetris.rotate_clockwise()
	elif option == '(':
		tetris.rotate_counterclockwise()
	elif option == '<':
		tetris.nudge_left()
	elif option == '>':
		tetris.nudge_right()
	elif option == 'v':
		tetris.nudge_down()
	elif option == 'V':
		tetris.hard_drop()
	elif option.isupper():
		tetris.draw_tetramino(option)
	elif option == ';':
		print('')


def choose_option_length(answer):
	if len(answer) > 1 and answer[0] != '?':
		answer_list = list(answer)
		for i in range(len(answer_list)):
			option = answer_list[i]
			choose_option(option)
	else:
		choose_option(answer)
	choose_option_length(input())


choose_option_length(input())
