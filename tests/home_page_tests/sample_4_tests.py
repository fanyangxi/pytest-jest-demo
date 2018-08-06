import pytest

class TestClass(object):

    # @pytest.fixture
    # def resource(self):
    #     print (">>> setup")
    #     yield "resource"
    #     print (">>> teardown")

    # def setup(self):
    #     print ("setup class: TestStuff")

    # def teardown(self):
    #     print ("teardown class: TestStuff")

    # def setup_class(cls):
    #     print ("setup_class class: %s" % cls.__name__)

    # def teardown_class(cls):
    #     print ("teardown_class class: %s" % cls.__name__)

    # def setup_method(self, method):
    #     print ("setup_method method: %s" % method.__name__)

    # def teardown_method(self, method):
    #     print ("teardown_method method: %s" % method.__name__)

    ### Module level setup/teardown¶
    def setup_module(module):
        """ setup any state specific to the execution of the given module."""
        print (">>> setup_module: %s" % module.__name__)

    def teardown_module(module):
        """ teardown any state that was previously setup with a setup_module
        method.
        """
        print (">>> teardown_module: %s" % module.__name__)

    ### Class level setup/teardown¶
    @classmethod
    def setup_class(cls):
        """ setup any state specific to the execution of the given class (which
        usually contains tests).
        """
        print (">>> setup_class: %s" % cls.__name__)

    @classmethod
    def teardown_class(cls):
        """ teardown any state that was previously setup with a call to
        setup_class.
        """
        print (">>> teardown_class: %s" % cls.__name__)

    ### Method and function level setup/teardown¶
    def setup_method(self, method):
        """ setup any state tied to the execution of the given function.
        Invoked for every test function in the module.
        """
        print (">>> setup_function: %s" % method.__name__)

    def teardown_method(self, method):
        """ teardown any state that was previously setup with a setup_function
        call.
        """
        print (">>> teardown_function: %s" % method.__name__)

    def test_one(self):
        x = "this"
        assert 'h' in x

    def test_two(self):
        x = "hello"
        assert hasattr(x, 'check')
