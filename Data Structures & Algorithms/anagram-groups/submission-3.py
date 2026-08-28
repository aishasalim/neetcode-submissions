class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        
        listofsigs = []
        for word in strs:
            signature = [0]*26
            for char in word:
                signature[ord(char) - ord('a')] += 1
            signature = "".join(str(signature))
            listofsigs.append(signature)
        
        count = {}
        for num in range(0, len(listofsigs)):
            if listofsigs[num] in count:
                count[listofsigs[num]].append(strs[num])
            else:
                sublist = []
                sublist.append(strs[num])
                count[listofsigs[num]] = sublist
        output = list(count.values())
        return output

        # output = []
        # pointer = 0
        # copylist=strs.copy()

        # while pointer < len(strs):
        #     if strs[pointer] in copylist:
        #         count = {}
        #         for char in strs[pointer]:
        #             count[char] = count.get(char, 0) + 1
        #         copylist.remove(strs[pointer])

        #         sublist = []
        #         sublist.append(strs[pointer])
        #         for copylistword in copylist:
        #             if len(copylistword) != len(strs[pointer]):
        #                 continue
                  
        #             secondcount = {}
        #             for char in copylistword:
        #                 secondcount[char] = secondcount.get(char, 0) + 1
        #             if count == secondcount:
        #                 sublist.append(copylistword)   

        #         copylist = [item for item in copylist if item not in sublist] 
        #         output.append(sublist)
           
        #     pointer += 1
        # return output
    

        

            
