﻿# coding:utf-8
 
import sys
import locale

#reload(sys)
#sys.setdefaultencoding('gbk')
 
def p(f):
    print '%s.%s(): %s' % (f.__module__, f.__name__, f())
 
sss=u'汗'
print sss
# 返回当前系统所使用的默认字符编码
p(sys.getdefaultencoding)
 
# 返回用于转换Unicode文件名至系统文件名所使用的编码
p(sys.getfilesystemencoding)
 
# 获取默认的区域设置并返回元祖(语言, 编码)
p(locale.getdefaultlocale)
 
# 返回用户设定的文本数据编码
# 文档提到this function only returns a guess
p(locale.getpreferredencoding)
 
# \xba\xba是'汉'的GBK编码
# mbcs是不推荐使用的编码，这里仅作测试表明为什么不应该用
print r"'\xba\xba'.decode('mbcs'):", repr('\xba\xba'.decode('mbcs'))
 
#在笔者的Windows上的结果(区域设置为中文(简体, 中国))
#sys.getdefaultencoding(): gbk
#sys.getfilesystemencoding(): mbcs
#locale.getdefaultlocale(): ('zh_CN', 'cp936')
#locale.getpreferredencoding(): cp936
#'\xba\xba'.decode('mbcs'): u'\u6c49'

#这两天遇到一个问题，刚搞明白！
#s=u'汗'
#在命令行下工作正常
#在声明为utf8格式的py脚本文件中异常，但是gbk/gb2312的文件中又是正常的。
#
#这个问题，应该是我用gvim编辑的文件保存的格式是跟着win8走的cp936，而python会根据编码声明去decode，它拿着utf8格式解cp936的文件就报错了~
#对吧？