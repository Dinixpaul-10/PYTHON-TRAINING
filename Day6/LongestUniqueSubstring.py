class LongestWindow():
            def lengthofwindow(self,str):
                char_set=set()
                left=0
                max_len=0
                for right in range(len(str)):
                    current=str[right]
                    while current in char_set:
                        char_set.remove(str[left])
                        left+=1
                    char_set.add(current)
                    max_len=max(max_len,right-left+1)
                return max_len
#main
l=LongestWindow()
print(l.lengthofwindow("abcabcbb"))