# coding:gb2312
 
import sys
import locale

#reload(sys)
#sys.setdefaultencoding('gbk')
 
def p(f):
    print '%s.%s(): %s' % (f.__module__, f.__name__, f())
 
sss=u'��'
print sss
# ���ص�ǰϵͳ��ʹ�õ�Ĭ���ַ�����
p(sys.getdefaultencoding)
 
# ��������ת��Unicode�ļ�����ϵͳ�ļ�����ʹ�õı���
p(sys.getfilesystemencoding)
 
# ��ȡĬ�ϵ��������ò�����Ԫ��(����, ����)
p(locale.getdefaultlocale)
 
# �����û��趨���ı����ݱ���
# �ĵ��ᵽthis function only returns a guess
p(locale.getpreferredencoding)
 
# \xba\xba��'��'��GBK����
# mbcs�ǲ��Ƽ�ʹ�õı��룬����������Ա���Ϊʲô��Ӧ����
print r"'\xba\xba'.decode('mbcs'):", repr('\xba\xba'.decode('mbcs'))
 
#�ڱ��ߵ�Windows�ϵĽ��(��������Ϊ����(����, �й�))
#sys.getdefaultencoding(): gbk
#sys.getfilesystemencoding(): mbcs
#locale.getdefaultlocale(): ('zh_CN', 'cp936')
#locale.getpreferredencoding(): cp936
#'\xba\xba'.decode('mbcs'): u'\u6c49'

