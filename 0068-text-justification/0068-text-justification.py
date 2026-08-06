class Solution:
    def fullJustify(self, words: List[str], maxWidth: int) -> List[str]:
        line, length = [], 0
        res = []
        i = 0

        while i < len(words):
            if length + len(line) + len(words[i]) > maxWidth:
                extra_spaces = maxWidth - length
                spaces = extra_spaces // max(1, len(line)-1)
                remainder = extra_spaces % max(1, len(line)-1)

                for j in range(max(1, len(line)-1)):
                    line[j] += ' ' * spaces
                    if remainder:
                        line[j] += ' '
                        remainder -= 1

                res.append("".join(line))
                line, length = [], 0

            line.append(words[i])
            length += len(words[i])
            i += 1
        
        last_word = " ".join(line)
        spaces = maxWidth - len(last_word)
        res.append(last_word + ' ' * spaces)
        return res
