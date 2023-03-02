class Solution:
    def isValidDigit(self, token):
        if len(token) == 0 or (token[0] == '0' and len(token) > 1):
            return False
        digit = int(token)
        if (0 <= digit <= 255):
            return True
        return False

    def isValidIpV6Token(self, token):
        length = 1 <= len(token) <= 4
        return length

    def isIPv4(self, string):
        digits = '0123456789'
        token = ''
        address=[]

        for letter in string:
            if letter in digits:
                token += letter
            elif letter is '.':
                if self.isValidDigit(token):
                    digit = int(token)
                    address.append(digit)
                    token = ''
                else:
                    return False
            else:
                return False
        
        if self.isValidDigit(token) and len(address) == 3:
            digit = int(token)
            address.append(digit)
        else:
            return False
        
        return True
        
    def isIPv6(self, string):
        digits = '0123456789abcdefABCDEF'
        token = ''
        address=[]

        for letter in string:
            if letter in digits:
                token += letter
            elif letter is ':':
                if self.isValidIpV6Token(token):
                    address.append(token)
                    token = ''
                else:
                    return False
            else:
                return False
        
        if self.isValidIpV6Token(token) and len(address) == 7:
            address.append(token)
        else:
            return False
        
        return True


    def validIPAddress(self, queryIP: str) -> str:
        if self.isIPv4(queryIP):
            return 'IPv4'
        elif self.isIPv6(queryIP):
            return 'IPv6'
        else:
            return 'Neither'