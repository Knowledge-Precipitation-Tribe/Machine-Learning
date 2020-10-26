# -*- coding: utf-8 -*-#
'''
# Name:         test
# Description:  
# Author:       super
# Date:         2020/8/14
'''

class LNode:
    def __init__(self, x):
        self.val = x
        self.next = None


if __name__ == '__main__':
    head = LNode(1)
    head.next = None
    for i in range(5):
        temp = LNode(i)
        temp.next = head.next
        head.next = temp

    h = head.next
    while h != None:
        print(h.val)
        h = h.next