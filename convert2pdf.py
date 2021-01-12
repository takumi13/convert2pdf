
import img2pdf
import os
import shutil
import re
import glob
from PIL import Image

# ----------------------------------------------
# 対象ディレクトリ内の.pngファイルを.jpegファイルに
# 一括変換する
# ----------------------------------------------
def __convert2JPEG(target_dir):
    files = glob.glob(target_dir + '/*.png')
    match = re.compile("(png)")

    for file_name in files:
        im = Image.open(file_name)
        im = im.convert("RGB")

        new_file_name = match.sub("jpeg", file_name)
        os.remove(file_name)
        im.save(new_file_name, quality=100)

        print(file_name + " convert is completed")

# ----------------------------------------------
# 1.jpeg ~ 9.jpeg : True
# それ以外: False
# ----------------------------------------------
def __need_prefix_of_0(filename):
    return len(filename) == 6

# ----------------------------------------------
# 対象ディレクトリにおいて, 1.jpeg ~ 9.jpegを
# 01.jpeg ~ 09.jpegにファイル名を変換する
# ----------------------------------------------
def __normalization_filename(target_dir, fnames):
    for i in range(len(fnames)):
        filename = glob.glob(target_dir + '/' + fnames[i])
        filename = filename[0]
        if __need_prefix_of_0(fnames[i]) == True:
            os.rename(filename, target_dir + '/0' + fnames[i])
            fnames[i] = '/0' + fnames[i]
    return fnames

# ----------------------------------------------
# カレントディレクトリから数えて, 各サブディレクトリを再帰的に探索し, 
# 最深部に到達したときに, そこにある.pngファイルをすべて結合して
# .pdfファイルを生成する
# ----------------------------------------------
def convert_from_deepest_subdir(dirname='./'):
    shutil.rmtree('pdf')
    os.makedirs('pdf')
    for current_dir, dir_names, fnames in os.walk(dirname):
        imgs = []
        if len(dir_names) > 0 or current_dir=='./pdf':
            continue
        else:
            __convert2JPEG(current_dir)
            fnames = __normalization_filename(current_dir, fnames)
            pdf_name = './pdf/' + current_dir[2:] + '.pdf'
            with open(pdf_name, "wb") as f:
                for fname in fnames:
                    if not fname.endswith(".jpeg"):
                        continue
                    imgs.append(current_dir + '/' + fname)
                print('-------------------------------------------')
                print('current_dir: {}'.format(current_dir))
                print('dir_name   : {}'.format(dir_names))
                print('pdf_name   : {}'.format(pdf_name))
                print('-------------------------------------------')
                sorted_imgs = sorted(imgs)
                print(sorted_imgs)
                print()
                f.write(img2pdf.convert(sorted_imgs))
                shutil.rmtree(current_dir)

def main():
    convert_from_deepest_subdir()

if __name__=='__main__':
    main()