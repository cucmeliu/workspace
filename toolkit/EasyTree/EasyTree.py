#!/usr/bin/python
# -*- coding: UTF-8 -*-
# Filename: EasyTree
# Desc:  GUI
# author: leo.liu
# date: 2018.3.9

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
        self.replaceButton = Button(self, text='Replace tags', command=self.replacetag)
        self.replaceButton.grid(row=0, column=2)

        self.concateButton = Button(self, text='Concate Gene', command=self.concategene)
        self.concateButton.grid(row=0) #.pack()

        self.modifyButton = Button(self, text='Modify Tree', command=self.modifytree)
        self.modifyButton.grid(row=0, column=1) #.pack()

        self.helpButton = Button(self, text='Help', command=self.help)
        self.helpButton.grid(row=1, column=2) #.pack()

        self.citationButton = Button(self, text='Citation', command=self.citation)
        self.citationButton.grid(row=1, column=3) #.pack()

        self.copyrightButton = Button(self, text='Copyright', command=self.copyright)
        self.copyrightButton.grid(row=1, column=4) #.pack()

        self.quitButton = Button(self, text='Quit', command=self.quit)
        self.quitButton.grid(row=1, column=5) #.pack()
        # self.nameInput = Entry(self)
        # self.nameInput.pack()

    def replacetag(self):
        if replacetags.do_main(None):
            tkMessageBox.showinfo('Info', '''Replace complete.
            Please find the result file in the ./data/ DIR''')

    def concategene(self):
        if geneconcate.do_main():
            tkMessageBox.showinfo('Info', '''Concate complete.
            Please find the result file in the ./data/ DIR''')

    def modifytree(self):
        # treemodify.main()
        if geneconcate.do_main():
            tkMessageBox.showinfo('Info', '''Modify complete.
            Please find the result file in the ./data/ DIR''')



    def help(self):
        #name = self.nameInput.get() or 'world'
        tkMessageBox.showinfo('Help',
        ''' --Concate Gene--
        Please put the origin files in the "data" directory in current exe dir.
        The origin files include:
        1. Datasheet.xlsx
        2. DNA/RNA text files such as ITS.txt, LSU.txt...
        The result is saved in the file in name like: ITS+LSU.txt

         --Modify Tree--
        Please put the origin files in the "data" directory in current exe dir.
        The origin files include:
        1. Dataseet.xlsx
        2. Tree.txt

        ''')

    def citation(self):
        tkMessageBox.showinfo('Citation',
        ''' --Citation--


        ''')

    def copyright(self):
        tkMessageBox.showinfo('Copyright',
        ''' --Copyright--


        ''')


def main():
    app = Application()
    app.master.title('Gene Concater')
    app.mainloop()

if __name__ =="__main__":
    main()
