#Calculator Function to Calculate the answer

def Calculator(no1, no2, method) :
    answer = 0
    if method == "*" :
        answer = no1 * no2
    if method == "/" :
        answer = no1 / no2
    if method == "+" :
        answer = no1 + no2
    if method == "-" :
        answer = no1 - no2
    return answer

# Asking Number, Calculation Method and Sending Answer here
print("Hello, What is the First Number?")
no1 = int(input())
print("Input the Second Number")
no2 = int(input())
print("Input the Calculation Method")

method = input()
answer = Calculator(no1, no2, method)

print("The Answer is: " + str(answer))