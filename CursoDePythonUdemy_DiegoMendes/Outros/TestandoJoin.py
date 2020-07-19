from os import sep
Files = 'C:\PoketchX\GTA\GTO\+btn.png'
Files = Files.split(sep)
Files = sep.join(Files[1::2])
print(Files)