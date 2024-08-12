# -*- coding: gbk -*-
# Author: style_forever
# Date: 12
# Description: 




# �� Python �У��б�list�������������У�queue�����������б���ص㣬ֱ��ʹ���б���ʵ�ֶ��в��������ŵ�ѡ��

# ������һ���Ƚ��ȳ���FIFO, First-In-First-Out�������ݽṹ����ζ��������ӵ�Ԫ�����ȱ��Ƴ���

# ʹ���б�ʱ�����Ƶ�������б�Ŀ�ͷ�����ɾ��Ԫ�أ����ܻ��ܵ�Ӱ�죬��Ϊ��Щ������ʱ�临�Ӷ��� O(n)��Ϊ�˽��������⣬Python �ṩ�� collections.deque������˫�˶��У����������˸�Ч����Ӻ�ɾ��Ԫ�ء�


from collections import deque

# ����һ���ն���
queue = deque()

# ���β���Ԫ��
queue.append('a')
queue.append('b')
queue.append('c')

print("����״̬:", queue)  # ���: ����״̬: deque(['a', 'b', 'c'])

# �Ӷ����Ƴ�Ԫ��
first_element = queue.popleft()
print("�Ƴ���Ԫ��:", first_element)  # ���: �Ƴ���Ԫ��: a
print("����״̬:", queue)            # ���: ����״̬: deque(['b', 'c'])

# �鿴����Ԫ�أ����Ƴ���
front_element = queue[0]
print("����Ԫ��:", front_element)    # ���: ����Ԫ��: b

# �������Ƿ�Ϊ��
is_empty = len(queue) == 0
print("�����Ƿ�Ϊ��:", is_empty)     # ���: �����Ƿ�Ϊ��: False

# ��ȡ���д�С
size = len(queue)
print("���д�С:", size)            # ���: ���д�С: 2


# ��Ȼ����ʹ���б���ʵ�ֶ��У���ʹ�� collections.deque �����Ч�ͼ�ࡣ���ṩ�� O(1) ʱ�临�Ӷȵ���Ӻ�ɾ���������ǳ��ʺ϶����������ݽṹ��

class Queue:
    def __init__(self):
        self.queue = []

    def enqueue(self, item):
        self.queue.append(item)

    def dequeue(self):
        if not self.is_empty():
            return self.queue.pop(0)
        else:
            raise IndexError("dequeue from empty queue")

    def peek(self):
        if not self.is_empty():
            return self.queue[0]
        else:
            raise IndexError("peek from empty queue")

    def is_empty(self):
        return len(self.queue) == 0

    def size(self):
        return len(self.queue)

# ʹ��ʾ��
queue = Queue()
queue.enqueue('a')
queue.enqueue('b')
queue.enqueue('c')

print("����Ԫ��:", queue.peek())    # ���: ����Ԫ��: a
print("���д�С:", queue.size())    # ���: ���д�С: 3

print("�Ƴ���Ԫ��:", queue.dequeue())  # ���: �Ƴ���Ԫ��: a
print("�����Ƿ�Ϊ��:", queue.is_empty())  # ���: �����Ƿ�Ϊ��: False
print("���д�С:", queue.size())    # ���: ���д�С: 2