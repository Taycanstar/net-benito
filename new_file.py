beauty = "olivia"
lyst = [1,2,3,4,5]

# print(lyst[2])

# print(type(False))

# print(float(123))

# print(5/3, "regular division")
# print(5//3, "floor division")

# def power(x, y):
#     return x**y

# print(power(6, 7))

# a = False
# b = False
# print(not b and not a)

# pi = 3
# print("first pi is ", pi)
# radius = 11
# print("first radius is ", radius)
# area = pi * (radius**2)
# print("the area is ", area)
# radius = 14
# print("new radius is ", radius)

# epic_variable = 7

# def is_even(number):
    # if number % 2 == 0:
        # return f"The number {number} is even"
    # else :
        # return f"The number {number} is odd"

# test_number = 18
# print(is_even(test_number))

# b = ":"
# c = ")"
# s1 = b + 2*c

# f = "a"
# g = " b"
# h = "3"
# s2 = (f+g) * int(h)

#print(s2)

# s = "abc"
# print(len(s))


# s = "ABC d3f ghi"

# # s[3:len(s)-1]
# print(s[4:0:-1])
# print(s[6:3])


# number = 2

# while number >= 0:
#     print(number)
#     number = number - 1



# for i in range(0,5,2):
#     print(i)


# for n in range(21):
#     if n % 4 ==0:
#         print(n)


# for i in range(1,4,1):
#    print(i)

# for j in range(1, 4, 2):
#     print(j*2)

# for me in range(1,80,1):
#     print("<3" * me)


# my_sum = 0
# start = 98765
# end = 763489
# for i in range(start,end+1):
#     my_sum += i
    
# print(my_sum)

# count = 1
# while True:
#     print("count is ", count)
#     count += 1
#     if count == 1000000:
#         break


# s = "demo loops - fruit loops"
# for index in range(len(s)):
#     if s[index] == 'i' or s[index] == 'u':
#         print("THere is an i or u")

# for char in s:
#     if char == 'i' or char == 'u':
#         print("There is an i or u")

# for char in s:
#     if char in 'ui':
#         print("There is an i or u")



# number = int(input("Enter number: "))

# def factorial(number):
#     x = 1
#     for i in range(number,1,-1):
#         x = i * x
#     return x
    

# print(factorial(number)) 
    


# def prime():
#     for i in range(2,51):
#         for k in range(2,i):
#             if i % k == 0:
#                 pass
#             else:
#                 print(i)

# prime()

# import random

# #rock:1, paper: 2,

# comp_score = 0
# player_score = 0
# while player_score or comp_score < 3:
#         player = input("Choose rock, paper, or scissor: ")
#         comp_num = random.randint(1,3)
#         if comp_num == 1:
#             comp_num = "rock"
#         elif comp_num == 2:
#             com_num = "paper"
#         elif comp_num == 3:
#             comp_num = "scissor"

#         if comp_num == "rock" and player == "paper":
#             player_score = player_score + 1
#             print("You Win")
#         elif comp_num == "scissor" and player == "paper":
#             comp_score = comp_score + 1
#             print("Computer Wins")
#         elif comp_num == "scissor" and player == "rock":
#             player_score = player_score + 1
#             print("You Win")
#         elif comp_num == "paper" and player == "rock":
#             comp_score = comp_score + 1
#             print("Computer Wins")
#         elif comp_num == "rock" and player == "scissor":
#             comp_score = comp_score + 1
#             print("Computer Wins")
#         elif comp_num == "paper" and player == "scissor":
#             player_score = player_score + 1
#             print("You Win")
#         elif comp_num == player:
#             print("Tie")

# x = 0

# y = int(input("Enter Integer: "))

# while x**2 < y:
#     print("x is", x, "y is", y)
#     x = x - 1
# if x**2 == y:
#     print("Square root of ", y, " is ", x)
# else:
#     print(y, "aint no perfect square")


# guess = 0
# neg_flag = False
# x = int(input("Enter a positive integer: "))
# if x < 0:
# 	neg_flag = True
# while guess**2 < x:
# 	guess = guess + 1
# if guess**2 == x:
# 	print("Square root of", x, "is", guess)
# else:
# 	print(x, "is not a perfect square")
# 	if neg_flag:
# 		print("Just Checking… did you mean", -x,"?")
		


# x = 45
# is_found = False
# for i in range(1,10):
#     if i == x:
#         is_found = True
#         print("the secret value is", x)
#     # else:
#     #     print("not found")
# if is_found == False:
#     print("not found")



# def div_by(n, d):
#     return (d % n == 0)
    

# print(div_by(10,3))


# def sum_odd(a,b):
#     for i in range(a,b):
#         sum_of_odds +=1
#     return sum_of_odds

# def is_even(i):
#     return i % 2 == 0

# def sum_odd(a,b):
#     sum_of_odds = 0
#     i = a
#     while i <=b:
#         if not is_even(i):
#             sum_of_odds += i
#         i += 1
#     return sum_of_odds

# print(sum_odd(1,9))

# def is_palindrome(s):
#     if s == s[::-1]:
#         return True
#     else:
#         return False
    
# print(is_palindrome("bob"))


# def keep_consonants(word):
#     x = ""
#     for i in word:
#         if i not in "aeiou":
#             x +=i
#     return x

# print(keep_consonants("pluck"))

