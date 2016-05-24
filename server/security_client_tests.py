from livia.security.client import SecurityClient

#TODO fazer os testes corretamente

if __name__ == '__main__':
	userlogin = SecurityClient().login("abraao.isvi@gmail.com",'123456')
	print(userlogin)
	tokenvalidation = SecurityClient().check_token(userlogin['code'],userlogin['token'])
	print(tokenvalidation)