import random
num = random.randint(1, 100)
print('����� ���������� � �������� ��������!\n������� ����� �� 1 �� 100:\n')

def is_valid(n):
    return n.isdigit() and 1 <= int(n) <= 100

def input_num():
    while True:
        guess = input()
        if is_valid(guess):
            return int(guess)
        else:
            print('� ����� ���� ���-���� ������ ����� ����� �� 1 �� 100?')

def compare_num():
    while True:
        n = input_num()
        if n < num:
            print('���� ����� ������ �����������, ���������� ��� �����')
        elif n > num:
            print('���� ����� ������ �����������, ���������� ��� �����')
        else:
            print('�� �������, �����������!')
            break

compare_num()


