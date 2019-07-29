import os

os.chdir('/Users/allan/PycharmProjects/CursoDePythonUdemy')
print(os.getcwd())

listFiles = os.listdir('/Users/allan/PycharmProjects/CursoDePythonUdemy')
listFiles = os.listdir('.')
print(listFiles)
os.chdir('/Users/allan')
print(os.getcwd())
listFiles = os.listdir('.')
print('2 => {}'.format(listFiles))

try:
    os.chdir('/Users/allan/PycharmProjects/CursoDePythonUdemy/OS')
    os.mkdir('teste')

except(FileExistsError):
    os.rmdir('teste')
    os.mkdir('teste')
listFiles = os.listdir('/Users/allan/PycharmProjects/CursoDePythonUdemy/OS')
print(os.getcwd())

print(os.stat('OS.py'))
print(os.stat('OS.py'))
