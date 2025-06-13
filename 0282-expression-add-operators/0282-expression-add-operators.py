class Solution(object):
    def addOperators(self, num, target):
        """
        """
        n = len(num)
        results = []
        if n == 0:
            return []
        def backtrack(index, path_expr, current_eval, prev_operand_val):
            
            if index == n:
                if current_eval == target:
                    results.append(path_expr)
                return

            for j in range(index, n):
                current_s_operand = num[index : j + 1]
                if len(current_s_operand) > 1 and current_s_operand[0] == '0':
                    break  
                current_n_operand = int(current_s_operand)

                if index == 0:
                    backtrack(j + 1, 
                              current_s_operand, 
                              current_n_operand, 
                              current_n_operand)
                else:
                    backtrack(j + 1,
                              path_expr + "+" + current_s_operand,
                              current_eval + current_n_operand,
                              current_n_operand) 
                    backtrack(j + 1,
                              path_expr + "-" + current_s_operand,
                              current_eval - current_n_operand,
                              -current_n_operand) 
                    backtrack(j + 1,
                              path_expr + "*" + current_s_operand,
                              current_eval - prev_operand_val + (prev_operand_val * current_n_operand),
                              prev_operand_val * current_n_operand)

        backtrack(0, "", 0, 0)
        return results
