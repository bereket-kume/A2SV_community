class Solution:
    def interpret(self, command: str) -> str:
        myl = []
        for i in range(len(command)):
            if command[i] == 'G':
                myl.append('G')
            elif command[i] == '(':
                if command[i+1] == ')':
                    myl.append('o')
                else:
                    myl.append('al')
                
           
        return "".join(myl)
