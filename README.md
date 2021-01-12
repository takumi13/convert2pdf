# convert2pdf.pyの使い方  

convert2pdf.pyの動作を説明する.  
例として以下のディレクトリ構成図を基に説明する.  
また, 主として用いるメソッドの説明もおこなう.  

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

## メソッド  
## convert_from_deepest_subdir(dirname='./', dir_delete=False)  
### 引数の説明  
- dirname: 探索対象のディレクトリ. デフォルトではカレントディレクトリが指定される.
- dir_delete: Trueを指定すると, 探索したフォルダを最後に削除する. Falseを指定すると削除はしない. デフォルトではFalseが指定されている.

## 使い方  
1. dirnameに存在するすべてのフォルダを探索する. ここでは, \[hoge\]と\[huga\]である.  
2. 各フォルダ内ごとに*.pngファイルを見つけ次第名前順に並び替え, それらをすべて結合し, \[convert2pdf\]に\[フォルダ名\].pdfを生成する. 
3. dir_delete=Trueの場合, 探索したフォルダをすべて削除する.

各フォルダを最後に削除する操作があることから, convert2pdf.pyは専用のフォルダに配置することを強く推奨する.

