from time import *

time1 = time()
print('������ ��� � 01.01.1970:', time1 / 3600 / 24 / 365.25)

sleep(5)

time2 = time()
print('������ ��� � 01.01.1970:', time2 / 3600 / 24 / 365.25)

print('��������� ��������', time2 - time1, '������')