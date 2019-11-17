#coding:gbk
"""
��һ��С��Ŀ��Rock-paper-scissors-lizard-Spock
���ߣ��ž�
���ڣ�2019��11��17��
"""

import random

# 0 - ʯͷ
# 1 - ʷ����
# 2 - ֽ
# 3 - ����
# 4 - ����

def name_to_number(name):
    """
    ����Ϸ�����Ӧ����ͬ������
    """
    if name=="ʯͷ":
        return 0
    elif name=="ʷ����":
        return 1
    elif name=="ֽ":
        return 2
    elif name=="����":
        return 3
    elif name=="����":
        return 4
    else:
        print("Error: No Correct Name")
        
def number_to_name(number):
    """
    ������ (0, 1, 2, 3, or 4)��Ӧ����Ϸ�Ĳ�ͬ����
    """
    if number==0:
        return "ʯͷ"
    elif number==1:
        return "ʷ����"
    elif number==2:
        return "ֽ"
    elif number==3:
        return "����"
    elif number==4:
        return "����"

def rpsls(choice_name):
	"""
	�û�����������һ��ѡ�񣬸���RPSLS��Ϸ��������Ļ�������Ӧ�Ľ��
	"""
	print("----------------")
	print("����ѡ��Ϊ��", choice_name)
	player_choice = choice_name#�������player_choice

	player_choice_number = name_to_number(player_choice)# ����name_to_number()�������û�����Ϸѡ�����ת��Ϊ��Ӧ���������������player_choice_number

	comp_number = random.randrange(0, 5)# ����random.randrange()�Զ�����0-4֮��������������Ϊ��������ѡ�����Ϸ���󣬴������comp_number

	comp_choice = number_to_name(comp_number)# ����number_to_name()����������������������ת��Ϊ��Ӧ����Ϸ����

	print("�������ѡ��Ϊ��", comp_choice)
	
	x= player_choice_number - comp_number
	if x ==1:# ����if/elif/else ���
		print("��Ӯ��")
	elif x==2:
		print("��Ӯ��")
	elif x==-3:
		print("��Ӯ��")
	elif x==-4:
		print("��Ӯ��")
	elif x==0:
		print("���ͻ�������һ����")
	elif x==-1 or x==-2 or x==3 or x==4:
		print("����Ӯ��")


print("��ӭʹ��RPSLS��Ϸ")
print("----------------")
choice_name = input("����������ѡ��")
rpsls(choice_name)
