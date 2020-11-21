class Anagram:
    def __init__(self):
        self.requests = {}

    @staticmethod
    def checkIfAnagram(word1, word2):
        """
        check if two words are anagram
        TC: O(n), n is max character of the two words

        Args:
            word1 (str): The first parameter.
            word2 (str): The second parameter.

        Returns:
            bool: True if words are anagram, False otherwise.
        """

        if word1 is None or word2 is None:
            return False

        lettersCount = {}
        letters1 = list(word1.lower())
        letters2 = list(word2.lower())

        # count each letter from first word "word1" by +1 in lettersCount
        for i in letters1:
            count = 1
            if i in lettersCount:
                count = lettersCount[i] + 1
            lettersCount[i] = count

        # count each letter from second word "word1" by -1 in lettersCount
        for i in letters2:
            count = -1
            if i in lettersCount:
                count = lettersCount[i] - 1
            lettersCount[i] = count

        # total count of each letter in the lettersCount should be 0
        # if two words are anagram
        for key, value in lettersCount.items():
            if value != 0:
                return False

        return True

    def insertRequest(self, word1, word2):
        """
        insert words request into the requests dict
        TC: O(1)

        Args:
            word1 (str): The first parameter.
            word2 (str): The second parameter.
        """
        if word1 + " " + word2 in self.requests:
            self.requests[word1 + " " + word2] += 1
        elif word2 + " " + word1 in self.requests:
            self.requests[word2 + " " + word1] += 1
        else:
            self.requests[word1 + " " + word2] = 1

    def getTopTenRequests(self):
        """
        get the top 10 most popular requests from requests dist
        TC: O(nlogn), n is number of request in the requests dist

        Returns:
            collection: list of tuple(request), each tuple contain request word "request"
            and number of the requests "times".
        """
        # sort the requests dict
        sortedRequests = sorted(self.requests.items(), key=lambda item: item[1], reverse=True)

        # return the top ten of the requests
        topTen = []
        for k, v in sortedRequests[0:min(10, len(sortedRequests))]:
            tuple = {
                "request": k,
                "times": v
            }
            topTen.append(tuple)
        return topTen
