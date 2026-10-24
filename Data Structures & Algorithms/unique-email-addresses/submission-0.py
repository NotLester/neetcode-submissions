class Solution:
    def numUniqueEmails(self, emails: List[str]) -> int:
        res = set()

        for email in emails:
            email_spl = email.split('@')[0].split('+')[0].split('.')
            temp = ''.join(email_spl) + '@' + email.split('@')[1]
            res.add(temp)

        return len(res)