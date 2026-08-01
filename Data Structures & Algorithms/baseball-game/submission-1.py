class Solution:
    def calPoints(self, operations: List[str]) -> int:
        record = []
        sum = 0

        for operation in operations:
            if operation == '+':
                newScore = record[-2] + record[-1]
                record.append(newScore)
                sum += newScore
            elif operation == 'D':
                newScore = 2 * record[-1]
                record.append(newScore)
                sum += newScore
            elif operation == 'C':
                removed = record.pop()
                sum -= removed
            else:
                newScore = int(operation)
                record.append(newScore)
                sum += newScore
        
        return sum
        
