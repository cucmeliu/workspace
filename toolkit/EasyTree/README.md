# EasyTree

本程序实现基因序列的替换、拼接和系统树的修改。

待处理数据放在程序目录下的 data 目录中，文件格式见功能描述中；

处理后的数据存于 data/result/目录中；

## 功能：序列替换 Gene Replacement

将data/A.txt的>后的编码替换为TextModify.csv的映射关系的另一值，结果存于data/result/A_out.txt

## 功能：序列拼接 Gene Concate

将基因序列按data/Datasheet.xlsx中对应的顺序，拼接成完整的基因，结果存于data/序列1+序列2+....txt

The genconcate program helps to concate the <strong>Gene<strong> serial for the Strains.

All DNA/RNA pairs are saved in the Datasheet.xlsx, in type of:

Unicode Species	Strain No	Type	DNA1	DNA2  DNA3.....,

and the full DNA/RNA information is saved in the text files with the name of the DNA/RNA name.

the program concate the strain followed by the full DNA/RNA information, and output with the file named by all DNA/RNA.


## 功能：系统树修改 tree treemodify

 将基因系统树文件中中Unicode修改成Datasheet中Species和Strain No 的拼接串，结果存于data/result/Tree_o.txt

 The treemodify program helps to modify the gene tree file
