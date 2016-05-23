import pytest
from livia.services.securityservice import SecurityService


@pytest.fixture(scope="session", autouse=True)
def initialize():
	global security_service
	security_service = SecurityService()
	security_service.connect()

def test_login():
	global token
	global code
	checked, code, token = security_service.login("abraao.isvi@gmail.com", "123456")
	print(code,token)
	assert (checked), "Checked is False"
	assert token is not None,"Token was not generated"
	assert code is not None,"Account was not found"

def test_check_token():
	checked = security_service.check_token(code, token)
	assert checked, "Checked is False token:"+str(token)+" code:"+str(code)

#initialize()
#test_login()
#test_check_token()

if __name__ == '__main__':
	initialize()
	test_login()
	test_check_token()