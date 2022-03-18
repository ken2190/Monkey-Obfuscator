'''

MONKEY OBFUSCATOR // vesper#0003

@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@
@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@
@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@
@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@
@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@,(((((((((((((((((,%@@@@@@@@@@@@@@@@@@@@@@@@@@@@@
@@@@@@@@@@@@@@@@@@@@@@@@@@@/(((((((((((((((((((((((((/(@@@@@@@@@@@@@@@@@@@@@@@@@
@@@@@@@@@@@@@@@@@@@@@@@@/(((((((((((((((((((((((((((((((/@@@@@@@@@@@@@@@@@@@@@@@
@@@@@@@@@@@@@@@@@@@@@@/((((((((((((((((((((((((((((((((((((@@@@@@@@@@@@@@@@@@@@@
@@@@@@@@@@@@@@@@@@@@/((((((/@@@@@@@@@@@/(/@@@@@@@@@@@/((((((/@@@@@@@@@@@@@@@@@@@
@@@@@@@@@@@@@@@@@@@/(((((,@@@@@@@@@@@@@@@@@@@@@@@@@@@@@.((((((@@@@@@@@@@@@@@@@@@
@@@@@@@@@@@@@@@@@@*(((((@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@(((((/@@@@@@@@@@@@@@@@@
@@@@@@@@@@@@@@@@@@(((((*@@@@@@/((((,@@@@@@@@@/(((//@@@@@@@(((((*@@@@@@@@@@@@@@@@
@@@@@@@@@@@@@@@@@(((((*@@@@@(((((((((*@@@@#((((((((( @@@@@*((((*@@@@@@@@@@@@@@@@
@@@@@@@/((((((((((((((*@@@@.((((((((((@@@@/((((((((((@@@@@,((((((((((((((,@@@@@@
@@@@@/((((((/(((((((((/@@@@@*((((((((%@@@@@/(((((((/@@@@@@/((((((((((((((((*@@@@
@@@@/((((%@@@@@@*((((((,@@@@@@@# #&@@@@@@@@@@@#.#@@@@@@@@/((((((.@@@@@@(((((/@@@
@@@&((((@@@@@@@@@*((((((,@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@,((((((,@@@@@@@@ ((((@@@
@@@&((((#@@@@@@@@/(((((((*@@@@@@@@@@@@@@@@@@@@@@@@@@@@@*(((((((,@@@@@@@@ ((((@@@
@@@@/((((,@@@@@@/((((((&@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@&((((((,@@@@@@*((((*@@@
@@@@@*(((((((((((((((.@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@.(((((((((((((((,@@@@
@@@@@@@,((((((((((((.@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@.((((((((((((.@@@@@@
@@@@@@@@@@@@&&@@.(((@@@@@@@,(((((((((((((((((((((((((*@@@@@@@(((.@@&&@@@@@@@@@@@
@@@@@@@@@@@@@@@@.((( @@@@@@@,((((((((((((((((((((((( @@@@@@@@(((,@@@@@@@@@@@@@@@
@@@@@@@@@@@@@@@@@((((&@@@@@@@@/(((((((((((((((((((/@@@@@@@@@((((@@@@@@@@@@@@@@@@
@@@@@@@@@@@@@@@@@@((((.@@@@@@@@@@.(((((((((((((.@@@@@@@@@@.((((@@@@@@@@@@@@@@@@@
@@@@@@@@@@@@@@@@@@@,((((/@@@@@@@@@@@@@*///*@@@@@@@@@@@@@/((((,@@@@@@@@@@@@@@@@@@
@@@@@@@@@@@@@@@@@@@@@,(((((/*@@@@@@@@@@@@@@@@@@@@@@@*/(((((,@@@@@@@@@@@@@@@@@@@@
@@@@@@@@@@@@@@@@@@@@@@@@@/((((((((*,&@@@@@@@&@*/(((((((/@@@@@@@@@@@@@@@@@@@@@@@@
@@@@@@@@@@@@@@@@@@@@@@@@@@@@@#./(((((((((((((((((/.#@@@@@@@@@@@@@@@@@@@@@@@@@@@@
@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@
@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@
@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@
'''
import marshal, zlib, base64, os, lzma
from sys import argv
from tkinter import *
from tkinter import messagebox
from tkinter.filedialog import askopenfilename
from time import sleep

window = Tk()
window.title("Monkey Obfuscator || vesper#0003")
window.geometry("561x522")
window.maxsize(561, 522)
window.minsize(561, 522)
window.iconbitmap("assets/logo.ico")
window.config(background='#151414')

