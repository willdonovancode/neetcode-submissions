class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        words={}
        for word in strs:
            if ''.join(sorted(word)) not in words.keys():
                words[''.join(sorted(word))]=[word]
            elif ''.join(sorted(word)) in words:
                words[''.join(sorted(word))].append(word)
        
        res=[]

        for keys,values in words.items():
            res.append(values)
        
        return res
                
