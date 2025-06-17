from login import login
def test_login_success():
    assert login("admin","123") == "Login Success"

def test_login_failure():
    assert login("user","wrong") == "Login Failed"