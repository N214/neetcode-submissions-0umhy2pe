class Solution:
    def fullJustify(self, words: list[str], maxWidth: int) -> list[str]:
        res, line, line_len = [], [], 0
        
        for word in words:
            # Check if current word fits (word length + spaces needed + current line length)
            if line_len + len(word) + len(line) > maxWidth:
                # Distribute extra spaces
                for i in range(maxWidth - line_len):
                    # Use modulo to cycle through gaps (leftmost get more spaces)
                    line[i % (len(line) - 1 or 1)] += ' '
                res.append("".join(line))
                line, line_len = [], 0
            
            line.append(word)
            line_len += len(word)
            
        # Handle the last line (left-justified)
        last_line = " ".join(line)
        res.append(last_line.ljust(maxWidth))
        
        return res
