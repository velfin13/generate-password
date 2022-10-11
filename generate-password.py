import random
pass1 = ['a','b','c','d','f','g','h','i','j','k',
		'l','m','n','ñ','o','p','q','r','s','t',
		'v','w','x','y','z','A','B','C','D','E','F',
		'G','H','I','J','K','L','M','N','Ñ','O','P',
		'Q','R','S','T','V','W','X','Y','Z','1','2',
		'3','4','5','6','7','8','9','0','~','!','@',
		'#','$','%','^','&','*','-','_','+','=','.',
		'{','}','[',']','(',')','?','<','>',';',':']

password = ""

for x in range(23):
	password = password + random.choices(pass1)[0]

print('Your password is: \n', password)
