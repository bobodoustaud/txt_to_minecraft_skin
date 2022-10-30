import imp
from math import ceil
from pickletools import optimize
from PIL import Image
from pathlib import Path
class compiler:
    def __init__(self,str,x,y):
        chunks=[]
        n=8
        chunks = [str[i:i+n] for i in range(0, len(str), n)]
        for i in range(len(chunks)):
            if len(chunks[i])<n:
                chunks[i]+='0'*(n-len(chunks[i]))
        self.img=Image.new('RGBA', (x,y))
        for i in range(len(chunks)):
            foo=i%x
            bar=i//x
            self.img.putpixel((foo,bar),(int(chunks[i][0:2],base=16),int(chunks[i][2:4],base=16),int(chunks[i][4:6],base=16),int(chunks[i][6:8],base=16)))
class decompiler:
    def __init__(self, img, x, y, xx, yy):
        sus = img.crop((x, y, xx, yy))
        bar=[]
        for i in range(sus.size[1]*sus.size[0]):
            ax=i%sus.size[0]
            ay=i//sus.size[0]
            bar.append(hex(sus.getpixel((ax,ay))[0])[2:].rjust(2,'0')+hex(sus.getpixel((ax,ay))[1])[2:].rjust(2,'0')+hex(sus.getpixel((ax,ay))[2])[2:].rjust(2,'0')+hex(sus.getpixel((ax,ay))[3])[2:].rjust(2,'0'))
        lacking=''
        for i in range(len(bar)):
            lacking+=bar[i]
        self.str=lacking
class prog:
    def __init__(self, pic, str, cells):
        str = Path(str).read_text()
        str=str.encode().hex()
        # if len(str)<5376:
        #     str+='0'*(5376-len(str))
        pic=Image.open(pic)
        cells=cells.split(',')
        for i in range(len(cells)):
            if cells[i]=='1':
                pic.paste(compiler(str[:512],8,8).img,(0,0))
                str=str[512:]
            if cells[i]=='2':
                pic.paste(compiler(str[:1024],16,8,).img,(24,0))
                str=str[1024:]
            if cells[i]=='3':
                pic.paste(compiler(str[:512],8,8).img,(56,0))
                str=str[512:]
            if cells[i]=='4':
                pic.paste(compiler(str[:128],4,4).img,(0,16))
                str=str[128:]
            if cells[i]=='5':
                pic.paste(compiler(str[:256],8,4).img,(12,16))
                str=str[256:]
            if cells[i]=='6':
                pic.paste(compiler(str[:256],8,4).img,(36,16))
                str=str[256:]
            if cells[i]=='7':
                pic.paste(compiler(str[:128],4,4).img,(52,16))
                str=str[128:]
            if cells[i]=='8':
                pic.paste(compiler(str[:128],4,4).img,(0,32))
                str=str[128:]
            if cells[i]=='9':
                pic.paste(compiler(str[:256],8,4).img,(12,32))
                str=str[256:]
            if cells[i]=='10':
                pic.paste(compiler(str[:256],8,4).img,(36,32))
                str=str[256:]
            if cells[i]=='11':
                pic.paste(compiler(str[:128],4,4).img,(52,32))
                str=str[128:]
            if cells[i]=='12':
                pic.paste(compiler(str[:2048],8,32).img,(56,16))
                str=str[2048:]
            if cells[i]=='13':
                pic.paste(compiler(str[:128],4,4).img,(0,48))
                str=str[128:]
            if cells[i]=='14':
                pic.paste(compiler(str[:256],8,4).img,(12,48))
                str=str[256:]
            if cells[i]=='15':
                pic.paste(compiler(str[:256],8,4).img,(28,48))
                str=str[256:]
            if cells[i]=='16':
                pic.paste(compiler(str[:256],8,4).img,(44,48))
                str=str[256:]
            if cells[i]=='17':
                pic.paste(compiler(str[:128],4,4).img,(60,48))
                str=str[128:]
        pic.save('!!!!!!!!!!!!!!!_encrypted_skin.png', optimize=True)
class prog2:
    def __init__(self, img, cells):
        cells=cells.split(',')
        self.str=''
        img=Image.open(img)
        for i in range(len(cells)):
            if cells[i]=='1':
                self.str+=(decompiler(img, 0, 0, 8, 8).str)
            if cells[i]=='2':
                self.str+=(decompiler(img, 24, 0, 40, 8).str)
            if cells[i]=='3':
                self.str+=(decompiler(img, 56, 0, 64, 8).str)
            if cells[i]=='4':
                self.str+=(decompiler(img, 0, 16, 4, 20).str)
            if cells[i]=='5':
                self.str+=(decompiler(img, 12, 16, 20, 20).str)
            if cells[i]=='6':
                self.str+=(decompiler(img, 36, 16, 44, 20).str)
            if cells[i]=='7':
                self.str+=(decompiler(img, 52, 16, 56, 20).str)
            if cells[i]=='8':
                self.str+=(decompiler(img, 0, 32, 4, 36).str)
            if cells[i]=='9':
                self.str+=(decompiler(img, 12, 32, 20, 36).str)
            if cells[i]=='10':
                self.str+=(decompiler(img, 36, 32, 44, 36).str)
            if cells[i]=='11':
                self.str+=(decompiler(img, 52, 32, 56, 36).str)
            if cells[i]=='12':
                self.str+=(decompiler(img, 56, 16, 64, 48).str)
            if cells[i]=='13':
                self.str+=(decompiler(img, 0, 48, 4, 52).str)
            if cells[i]=='14':
                self.str+=(decompiler(img, 12, 48, 20, 52).str)
            if cells[i]=='15':
                self.str+=(decompiler(img, 28, 48, 36, 52).str)
            if cells[i]=='16':
                self.str+=(decompiler(img, 44, 48, 52, 52).str)
            if cells[i]=='17':
                self.str+=(decompiler(img, 60, 48, 64, 52).str)
        f=open('output.txt', 'w')
        self.str=str(bytes.fromhex(self.str).decode())
        f.write(self.str)
        f.close()
a=True
while a:
    if input('Enter mode e/d\n') == 'e':
        print('Reminder :\ncell 1,3 = 512 values aka 256 characters\ncell 2 = 1024 values aka 512 characters\ncell 4,7,8,11,13,17 = 128 values aka 64 characters\ncell 5,6,9,10,14,15,16 = 256 values aka 128 characters\ncell 12 = 2048 values aka 1024 characters\nfor a grand total of 6656 values aka 3328 characters.')
        prog(input('Enter the name of the skin (must be in the same folder) ex: skin.png\n'), input('Enter the file name of the text ex: example.txt\n'), input('Enter which cells have to be filled (order matters) ex: 1,7,8,9,4\n'))
        print('saved under \'!!!!!!!!!!!!!!!_encrypted_skin.png\'\n\n')
    else:
        print('\n'+prog2(input('Enter the name of the skin (must be in the same folder) ex: skin.png\n'), input('Which tiles should be read (order matters) ex: 1,7,8,9,4\n')).str+'\n')
    if input('Quit? y/n\n')=='y':
        a=False