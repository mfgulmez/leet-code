class Solution(object):
    def multiply(self, num1, num2):
        if num1 == "0" or num2 == "0":
            return "0"

        n1, n2 = len(num1), len(num2)

        res = [0] * (n1 + n2)

        for i in range(n1 - 1, -1, -1):
            for j in range(n2 - 1, -1, -1):
                p = int(num1[i]) * int(num2[j])
                pos_low = i + j + 1
                pos_high = i + j

                total = res[pos_low] + p
                res[pos_low] = total % 10         
                res[pos_high] += total // 10       

        k = 0
        while k < len(res) and res[k] == 0:
            k += 1

        return ''.join(map(str, res[k:])) if k < len(res) else "0"
