'''
A fruit seller buys a dozen of banana at Rs.X. He sells 1 banana at Rs.Y. Write a program to determine the profit or loss in Rs. for the fruitseller.
Input format:
Input consists of 2 floating point numbers
The first input corresponds to the total cost(X)
The second input corresponds to the sold cost(Y)
Output format:
Print "Profit or Loss" with Rupees.
Sample Input:
60
4
Sample Output:
Loss : Rs.12.00
'''


X = float(input())  
Y = float(input())  
totalsellingprice = 12 * Y
profitorloss = totalsellingprice - X
if profitorloss > 0:
    print(f"Profit : Rs.{profitorloss:.2f}")
else:
    print(f"Loss : Rs.{abs(profitorloss):.2f}")
