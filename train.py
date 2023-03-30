# download shakespeare dataset at this url
# https://raw.githubusercontent.com/karpathy/char-rnn/master/data/tinyshakespeare/input.txt

with open('input.txt', 'r', encoding='utf-8') as f:
    text = f.read()

# print('length of dataset in characters: ', len(text))
# running the above code shows dataset has 1115394 characters

# this prints the first 1k characters
# print(text[0:1000])

# now lets get all the uniqe characters of the dataset
chars = sorted(list(set(text)))
vocab_size = len(chars)
print(''.join(chars))
print(vocab_size)

# character level language model means...
# we need to translate characters into integers


# Now that chars is a list of all the characters sorted into an array, 
# we are able to create a dictionary and map characters to their index
# and vice versa. 
stoi = { ch:i for i,ch in enumerate(chars) }
itos = { i:ch for i,ch in enumerate(chars) }

encode = lambda s: [stoi[c] for c in s] # encoder: take a string, output a list of integers
decode = lambda l: ''.join([itos[i] for i in l]) # decoder: take a list of integers, output a string

print(encode("hi there"))
print(decode(encode("hi there")))


