#!/usr/bin/python
# -*- coding: UTF-8 -*-
# Filename: EasyTree
# Desc:  GUI
# author: leo.liu
# date: 2018.3.9

import os
from Tkinter import *
import tkMessageBox
import geneconcate
import treemodify
import replacetags

# 基因拼接
# 修改树
# Help
# Citation
# Copyright

class Application(Frame):
    def __init__(self, master=None):
        Frame.__init__(self, master)
        self.pack()
        self.createWidgets()

    def createWidgets(self):
        # self.helloLabel = Label(self, text='Gene Concater')
        # self.helloLabel.pack()
        self.replaceButton = Button(self, text='替换 Replace', command=self.replacetag)
        self.replaceButton.grid(row=0, column=2)

        self.concateButton = Button(self, text='拼接序列 Concate Gene', command=self.concategene)
        self.concateButton.grid(row=0) #.pack()

        self.modifyButton = Button(self, text='修改系统树 Modify Tree', command=self.modifytree)
        self.modifyButton.grid(row=0, column=1) #.pack()



        self.citationButton = Button(self, text='Citation', command=self.citation)
        self.citationButton.grid(row=1, column=3) #.pack()

        self.copyrightButton = Button(self, text='Copyright', command=self.copyright)
        self.copyrightButton.grid(row=1, column=4) #.pack()

        self.helpButton = Button(self, text='Help', command=self.help)
        self.helpButton.grid(row=1, column=5) #.pack()

        self.quitButton = Button(self, text='Quit', command=self.quit)
        self.quitButton.grid(row=1, column=6) #.pack()
        # self.nameInput = Entry(self)
        # self.nameInput.pack()

    def replacetag(self):
        if replacetags.do_main(None):
            tkMessageBox.showinfo('Info', '''Replace complete.
            result is saved in ./data/result/''')

    def concategene(self):
        if geneconcate.do_main():
            tkMessageBox.showinfo('Info', '''Concate complete.
            result is saved in ./data/result/''')

    def modifytree(self):
        # treemodify.main()
        if treemodify.do_main():
            tkMessageBox.showinfo('Info', '''Modify complete.
            result is saved in ./data/result/''')

    def help(self):
        #name = self.nameInput.get() or 'world'
        tkMessageBox.showinfo('Help',
        ''' --Concate Gene--
        将基因序列按data/Datasheet.xlsx中对应的顺序，拼接成完整的基因，结果存于data/序列1+序列2+....txt
        Please put the origin files in the "data" directory in current exe dir.
        The origin files include:
        1. Datasheet.xlsx
        2. DNA/RNA text files such as ITS.txt, LSU.txt...
        The result is saved in the file in name like: ITS+LSU.txt

 --Modify Tree--
        将基因系统树文件中中Unicode修改成Datasheet中Species和Strain No 的拼接串，结果存于data/result/Tree_o.txt
        Please put the origin files in the "data" directory in current exe dir.
        The origin files include:
        1. Dataseet.xlsx
        2. Tree.txt

 --Replace Tags--
        将data/A.txt的>后的编码替换为TextModify.csv的映射关系的另一值，结果存于data/result/A_out.txt

        ''')

    def citation(self):
        tkMessageBox.showinfo('Citation',
        ''' --Citation--
        Coming soon...

        ''')

    def copyright(self):
        tkMessageBox.showinfo('Copyright',
        ''' --Copyright--
        刘春明(Leo) @
            email: cucmeliu@gmail.com
            github: https://github.com/cucmeliu

        胡殿明 @


        宋海燕 @


        ''')

RST_PATH = U'./data/result/'

# pack cmd: pyinstaller -F -i ico\16X16.ico EasyTree.py  --noconsole
def main():
    app = Application()
    app.master.title('序列拼接与补齐 Gene Concater')
    if not os.path.exists(RST_PATH):
        os.mkdir(RST_PATH)
    app.mainloop()

if __name__ =="__main__":
    main()
