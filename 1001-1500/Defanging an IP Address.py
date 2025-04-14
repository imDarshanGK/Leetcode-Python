class Solution:
    def defangIPaddr(self, address: str) -> str:
        replace = address.replace(".", "[.]")
        return replace