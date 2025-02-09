def solve(set1, set2, set3):
    line1 = set((set1.split()))
    line2 = set((set2.split()))
    line3 = set((set3.split()))

    result_set = line2.intersection(line3) - line1
    result_list = list(result_set)
    total = sum(int(n) for n in result_list)
    return "; ".join(result_list), total


def output_result():
    s1 = input()
    s2 = input()
    s3 = input()
    result, total = solve(s1, s2, s3)
    print(result)
    print(total)


output_result()
