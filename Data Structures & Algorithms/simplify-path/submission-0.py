class Solution:
    def simplifyPath(self, path: str) -> str:
        components = path.split('/')
        stack = []

        for part in components:
            if part == "..":
                if stack:
                    stack.pop()
            elif part not in ['', '.']:
                stack.append(part)
        
        return '/' + "/".join(stack)