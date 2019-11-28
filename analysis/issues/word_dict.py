words_dict = [
    # -- single word doesn't provide enough context to distinguish if
    # -- issue or comment is related to code readability, a phrase is chosen
    # got from https://sarahfakhoury.com/2019-icpc-readability.pdf

    # created from the index section of:
    #   - Clean Code A Handbook of Agile Software Craftsmanship
    #   - The Art of Readable Code

    # -- we should only select negative words

    # hard|harder to read|debug|understand|spot|remember
    "readable", "readability", 
    "understand", "understandable", "understandability", "understanding", 
    "comprehension", "comprehend", "comprehending", "comprehensible",
    "confuse", "confuses", "confused", "confusing", "confusion",
    "clean up", "cleanup",
    "indentation", "indent level",
    
    "formatting", "variable name", "line length",
    "line break", "order of code", "ambiguous names", "clear name",
    "duplicate", "duplicated", "duplication",
    "unused code", "complex code", "complicated", 
    # some keywords are too general
    "order of ", 
    # some can means too many other things
    # ignore this=>"bad code", "bad piece of code",
    "bad comment", "bad comments",
    "clarify", "clarified", "clarification",
    "misleading", "is vague", "is too vague",
    "bad name", "bad naming", "bad names", 
    "not meaningful", "not descriptive",

    "typo", "long name", "short name",
    "redundant comment", "redundant code",
    "rename", "renaming", 
]
