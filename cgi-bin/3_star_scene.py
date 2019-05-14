#!/usr/bin/env python
# -*- coding: utf-8 -*-
# vim:fileencoding=utf-8
import cgi,sys,os,cgitb, datetime
#from myvpython import earth_sat_func

cgitb.enable()

fields = (('fstar_mass',
		  'fstar_pos',
		  'fstar_vel'),
		  ('sstar_mass',
		  'sstar_pos',
		  'sstar_vel'),
		  ('lsat_mass',
		  'lsat_ang',
		  'lsat_vel'))

def get_data():
	try:
		sats = {}
		for i in fields:
			vals = (form.getvalue(i[0]),
					  form.getvalue(i[1]),
					  form.getvalue(i[2]))
			if None in vals: raise KeyError
			sats[i[0].split('_')[0]] = {i[0]: vals[0],
										i[1]: vals[1],
										i[2]: vals[2]}
			with open('log.txt','a') as log:
				for i in sats.values():
					log.write(str(datetime.datetime.now()) + str(i) + '\n')
	except KeyError:
		htmlerror = '''
		<html>
		<title>ERROR IN DATA</title>
		<body>
		<form method=POST action="earth_sat_scene.py">
    		<table>
		    	<tr><th><b>Earth satellites</b></th></tr>
		    	<tr><th>First sat mass <td><input type="text" name='fsat_mass'></td></th></tr>
		  		<tr><th>First sat orbit radius <td><input type="text" name="fsat_orb"></td></th></tr>
		  		<tr><th>First sat velocity <td><input type="text" name="fsat_vel"></td></th></tr>
				<tr><th>Second sat mass <td><input type="text" name="ssat_mass"></td></th></tr>
		  		<tr><th>Second sat orbit radius <td><input type="text" name="ssat_orb"></td></th></tr>
		  		<tr><th>Second sat velocity <td><input type="text" name="ssat_vel"></td></th></tr>
		  		<tr><th>Launching sat mass <td><input type="text" name="lsat_mass"></td></th></tr>
		  		<tr><th>Launching sat angle <td><input type="text" name="lsat_ang"></td></th></tr>
		  		<tr><th>Launching sat velocity <td><input type="text" name="lsat_vel"></td></th></tr>
		    </table>
    		<input type="submit" value="Poehali!" name="action">
		</form>
		</body></html>
		'''
		print(htmlerror)
		return None
	else:
		return sats

def processing():
	import vpython as vp
	ball = vp.sphere()

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