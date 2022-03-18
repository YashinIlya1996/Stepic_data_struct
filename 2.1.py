d = {')': '(', ']': '[', '}': '{'}
stack_staples = []
stack_ind = []
s = input()
answer = 'Success'
flag = True
for i in range(len(s)):
    if s[i] in '([{':
        stack_staples.append(s[i])
        stack_ind.append(i)
    elif s[i] in ')]}':
        if not stack_staples:
            answer = i + 1
            flag = False
            break
        else:
            cur_staple = stack_staples.pop()
            cur_ind = stack_ind.pop()
            if d[s[i]] != cur_staple:
                answer = i + 1
                flag = False
                break
if stack_staples and flag:
    answer = stack_ind.pop() + 1
print(answer)

