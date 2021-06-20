import autorization
userName = input()
userPassword = input()
result = autorization.send_register(userName, userPassword, 44)
result = autorization.send_login(userName, userPassword)
##################################################################
if result[:4] == 'id: ':
	userID = int(0)
	keyJoin = str()
	LastKeyJoin = str()
	getting = result.split(' | ')
	for elem in getting:
		item = elem.split(': ')
		if item[0] == 'id':
			userID = int(item[1])
		elif item[0] == 'keyJoin':
			keyJoin = item[1]
		elif item[0] == 'LastKeyJoin':
			LastKeyJoin = item[1]
	print('%d %s %s' % (userID, keyJoin, LastKeyJoin))

elif result == 'ConnectError':
	print("host failed")	
elif result == 'UserError':
	print("user failed")	
elif result == 'AutorizationError':
	print("failed autorization")	
elif result == 'RegisterError':
	print("failed register")	
elif result == 'RegisterSucces':
	print("good register") 
else:
	print("Other Error!")