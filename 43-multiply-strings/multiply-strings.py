class Solution(object):
    def multiply(self, num1, num2):
        if num1 == "0" or num2 == "0":
            return "0"

        n1, n2 = len(num1), len(num2)
        res = [0] * (n1 + n2)

        for i in range(n1 - 1, -1, -1):
            for j in range(n2 - 1, -1, -1):
                mul = int(num1[i]) * int(num2[j])
                s = mul + res[i + j + 1]
                res[i + j + 1] = s % 10
                res[i + j] += s // 10
                
        if res[0] == 0:
            res = res[1:]

        return ''.join(map(str, res))
