class Solution(object):
    def totalNQueens(self, n):
        """
        :type n: int
        :rtype: int
        """
        self.count = 0
        full_mask = (1 << n) - 1 

        def backtrack(cols, pos_diag, neg_diag):
            if cols == full_mask:
                self.count += 1
                return

            free = full_mask & ~(cols | pos_diag | neg_diag)

            while free:
                bit = free & -free
                free -= bit
                backtrack(
                    cols | bit,
                    (pos_diag | bit) << 1,
                    (neg_diag | bit) >> 1
                )

        backtrack(0, 0, 0)
        return self.count