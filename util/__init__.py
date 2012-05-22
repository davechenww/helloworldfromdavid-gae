from django.utils import html


def dump_dict(d):
    ret = ['<table>']
    ret.append('<tr><th>KEY</th><th>VALUE</th></tr>')
    for k in sorted(d.keys()):
        k = html.escape(k)
        v = d[k]
        if isinstance(v, dict) or hasattr(v, 'items'):
            v = dump_dict(v)
        else:
            v = html.escape(str(v))
        ret.append('<tr><td>%s</td><td>%s</td></tr>' % (k, v))
    ret.append('</table>')
    return ''.join(ret)

def dump_request(request):
    ret = ['<table>']
    ret.append('<tr><th>KEY</th><th>VALUE</th></tr>')
    for attr in dir(request):
        if attr.startswith('_'):
            continue
        if attr in ['postvars', 'queryvars', 'str_postvars', 'str_queryvars']:
            continue
        v = getattr(request, attr)
        if callable(v):
            continue
        attr = html.escape(attr)
        if isinstance(v, dict) or hasattr(v, 'items'):
            v = dump_dict(v)
        else:
            v = html.escape(str(v))
        ret.append('<tr><td>%s</td><td>%s</td></tr>' % (attr, v))
    ret.append('</table>')
    return ''.join(ret)
