def find_value(word, assigned):
    return sum(assigned[c] * (10 ** i) for i, c in enumerate(reversed(word)))

def _solve(word1, word2, result, letters, assigned, solutions):

    if not letters:
        if assigned[word1[0]] and assigned[word2[0]] and assigned[result[0]]:
            num1, num2, num_res = find_value(word1, assigned), find_value(word2, assigned), find_value(result, assigned)
            if num1 + num2 == num_res:
                solutions.append((f"{num1} + {num2} = {num_res}", assigned.copy()))
        return
    
    cur_letter = letters.pop()

    for num in set(range(10)) - set(assigned.values()):
        assigned[cur_letter] = num
        _solve(word1, word2, result, letters, assigned, solutions)
        assigned.pop(cur_letter)
    letters.append(cur_letter)

def solve(word1, word2, result):

    letters, solutions = sorted(set(word1 + word2 + result)), []
    
    if len(result) > max(len(word1), len(word2)) + 1 or len(letters) > 10:
        print('0 Solutions!'); return
    _solve(word1, word2, result, letters, {}, solutions)
    if solutions:
        print('\nSolutions:')
        for eq, assignment in solutions:
            print(f"{eq} with assignment {assignment}")
    else:
        print('No solutions.')

if __name__ == '__main__':
    solve(input('WORD1: ').upper(), input('WORD2: ').upper(), input('RESULT: ').upper())
