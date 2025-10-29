class Solution(object):
    def isValid(self, s):
        """
        :type s: str
        :rtype: bool
        """

        if len(s) % 2 == 1:
            return False

        opening = []
        closing = []
        i = 0
        while i < len(s):
            while i < len(s) and (s[i] == "(" or s[i] == "[" or s[i] == "{"):
                opening.insert(0, [s[i], i])
                i += 1
            while i < len(s) and (s[i] == ")" or s[i] == "]" or s[i] == "}"):
                closing.append([s[i], i])
                i += 1
            while len(opening) > 0 and len(closing) > 0:
                if len(opening) > 0 and len(closing) > 0 and opening[0][0] == "(":
                    if closing[0][0] != ")":
                        return False

                    else:
                        if opening[0][1] < closing[0][1]:
                            opening.pop(0)
                            closing.pop(0)

                        else:
                            return False

                if len(opening) > 0 and len(closing) > 0 and opening[0][0] == "[":
                    if closing[0][0] != "]":
                        return False

                    else:
                        if opening[0][1] < closing[0][1]:
                            opening.pop(0)
                            closing.pop(0)

                        else:
                            return False


                if len(opening) > 0 and len(closing) > 0 and opening[0][0] == "{":
                    if closing[0][0] != "}":
                        return False

                    else:
                        if opening[0][1] < closing[0][1]:
                            opening.pop(0)
                            closing.pop(0)

                        else:
                            return False
            
        print(opening, closing)
        if len(opening) == 0 and len(closing) == 0:
            return True
        else:
            return False