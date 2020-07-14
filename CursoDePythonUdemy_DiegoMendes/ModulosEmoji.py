import emoji

num = int(input('Digite um numero: '))
print('{}'.format(num))
start = int(1)
for start in range(num):
    print(emoji.emojize('olá mundo :punch:', use_aliases=True))
print('FIM')