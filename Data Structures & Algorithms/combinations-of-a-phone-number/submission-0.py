class Solution:
    def letterCombinations(self, digits: str) -> List[str]:
        number_to_letter = {
            "2" : ("a", "b", "c"),
            "3" : ("d", "e", "f"),
            "4" : ("g", "h", "i"),
            "5" : ("j", "k", "l"),
            "6" : ("m", "n", "o"),
            "7" : ("p", "q", "r", "s"),
            "8" : ("t", "u", "v"),
            "9" : ("w", "x", "y", "z")
        }

        if digits == "":
            return []

        from itertools import product
        lists = list(list(number_to_letter[char] for char in digits))
        result = ["".join(p) for p in product(*lists)]

        return result