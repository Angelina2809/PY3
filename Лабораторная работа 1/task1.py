"""
My little Queue
"""
from typing import Any
class Queue:
    def __init__(self):
        """
        Очередь с помощью python list
        TODO Описать где начало и конец очереди
        начало очереди находится в начале нашего списка, а конец в конце списка
        """
        self.queue = []
        ...  # TODO инициализировать список

    def enqueue(self, elem: Any) -> None: #O (n)
        """
        Добавление элемент в конец очереди
        :param elem: Элемент, который должен быть добавлен
        """
        self.queue.append(elem)
        ...  # TODO реализовать метод enqueue

    def dequeue(self) -> Any:# O(1)
        """
        Извлечение элемента из начала очереди.
        :raise: IndexError - Ошибка, если очередь пуста
        :return: Извлеченный с начала очереди элемент.
        """
        return self.queue.pop(0)

        ...  # TODO реализовать метод dequeue

    def peek(self, ind: int = 0) -> Any: # O(n)
        """
        Просмотр произвольного элемента, находящегося в очереди, без его извлечения.
        :param ind: индекс элемента (отсчет с начала, 0 - первый с начала элемент в очереди, 1 - второй с начала элемент в очереди, и т.д.)
        :raise: TypeError - если указан не целочисленный тип индекса
        :raise: IndexError - если индекс вне границ очереди
        :return: Значение просмотренного элемента
        """
        return self.queue[ind]
        ...  # TODO реализовать метод peek

    def clear(self) -> None: # O(n)
        """ Очистка очереди. """
        self.queue.clear()
    def __len__(self):
        """ Количество элементов в очереди. """
        return len(self.queue)
        ...  # TODO реализовать метод __len__