backg = PhotoImage(file="assets/background.png")
browss = PhotoImage(file="assets/browse.png")
obfus = PhotoImage(file="assets/obfuscate.png")
blankbu = PhotoImage(file="assets/blankbu.png")
fullbu = PhotoImage(file="assets/fullbu.png")

class Monkey:

    def __init__(self):
        self.iswallson = False
        self.main()

    def walls(self,src):
        with open(src, 'r') as f:
            mysrc = f.read()
        marsrc = compile(mysrc, 'coduter', 'exec')
        encode1 = marshal.dumps(marsrc)
        encode2 = zlib.compress(encode1)
        encode7 = lzma.compress(encode2)
        encode3 = base64.b64encode(encode7)
        encode6 = base64.b85encode(encode3)
        symbol = '__MONKEY_WALL' *150
        with open(src, 'w') as f:
            f.write('import marshal, zlib, base64, lzma\n')
            f.write(symbol+f"='{symbol}'\n")
            f.write(symbol+f"='{symbol}'")
            f.write(f"\nexec(marshal.loads(zlib.decompress(lzma.decompress(base64.b64decode(base64.b85decode({encode6}))))))\n")
            f.write(symbol+f"='{symbol}'\n")
            f.write(symbol+f"='{symbol}'")
            f.close()

    def monkeylol(self,src):
        symbol = '__MONKEY_MONKEY' * 25
        antiprocess = r"""
try:       
    from psutil import process_iter, NoSuchProcess, AccessDenied, ZombieProcess
    def MONKEND(MONKEYNAMEZ):
        for MONKEYPROC in process_iter():
            try:
                for MONK in MONKEYNAMEZ: 
                    if MONK.lower() in MONKEYPROC.name().lower():MONKEYPROC.kill()
            except (NoSuchProcess, AccessDenied, ZombieProcess):pass
    def MONKSTART():MONKEYNAMES = ['http', 'traffic', 'wireshark', 'fiddler', 'packet', 'process'];return MONKEND(MONKEYNAMEZ=MONKEYNAMES)  
    MONKSTART()
except:pass
        """
        obf_antiprocess = compile(antiprocess, 'coduter', 'exec')
        mar1 = marshal.dumps(obf_antiprocess)
        zlib1 = zlib.compress(mar1)
        lzma1 = lzma.compress(zlib1)
        b641 = base64.b64encode(lzma1)
        antiprocess_obf = f'\nexec(marshal.loads(zlib.decompress(lzma.decompress(base64.b64decode({b641})))))\n'
        with open(src, 'r') as e:
            MONKEYHAHA = e.read()
        with open(src, 'w') as f:
            f.write(symbol+f"='{symbol}'\n")
            f.write("import base64, marshal, zlib, lzma\n")
            f.write(symbol+f"='{symbol}'\n")
            f.write(antiprocess_obf)
            f.write("\n"+symbol+f"='{symbol}'\n")
            f.write("\n"+MONKEYHAHA)
            f.write("\n"+symbol+f"='{symbol}'\n")
        b64 = lambda _monkay : base64.b64encode(_monkay)
        mar = lambda _monkay : marshal.dumps(compile(_monkay,'<x>','exec'))
        zlb = lambda _monkay : zlib.compress(_monkay)
        OFFSET = 100
        symbol = '__MONKEY_MONKEY' * 50
        with open(src, 'r', encoding='utf-8', errors='ignore') as file:
            content = file.read()
        b64_content = base64.b64encode(content.encode()).decode()
        index = 0
        code = f'{symbol} = ""\n'
        for _ in range(int(len(b64_content) / OFFSET) +1):
            _str = ''
            for char in b64_content[index:index + OFFSET]:
                byte = str(hex(ord(char)))[2:]
                if len(byte) < 2:
                    byte = '0' + byte
                _str += '\\x' + str(byte)
            code += f'{symbol} += "{_str}"\n'
            index += OFFSET
        code2 =  f'exec(__import__("\\x62\\x61\\x73\\x65\\x36\\x34").b64decode({symbol}.encode("\\x75\\x74\\x66\\x2d\\x38")).decode("\\x75\\x74\\x66\\x2d\\x38"))'
        for x in range(5):
            method = repr(b64(zlb(mar(code2.encode('utf8'))))[::-1])
            data = "exec(__import__('marshal').loads(__import__('zlib').decompress(__import__('base64').b64decode(%s[::-1]))))" % method
        z = []
        for i in data:
            z.append(ord(i))
        beforemarsh ="_ = %s\nexec(''.join(chr(__) for __ in _))" % z
        marsrc = compile(beforemarsh, 'coduter', 'exec')
        obfmarsh = marshal.dumps(marsrc)
        obfzlib = zlib.compress(obfmarsh)
        obflzma = lzma.compress(obfzlib)
        obfbase64 = base64.b64encode(obflzma)
        obfbase16 = base64.b16encode(obfbase64)
        obfbase32 = base64.b32encode(obfbase16)
        obfbase85 = base64.b85encode(obfbase32)
        code += f'exec(marshal.loads(zlib.decompress(lzma.decompress(base64.b64decode(base64.b16decode(base64.b32decode(base64.b85decode({obfbase85}))))))))'
        with open(src, 'w+') as f:
            f.write("import marshal, zlib, base64, lzma\n")
            f.write(code)
            f.write(f"\n{symbol} = '{symbol}'")
    def findpy(self):
        filename = askopenfilename(filetypes=(("python files","*.py"),("All files","*.*")))
        self.filetoobf.insert(END,filename)
    def wallsonoff(self):
        if self.iswallson == False:
            self.iswallson = True
            self.enablewallz.config(image=fullbu)
        else:
            self.iswallson = False
            self.enablewallz.config(image=blankbu)
    def obfusctehehe(self):
        file = self.filetoobf.get()
        fileamount = int(self.filetoobfamnt.get())
        if self.iswallson == True:
            amount = int(self.wallsamnt.get())
        for _ in range(fileamount):
            self.monkeylol(file)
            sleep(0.5)
        if self.iswallson == True:
            for _ in range(amount):
                self.walls(file)
                sleep(0.5)
        namefile = file.split("/")[-1]
        messagebox.showinfo("Monkey Obfuscator || vesper#0003", f"Successfully Obfuscated {namefile}")
        self.__init__()

    def verify(self):
        poop = False
        file = self.filetoobf.get()
        while True:
            if os.path.exists(file) and file.endswith(".py"):
                pass
            else:
                messagebox.showerror("Monkey Obfuscator || vesper#0003", 'Invalid File')
                poop=False;break
            try:
                amount = int(self.filetoobfamnt.get())
                if amount > 5:
                    messagebox.showerror("Monkey Obfuscator || vesper#0003", 'Max Obfuscation Amount is 5')
                    poop=False;break
                else:pass
            except:
                messagebox.showerror("Monkey Obfuscator || vesper#0003", 'Invalid Amount')
                poop=False;break
            if self.iswallson == True:
                try:
                    amount2 = int(self.wallsamnt.get())
                    if amount2 > 50:
                        messagebox.showerror("Monkey Obfuscator || vesper#0003", 'Max Amount of walls is 50')
                        poop=False;break
                    else:pass
                except:
                    messagebox.showerror("Monkey Obfuscator || vesper#0003", 'Invalid Amount')
                    poop=False;break
            poop=True
            break
        if poop==True:
            self.obfusctehehe()
  
    def main(self):
        juicya_nvm_notthistime = Label(window, image=backg, borderwidth=0)
        juicya_nvm_notthistime.place(x=0,y=0)
        self.filetoobf = Entry(window,font=('SeoulHangang',10),bg='#A3A3A3', fg='#C16109',width=51,borderwidth=0)
        self.filetoobf.place(x=63, y=237)
        self.filetoobfamnt = Entry(window,font=('SeoulHangang',10),bg='#A3A3A3', fg='#C16109',width=5,borderwidth=0)
        self.filetoobfamnt.place(x=230, y=290)
        browse1 =Button(window, image=browss,bg='#1F1F1F',borderwidth=0, activebackground="#1F1F1F",command=self.findpy)
        browse1.place(x=427,y=232)
        self.enablewallz = Button(window, image=blankbu,bg='#1F1F1F',borderwidth=0, activebackground="#1F1F1F",command=self.wallsonoff)
        self.enablewallz.place(x=168,y=398)
        self.wallsamnt = Entry(window,font=('SeoulHangang',10),bg='#A3A3A3', fg='#C16109',width=5,borderwidth=0)
        self.wallsamnt.place(x=188, y=445)
        obfbu = Button(window, image=obfus,bg='#1F1F1F',borderwidth=0, activebackground="#1F1F1F",command=self.verify)
        obfbu.place(x=336,y=380)

messagebox.showinfo("Monkey Obfuscator || vesper#0003", "WARNING : Its recommended to put 1 in Amount of Obfuscation")
Monkey()
window.mainloop()
