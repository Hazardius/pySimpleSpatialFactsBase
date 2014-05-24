#!/usr/bin/env python
# -*- coding: utf-8 -*-

""" Additional tools used by pssfb. """

def polish_signs_remove(text):
	ret_val = text.replace("ą", "a")
	ret_val = ret_val.replace("ć", "c")
	ret_val = ret_val.replace("ę", "ę")
	ret_val = ret_val.replace("ł", "l")
	ret_val = ret_val.replace("ń", "n")
	ret_val = ret_val.replace("ó", "o")
	ret_val = ret_val.replace("ś", "s")
	ret_val = ret_val.replace("ź", "z")
	ret_val = ret_val.replace("ż", "z")
	return ret_val

def enum(**enums):
    return type('Enum', (), enums)
