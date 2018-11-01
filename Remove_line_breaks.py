import win32clipboard as wc
import win32con

wc.OpenClipboard()
copy_text = wc.GetClipboardData(win32con.CF_TEXT)
wc.CloseClipboard()

#print(copy_text,type(copy_text),'\n')
copy_text = copy_text.replace(b'\r\n',b' ')
#print(copy_text,type(copy_text),'\n')

wc.OpenClipboard()
wc.EmptyClipboard()
wc.SetClipboardData(win32con.CF_TEXT, copy_text)
wc.CloseClipboard()
print('done')