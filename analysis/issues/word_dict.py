words_dict = [
    # -- single word doesn't provide enough context to distinguish if
    # -- issue or comment is related to code readability, a phrase is chosen
    # got from https://sarahfakhoury.com/2019-icpc-readability.pdf

    # created from the index section of:
    #   - Clean Code A Handbook of Agile Software Craftsmanship
    #   - The Art of Readable Code

    # -- we should only select negative words

    "hard to read", "hard to debug", "hard to understand", "hard to spot", "hard to remember",
    "harder to read", "harder to debug", "harder to understand", "harder to spot", "harder to remember",
    "not readable", "readability", 
    "not understandable", "understandability", 
    "comprehension", "comprehend", "not comprehensible",
    "confuse", "confusing", "confusion",
    "clean up", "cleanup",
    "indentation", "indent level",
    
    "formatting", "variable name", "line length",
    "line break", "order of code", "ambiguous names", "clear name",
    "duplicate", "duplication",
    "unused code", "complex code", "complicated", 
    # some keywords are too general
    "order of line", 
    # some can means too many other things
    # ignore this=>"bad code", "bad piece of code",
    "bad comment",
    "clarify", "clarified", "clarification",
    "misleading", "is vague", "is too vague",
    "bad name", "bad naming", "bad names", 
    "not meaningful", "not descriptive",

    "typo", "long name", "short name",
    "redundant comment", "redundant code",
    "rename", "renaming", 
]
