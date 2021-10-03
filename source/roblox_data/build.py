import html2text
from bs4 import BeautifulSoup
from pathlib import PurePath, Path
import re

host = 'http://119.29.63.170:8030'

def html2md(path):
    p = PurePath(path)
    name = p.stem
    print(name)

    with open(path, 'r') as f:
        content = f.read()

    bs = BeautifulSoup(content, 'html.parser')
    html_main = bs.find_all(name='main')
    html_main = html_main[0]
    html_title = html_main.find(name='div', attrs={'class': 'd-none'})
    html_title = html_main.find(name='h1')
    html_title = html_title.text

    html_time = html_main.find(name='span')
    if html_time:
        html_time = html_time.text
    else:
        html_time = ''

    html_md = html_main.find(name='div', attrs={'class': 'article-details'})
    html_md = ''.join([str(content) for content in html_md.contents])
    ht = html2text.HTML2Text(baseurl='https://developer.roblox.com')
    ht.body_width = 0
    md = ht.handle(html_md)
    md = md.replace('代码示例 预期输出 [ 展开 __ ](javascript:void\\(0\\))\n', '```')
    md = md.replace('__ 复制代码 [ 亮色模式 __ __ ](javascript:void\\(0\\))\n', '```')
    md = md.replace('预期输出 [ 展开 __ ](javascript:void\\(0\\))\n', '```')
    md = md.replace('(/assets/', '(https://developer.roblox.com/assets/')
    md = md.replace('.png)', '.png)\n\n')
    # md = re.sub('`/articles/(.+)\|(.+)`', r'[\2](http://119.29.63.170:8030/articles/\1)', md)

    # fixme: .png这样不该换行的换行了 done
    # fixme: 添加roblox权利声明 done
    # fixme: 搜索是否能用 done
    # fixme: articles/game assets|Roblox 中的游戏资源
    # fixme Table.html截断 done
    # fixme: API

    roblox_right = '***\n__Roblox官方链接__:[{}](https://developer.roblox.com/zh-cn/articles/{})'.format(html_title, name)

    result = '# {} \nTime:<em>{}</em>\n\n{}\n\n\n{}'.format(html_title, html_time, md, roblox_right)

    path = '../articles/%s.md' % name
    with open(path, 'w') as f:
        f.writelines(result)


def main():
    p = Path('./articles/')
    for f in p.glob('*'):
        html2md(f)

if __name__ == '__main__':
    path = './articles/Table.html'
    # html2md(path)
    # print(md)
    main()
