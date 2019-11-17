#coding:gbk
"""
第一个小项目：Rock-paper-scissors-lizard-Spock
作者：张峻
日期：2019年11月17日
"""

import random

# 0 - 石头
# 1 - 史波克
# 2 - 纸
# 3 - 蜥蜴
# 4 - 剪刀

def name_to_number(name):
    """
    将游戏对象对应到不同的整数
    """
    if name=="石头":
        return 0
    elif name=="史波克":
        return 1
    elif name=="纸":
        return 2
    elif name=="蜥蜴":
        return 3
    elif name=="剪刀":
        return 4
    else:
        print("Error: No Correct Name")
        
def number_to_name(number):
    """
    将整数 (0, 1, 2, 3, or 4)对应到游戏的不同对象
    """
    if number==0:
        return "石头"
    elif number==1:
        return "史波克"
    elif number==2:
        return "纸"
    elif number==3:
        return "蜥蜴"
    elif number==4:
        return "剪刀"

def rpsls(choice_name):
	"""
	用户玩家任意给出一个选择，根据RPSLS游戏规则，在屏幕上输出对应的结果
	"""
	print("----------------")
	print("您的选择为：", choice_name)
	player_choice = choice_name#存入变量player_choice

	player_choice_number = name_to_number(player_choice)# 调用name_to_number()函数将用户的游戏选择对象转换为相应的整数，存入变量player_choice_number

	comp_number = random.randrange(0, 5)# 利用random.randrange()自动产生0-4之间的随机整数，作为计算机随机选择的游戏对象，存入变量comp_number

	comp_choice = number_to_name(comp_number)# 调用number_to_name()函数将计算机产生的随机数转换为对应的游戏对象

	print("计算机的选择为：", comp_choice)
	
	x= player_choice_number - comp_number
	if x ==1:# 利用if/elif/else 语句
		print("您赢了")
	elif x==2:
		print("您赢了")
	elif x==-3:
		print("您赢了")
	elif x==-4:
		print("您赢了")
	elif x==0:
		print("您和机器出的一样呢")
	elif x==-1 or x==-2 or x==3 or x==4:
		print("机器赢了")


print("欢迎使用RPSLS游戏")
print("----------------")
choice_name = input("请输入您的选择：")
rpsls(choice_name)
