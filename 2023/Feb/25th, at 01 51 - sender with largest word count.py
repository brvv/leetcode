class Solution:
    def largestWordCount(self, messages: List[str], senders: List[str]) -> str:
        wc = {}

        max_count = -1
        max_user = None

        for message, user in zip(messages, senders):
            if user not in wc:
                wc[user] = message.count(' ') + 1
            else:
                wc[user] += message.count(' ') + 1
        
            if wc[user] > max_count or not max_user:
                max_count = wc[user]
                max_user = user
            
            elif wc[user] == max_count:
                max_user = (sorted([user, max_user]))[-1]

        return max_user