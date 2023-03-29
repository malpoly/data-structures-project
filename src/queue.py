class Node:
    """Класс для узла очереди"""

    def __init__(self, data, next_node=None):
        """
        Конструктор класса Node

        :param data: данные, которые будут храниться в узле
        """
        self.data = data
        self.next_node = next_node
    

class Queue:
    """Класс для очереди"""


    def __init__(self):
        """Конструктор класса Queue"""
        self.head = None
        self.tail = None

    def enqueue(self, data):
        """
        Метод для добавления элемента в очередь

        :param data: данные, которые будут добавлены в очередь
        """
        new_node = Node(data)
        if self.tail is None:
            self.tail = self.head = new_node
        self.tail.next_node = new_node
        self.tail = new_node


    def dequeue(self):
        """
        Метод для удаления элемента из очереди. Возвращает данные удаленного элемента

        :return: данные удаленного элемента
        """
        if self.head is None:
            return None
        dequeue_node = self.head
        self.head = self.head.next_node
        if self.head is None:
            self.tail = None
            dequeue_node.next_node = None
        return dequeue_node.data

    def __str__(self):
        """Магический метод для строкового представления объекта"""
        if self.head is None:
            return ''
        node = self.head
        list_node = []
        while node:
            list_node.append(node.data)
            node = node.next_node
        return '\n'.join(list_node)
