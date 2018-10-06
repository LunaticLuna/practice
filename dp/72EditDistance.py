'''Given two words word1 and word2, find the minimum number of operations required to convert word1 to word2.

You have the following 3 operations permitted on a word:

Insert a character
Delete a character
Replace a character'''
def minDistance(self, word1, word2):
    """
    :type word1: str
    :type word2: str
    :rtype: int
    """
    if word1 == "": return len(word2)
    if word2 == "": return len(word1)
    dp = [[None] * (len(word2)+1) for i in range(len(word1)+1)] 
    
    for i in xrange(len(word1), -1,-1):
        for j in xrange(len(word2),-1,-1):
            # print i,j
            if i == len(word1) and j == len(word2):
                dp[i][j] =  0
                continue
            elif i == len(word1):
                dp[i][j] = len(word2) - j
                continue
            elif j == len(word2):
                dp[i][j] = len(word1)- i
                continue
            else:
                dp[i][j] =  min(dp[i+1][j+1],dp[i][j+1]+1,dp[i+1][j]+1) if word1[i] == word2[j] else 1 +min(dp[i+1][j+1],dp[i][j+1],dp[i+1][j])
                
    # for i in range(len(dp)):
    #     print dp[i]
    return dp[0][0]