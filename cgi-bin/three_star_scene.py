#!/usr/bin/env python
# -*- coding: utf-8 -*-
# vim:fileencoding=utf-8
'''Модуль для обработки ввёденных данных для трёх звезд и вызова соответствующей анимации'''
import cgi,sys,os,cgitb, datetime

cgitb.enable()

fields = (('fstar_mass',
		  'fstar_pos',
		  'fstar_vel'),
		  ('sstar_mass',
		  'sstar_pos',
		  'sstar_vel'),
		  ('tstar_mass',
		  'tstar_pos',
		  'tstar_vel'))

def get_data():
	'''Функция для сбора данных с полей формы с выдачи словаря со значениями для дальнейшей работы.
	При недостаточном количестве данных возвращается форма ввода данных снова'''
	try:
		stars = {}
		for i in fields:
			vals = (form.getvalue(i[0]),
					  form.getvalue(i[1]),
					  form.getvalue(i[2]))
			if None in vals: raise KeyError
			stars[i[0].split('_')[0]] = {i[0]: vals[0],
										i[1]: vals[1],
										i[2]: vals[2]}
	except KeyError:
		htmlerror = '''
		<html>
		<title>ERROR IN DATA</title>
		<body>
		<form method=POST action="three_star_scene.py">
		    <table>
		    	<tr><th><b>Three interesting stars</b></th></tr>
		    	<tr><th>First star mass <td><input type="text" name="fstar_mass"></td></th></tr>
		  		<tr><th>First star position <td><input type="text" name="fstar_pos"></td></th></tr>
		  		<tr><th>First star velocity <td><input type="text" name="fstar_vel"></td></th></tr>
		  		<tr><th>Second star mass <td><input type="text" name="sstar_mass"></td></th></tr>
		  		<tr><th>Second star position <td><input type="text" name="sstar_pos"></td></th></tr>
		  		<tr><th>Second star velocity <td><input type="text" name="sstar_vel"></td></th></tr>
		  		<tr><th>Third star mass <td><input type="text" name="tstar_mass"></td></th></tr>
		  		<tr><th>Third star position <td><input type="text" name="tstar_pos"></td></th></tr>
		  		<tr><th>Third star velocity <td><input type="text" name="tstar_vel"></td></th></tr>
		    </table>
		    <input type="submit" value="Poehali!" name="action">
		</form>
		</body></html>
		'''
		print(htmlerror)
		return None
	else:
		return stars

def processing(stars):
	


def htmlize(adict):
	new = adict.copy()
	for field in fieldnames:
		value = new[field]
		new[field] = cgi.escape(repr(value))
	return new

def main():
	global form
	a = None
	form = cgi.FieldStorage()
	action = form['action'].value if 'action' in form else None
	if action == 'Poehali!':
		a = get_data()
		if a  != None:
			processing()
	#print(replyhtml % htmlize(fields))

if __name__ == '__main__':
	main()