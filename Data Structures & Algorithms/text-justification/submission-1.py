class Solution:
    def fullJustify(self, words: List[str], maxWidth: int) -> List[str]:
        res, curr_line, total_char_in_line = [], [], 0
        for word in words:
            # Check if current word fits (word length + spaces needed + current line length)
            if len(word) + len(curr_line) + total_char_in_line > maxWidth:
                for i in range(maxWidth - total_char_in_line):
                    # Use modulo to cycle through gaps (leftmost get more spaces)
                    number_of_gaps = (len(curr_line) -1) or 1
                    curr_line[i % number_of_gaps] += " "
                
                # "".join and not " ".join because space are already embeded in the array so we dont need to add it
                res.append("".join(curr_line)) 
                curr_line, total_char_in_line = [], 0 # emtpy var for next line
            curr_line.append(word)
            total_char_in_line += len(word)
        
        # last edge case where all space will go at the end of the last line
        array_to_string = " ".join(curr_line)
        white_space = maxWidth - len(array_to_string) 
        res.append(array_to_string + " " * white_space)
        return res