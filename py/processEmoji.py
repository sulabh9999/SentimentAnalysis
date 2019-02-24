### process Emoji ###
# def check(char):
#     return 0x1F600 <= char <= 0x1F64F or  0x1F300 <= char <= 0x1F5FF: # Emoticons
             # Misc Symbols and Pictographs
#             0x1F680 <= char <= 0x1F6FF, # Transport and Map
#             0x1F1E6 <= char <= 0x1F1FF, # Regional country flags
#             0x2600 <= char <= 0x26FF,   # Misc symbols
#             0x2700 <= char <= 0x27BF,   # Dingbats
#             0xFE00 <= char <= 0xFE0F,   # Variation Selectors
#             0x1F900 <= char <= 0x1F9FF,  # Supplemental Symbols and Pictographs
#             127000 <= char <= 127600, # Various asian characters
#             65024 <= char <= 65039, # Variation selector
#             9100 <= char <= 9300, # Misc items
#             8400 <= char <= 8447: # Combining Diacritical Marks for Symbols
   



def hasEmoji(word):    
    charUnicode = ord(max(word))
    if 0x1F600 <= charUnicode <= 0x1F64F or 0x1F300 <= charUnicode <= 0x1F5FF:
            return True
    return False
            
hasEmoji(' < 😂')