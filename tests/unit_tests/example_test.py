import sys    

def test_always_passes():
    print("test")
    assert True
    
def test_python_version():
    assert sys.version_info.minor >= 6
