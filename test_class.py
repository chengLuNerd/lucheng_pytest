# content of test_class.py

class TestClass(object):
    def test_one(self):
        x = "This"
        assert 'h' in x


    def test_two(self):
        x = "hello"
        assert hasattr(x, 'check')
