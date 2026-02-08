class Solution:
    def fullJustify(self, words: List[str], maxWidth: int) -> List[str]:
        lines, length = [], 0
        res = []
        i = 0

        while i < len(words):
            if length + len(lines) + len(words[i]) > maxWidth:
                extra_spaces = maxWidth - length
                spaces = extra_spaces // max(1, len(lines)-1)
                remainder = extra_spaces % max(1, len(lines)-1)

                for j in range(max(1,len(lines)-1)):
                    lines[j] += ' ' * spaces
                    if remainder:
                        lines[j] += ' '
                        remainder -= 1
                
                res.append("".join(lines))
                lines, length = [], 0

            lines.append(words[i])
            length += len(words[i])
            i += 1
        
        last_line = " ".join(lines)
        last_spaces = maxWidth - len(last_line)
        res.append(last_line + ' ' * last_spaces)
        return res
