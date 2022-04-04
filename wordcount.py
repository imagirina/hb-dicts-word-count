"""Count words in file."""

def word_counter(file_name):
    list_of_counted_words = {}
    words = []
    contents = open(file_name)
    for line in contents:
        line = line.rstrip()
        words.extend(line.split(" "))
    
    contents.close()
    # print(contents.closed)
    for word in words:
        if word in list_of_counted_words:
            list_of_counted_words[word] += 1
        else:
            list_of_counted_words[word] = 1
    
    for key, value in list_of_counted_words.items():
        print (f"{key} {value}")
    
word_counter('test.txt')