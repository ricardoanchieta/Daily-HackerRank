if __name__ == '__main__':
    n = int(input())
    student_marks = {}
    for _ in range(n):
        name, *line = input().split()
        scores = list(map(float, line))
        student_marks[name] = scores
    query_name = input()
    
    dictAluno = student_marks[query_name]
    media = sum(dictAluno) / len(dictAluno)
    print(f'{media:.2f}')
 