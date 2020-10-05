from django.template import Library
from django.utils.safestring import mark_safe
import datetime ,time
register = Library()

@register.simple_tag
def navListTag():

    temlateData = [
        {
            'child': [],
            'title': '标题1',
            'url': '#',
        },
        {
            'child': [
                {
                    'title': '标题2-1',
                    'url': '#',
                },
                {
                    'title': '标题2-2',
                    'url': '#',
                },
                {
                    'title': '标题2-3',
                    'url': '#',
                },
                {
                    'title': '标题2-4',
                    'url': '#',
                },
                {
                    'title': '标题2-4',
                    'url': '#',
                },

            ],
            'title': '标题2'
        },
        {
            'child': [
                {
                    'title': '标题3-1',
                    'url': '#',
                },
                {
                    'title': '标题3-2',
                    'url': '#',
                },
            ],
            'title': '标题3'
        },
    ]


    template = ''''''
    template += '<ul class="side-list">'
    for item in temlateData:
        if len(item['child']) > 0:
            # 存在下级
        
            template+='<li class="side-item"><div class="side-menu-title">%s</div><ul class="side-list">' % item['title']
            for i in item['child']:
                template += '''<li class="side-item haschild">
                            <a href="%s" class='side-menu-title'>%s</a> 
                        </li>''' % (i['url'],i['title'])
            template +='</ul></li>'
        else:
            # 不存在下级
            template +='''<li class="side-item">
                            <a href="%s" class='side-menu-title'>%s</a> 
                        </li>''' % (item['url'],item['title'])

    template +='</ul>'


    # print()
    '''return mark_safe(
    <ul class="side-list">
        <li class="side-item">
            <div class='side-menu-title'>标题1</div>
            <ul class='side-list'>
                <li class="side-item">
                    <a >1</a>
                </li>
                <li class="side-item">
                    <a>2</a>
                </li>
                <li class="side-item">
                    <a>3</a>
                </li>
                <li class="side-item">
                    <a>4</a>
                </li>
                <li class="side-item">
                    <a>5</a>
                </li>
                <li class="side-item">
                    <a>6</a>
                </li>
            </ul>

        </li>
        <li>
            <a class='side-menu-title'>没有下级标题的标题</a>
        </li>
        <li>
            <div class='side-menu-title'>标题2</div>
            <ul class='side-list'>
                <li class="side-item">
                    <a>1</a>
                </li>
                <li class="side-item">
                    <a>2</a>
                </li>
                <li class="side-item">
                    <a>3</a>
                </li>
                <li class="side-item">
                    <a>4</a>
                </li>
                <li class="side-item">
                    <a>5</a>
                </li>
                <li class="side-item">
                    <a>6</a>
                </li>

            </ul>
        </li>
        <li>
            <a class='side-menu-title'>没有下级标题的标题</a>
        </li>
    </ul>
    '''

    return mark_safe(template)
    




