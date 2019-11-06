text = open ('NYT-bestsellers.txt').readlines()
titles = []
authors = []
publishers = []
dates = []
genres = []

for line in text:
    i = 0
    values = line.split('\t')
    text[i] =values
    i += 1


