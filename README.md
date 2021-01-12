# convert2pdf.pyの使い方  

convert2pdf.pyの動作を説明する.  
例として以下のディレクトリ構成図を基に説明する.

convert2pdf/  
　　┣ convert2pdf.py  
　　┣ hoge/  
　　┃　┣ 1.png  
　　┃　┣ 2.png  
　　┃　┣ 3.png  
　　┃　┣ 4.png  
　　┣ huga/  
　　　　┣ 1.png  
　　　　┣ 2.png  
　　　　┣ 3.png  
　　　　┣ 4.png  

1. convert2pdf.pyと同じディレクトリ, すなわちconvert2pdf内に存在するフォルダをすべて探索する. ここでは, \[hoge\]と\[huga\]である.  
2. 各フォルダ内ごとに*.pngファイルを見つけ次第名前順に並び替え, それらをすべて結合し, \[convert2pdf\]に\[フォルダ名\].pdfを生成する. 
3.  各フォルダを削除する. 

各フォルダを最後に削除する操作があることから, convert2pdf.pyは専用のフォルダに配置することを強く推奨する.

