def calculate(s):
    stack = []
    num = 0
    sign = "+"
    
    i = 0
    while i < len(s):
        if s[i].isdigit():
            num = num * 10 + int(s[i])

        if (not s[i].isdigit() and s[i] != " ") or i == len(s) - 1:
            
            if sign == "+":
                stack.append(num)
            elif sign == "-":
                stack.append(-num)
            elif sign == "*":
                stack[-1] = stack[-1] * num
            elif sign == "/":
                stack[-1] = stack[-1] / num

            sign = s[i]
            num = 0
        
        i += 1

    return sum(stack)


def solve(expression):
    while "(" in expression:
        start = expression.rfind("(")
        end = expression.find(")", start)
        
        value = calculate(expression[start + 1:end])
        expression = expression[:start] + str(value) + expression[end + 1:]
    
    return calculate(expression)


expr = input()
print(solve(expr))
