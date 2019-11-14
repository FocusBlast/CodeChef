parah = input().split()
parah1 = input().split()
revparah = ' '.join(reversed(parah))
revparah1 = ' '.join(reversed(parah1))
punctuations = '''!()-[]{};:'"\,<>./?@#$%^&*_~'''
no_punc = ""
for char in revparah:
    for char1 in revparah1:
        if char not in punctuations:
            no_punc = no_punc + char
    if char1 not in punctuations:
        no_punc  = no_punc + char +char1
print(no_punc)