# -*- coding: gbk -*-
# Author: style_forever
# Date: 11
# Description: 



# �������Ƶ�ʽʾ����

# 1. �б��Ƶ�ʽ
# ����һ������1��10��ƽ�����б�
squares = [x**2 for x in range(1, 11)]
print(squares)

# 2. �ֵ��Ƶ�ʽ
# ����һ������1��10��ż�����������ֵ�
even_odd = {x: 'even' if x % 2 == 0 else 'odd' for x in range(1, 11)}
print(even_odd)

# 3. �����Ƶ�ʽ
# ����һ������1��10��ż���ļ���
evens = {x for x in range(1, 11) if x % 2 == 0}
print(evens)

# 4. �����Ƶ�ʽ
# ����һ������1��10��ż�����б�
evens = [x for x in range(1, 11) if x % 2 == 0] 
print(evens)

numbers = range(1, 11)
evens = list(filter(lambda x: x % 2 == 0, numbers))
print(evens)  # [2, 4]

# 5. Ƕ���Ƶ�ʽ
# ����һ������1��10��ƽ�����б�ÿ��Ԫ���Ǹ�Ԫ�ص�ƽ��������ƽ����
squares_and_roots = [(x**2, x**0.5) for x in range(1, 11)]
print(squares_and_roots)