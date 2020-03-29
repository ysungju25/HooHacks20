# todo create main_list[]
# todo create interrupt_list[] todo create functions
#  for user: join/leave main list, join/leave sublist
# todo implement timer

import thread
import time

class Node:
    def __init__(self, name=None):
        self.name = name
        self.next = None


class LinkedList:
    def __init__(self):
        self.head = Node()  # NOT the current speaker - POINTS to current speaker

    def add_user(self, username):
        incoming_user = Node(username)
        current_user = self.head
        while current_user.next:
            if current_user.name == incoming_user.name:
                print("Cannot add ", username, " - name already on list")
                return
            current_user = current_user.next
        current_user.next = incoming_user

    def kick_user(self, outgoing_user):
        current_user = self.head
        while current_user.next:
            last_user = current_user
            current_user = current_user.next
            if current_user.name == outgoing_user:
                print("Kicking", current_user.name)
                last_user.next = current_user.next
                return
        print("Cannot kick", outgoing_user, "- name not found in list")

    def length(self):
        current_user = self.head
        no_of_users = 0
        while current_user.next:
            no_of_users += 1
            current_user = current_user.next
        return no_of_users

    def get_index(self, search_index):
        if search_index >= self.length():
            print("Invalid index!")
            return None
        current_index = 0
        current_user = self.head
        while True:
            current_user = current_user.next
            if current_index == search_index:
                return ('user', search_index, ':', current_user.name)
            current_index += 1

    def print(self):
        list_of_names = []
        current_user = self.head
        while current_user.next:  # aka, current_user != None
            current_user = current_user.next
            list_of_names.append(current_user.name)
        for i in range(len(list_of_names)):
            print(i + 1, list_of_names[i])

    # todo pop_user - take user off top of list and reset timer
    # def pop_user(self, username):

main_list = LinkedList()

main_list.add_user('Jeff')
main_list.add_user('SJ')
main_list.add_user('Scanna')
main_list.print()
main_list.add_user('SJ')
main_list.kick_user('Scanna')
main_list.print()
main_list.kick_user('Scanna')
main_list.add_user('XXXTentacion')
main_list.print()