# def keep_reversed_vowels(word):
#     x = ""
#     for i in word[::-1]:
#         if i in "aeiou":
#             x += i
#     return x

# print(keep_reversed_vowels("epic"))


# def add(x,y):
# 	return x+y
# def mult(x,y):
# 	print(x*y)

# add(1,2)
# print(add(2,3))
# mult(3,4)
# print(mult(4,5))


# def bisection_root(x):
# 	alpha = 0.01
# 	low = 0
# 	high = x
# 	ans = (high + low) /2.0
# 	while abs(ans**2 - x) >= alpha:
# 		if ans**2 < x:
# 			low = ans
# 		else:
# 			high = ans
# 		ans = (high + low) / 2.0
# 	return ans
	

# def count_nums_with_sqrt_close_to(n, alpha):
# 	count = 0
# 	for i in range(n**3):
# 		sqrt = bisection_root(i)
# 		if abs(n-sqrt) < alpha:
# 			print(i,sqrt)
# 			count = count+1
# 	return count
		
# print(count_nums_with_sqrt_close_to(10,.1))

# def calc(op, x, y):
# 	return op(x,y)

# def div(a,b):
# 	if b != 0:
# 		return a/b

# res = calc (div, 2, 0)

# print(res)



# def apply(criteria,n): 
#     for i in range(0,n+1):
#         if criteria(i):
#             return i

# print(apply(is_even,23))

# def is_even(x):
#     return x % 2 == 0

# def is_divisible_by_3(x):
#     return x % 3 == 0

# def is_in_range(x):
#     if x in range(1,101):
#         return True
#     else:
#         return False


# import random
# def guessing_game():
#     rand_int = random.randint(1,101)
#     for i in range(7):
#         x = int(input("Guess the Number: "))
#         if x != rand_int:
#             if is_even(x) and x < rand_int:
#                     print("Guess again bitch but here a hint: the number even and greater than", x)
#             elif is_even(x) and rand_int < x:
#                     print("Guess again bitch but here a hint: the number even and less than ", x)
#             elif not is_even(x) and rand_int > x:
#                     print("Guess again bitch but here a hint: the number odd and greater than", x)
#             elif not is_even(x) and rand_int < x:
#                 print("Guess again bitch but here a hint: the number odd and less than ", x)
#         elif x == rand_int:
#              print("good job dipshit it's", rand_int)

# guessing_game()

# def do_twice(n, fn):
#     return fn(fn(n))
# print(do_twice(3, lambda x: x**2))

# def apply(criteria,n):
#     return criteria

# print(apply(lambda y :y% 2 == 1, 3)) 



# def char_counts(s):
#     v = 0
#     c = 0
#     for i in s:
#         if i in "aeiou":
#             v += 1
#         else:
#             c += 1
#     return (v,c)

# print(char_counts("dummy"))


# def mean(*args):
# 	tot = 0
# 	for a in args:
# 		tot += a
# 	return tot/len(args)


# def make_ordered_list(n):
    
#     lyst = []
#     for i in range(0,n+1):
#         lyst.append(i)
#     return lyst


# # print(make_ordered_list(5))

# count = 0
# variable = 3
# for i in range(variable):
#     for k in range(variable):
#         if count % 2 != 0:
#             print("o", end=" ")
#         else:
#             print("x", end= " ")
#         count+=1

    

# def remove_elem(L, e):
#     new_list = []
#     for i in L:
#         if i != e:
#             new_list.append(i)
#     print("old list:", L)
#     string = "new list " + str(new_list)
#     return string
# lyst = [1,2,3,4,5]        
# print(remove_elem(lyst,3))


# s = "The quick brown fox jumps over the lazy dog"
# new_var = s.split("e")
# print(len(new_var))

# L = ['a','b','c']
# A = ''.join(L)
# B = '_'.join(L)
# #error
# # C = ''.join([1,2,3])
# ''.join(['1','2','3'])


# d = ["the","quick","hawk","jumped","over","the","skibidi","tuah"]
# r = '<3 <3'.join(d)
# print(r)


# def count_words(sen):
#     s = sen.split()
#     return len(s)

# print(count_words("what the sigma"))




# L = [4,2,7]
# L.sort()
# L.reverse()
# L_new = sorted(L)


# def sort_words(sen):
#     lyst = sen.split(' ')
#     lyst.sort()
#     return sen

# print(sort_words("look at this photograph"))

# def word_counter(sen):
#     char = 0
#     for i in sen:
#         if i != " ":
#             char += 1
#     return f"{len(sen.split())} words, {char} characters"
# print(word_counter(input("GIMME SENTENCE: ")))


# print(f"{b[0]}|{b[1]}|{b[2]}\n-+-+-\n{b[3]}|{b[4]}|{b[5]}\n-+-+-\n{b[6]}|{b[7]}|{b[8]}")


def display_board(b):
    print("{}|{}|{}\n-+-+-\n{}|{}|{}\n-+-+-\n{}|{}|{}".format(b[0],b[1],b[2],b[3],b[4],b[5],b[6],b[7],b[8]))

lyst = ["0","1","2","3","4","5","6","7", "8"]

display_board(lyst)

# def check_winner(board,player):
#     w



# def game():
    

player = int(input("X Enter: "))
print("YOU WIN!!!!! HOORAY!!!!")