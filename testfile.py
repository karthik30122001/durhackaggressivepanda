import re

def sort_by(description, log):

    description_upper = description.upper()
    found = False
    parts = log.strip().split(" ",3)
    # print(parts)
    if len(parts)==4: 
        if parts[2]== description_upper+":":
            # print(parts[0],' ', parts[-1], "\n")
            found = True
    
    return(found)
def search_by_re(word, log):
    word_pattern = re.compile(rf'\b{re.escape(word)}\b', re.IGNORECASE)
    parts = log.strip().split(" ",3)
    if len(parts)==4: 
        if word_pattern.search(parts[3]):
            return(log)