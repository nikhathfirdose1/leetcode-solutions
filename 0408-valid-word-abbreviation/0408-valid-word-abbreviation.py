class Solution:
    def validWordAbbreviation(self, word: str, abbr: str) -> bool:

        i = 0
        j = 0
        num = 0

        while i < len(word) and j < len(abbr):
            if abbr[j].isdigit():
                if abbr[j] == '0' and num == 0:
                    return False

                num = num * 10 + int(abbr[j])
                j += 1
                continue

            if num > 0:
                i += num
                num = 0


            if i >= len(word) or word[i] != abbr[j]:
                return False

            i += 1
            j += 1

        if num >0:
            i += num

        return i == len(word) and j == len(abbr)



                
                


                
        