# -*- coding: utf-8 -*-
import pytest

@pytest.fixture(scope='session')
def seed_local_fixture():
    """
    This is a sample local fixture that will return ‘hello world’ variables. 
    """
    my_message_1 = 'Hello World'
    my_message_2 = 'Here is a sample of a local pytest fixture'
    my_message_3 = 'It returns 3 values'
    return(my_message_1, my_message_2, my_message_3)
