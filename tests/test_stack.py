import pytest
from src.stack import Node, Stack

#@pytest.fixture
#def item1():
    #return Item("Смартфон", 10000, 20)
def test_node_init():
    n1 = Node(6, None)
    assert n1.data == 6
    assert n1.next_node == None


def test_stack_init():
    stack = Stack()
    assert stack

def test_stack_push():
    stack = Stack()
    stack.push('data1')
    assert stack.top.data == 'data1'

def test_stack_pop():
    stack = Stack()
    stack.push('data1')
    stack.push('data2')
    stack.pop()
    assert stack.top.data == 'data1'
