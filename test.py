# coding:utf8



# Part of image download
# import urllib2
#
#
# url='http://codeforces.com/predownloaded/c6/6b/c66bf8ecc5d9ef3b7001a32bf05d4a0d784f311b.png'
#
# request = urllib2.Request(url)
# response = urllib2.urlopen(request).read()
#
# with open('image.png','wb') as f:  #保存图片
#     f.write(response)
#


# import urllib2
# import urllib
# url='http://codeforces.com/problemset/problem/934/B'
# urllib.urlretrieve(url,'/home/momoto/code/crawler/scrapyproject/cf/1.html')



#
# url='http://codeforces.com/predownloaded/c6/6b'
# a=url.split('/')
# print(a[-2],a[-1])

# for i,j in enumerate(a):
#     print i,j

with open('/home/momoto/code/cfspider/955F/955F.html','a') as fp:
    fp.find('ment')