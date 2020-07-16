import re

def word_count(s):
    # Your code here
    
    clean_str = re.search(r'/[a-zA-Z]+/g',s)
    print(clean_str.group(0))
    
    str_array = s.lower().split(" ")
    hash = {}

    # push words to dictionary
    for word in str_array:
        if word in hash:
            hash[word] += 1
        else:
            hash[word] = 1
      
    
    return hash



if __name__ == "__main__":
    print(word_count('":;,.-+=/\\|[]{}()*^&'))
    print(word_count("Hello"))
    print(word_count('Hello, my cat. And my cat doesn\'t say "hello" back.'))
    print(word_count('This is a test of the emergency broadcast network. This is only a test.'))