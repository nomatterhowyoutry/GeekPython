from django.shortcuts import render
from app.models import askstories, showstories, newstories, jobstories
# Create your views here.


def get_table(data, tag):
    # Wrapping into <table> each table of database
    fnames = max([list(i[0].keys()) for i in data])
    string = '<tr>\n'
    for key in fnames:
        string += '<th scope="col">' + str(key) + '</th>'
    string += '\n</tr>\n'
    for item in data:
        string += '<tr>\n'
        for key in fnames:
            if key in item[0].keys():
                string += '<td>' + str(item[0][key]) + '</td>'
            else:
                string += '<td> </td>'
        string += '\n</tr>\n'
    return '''<a class="main-item" href="javascript:void(0);" >''' + tag + '''</a>
        <ul class="sub-menu">
        <li>\n<table class = "table">''' + string + '''\n</table>
        </li>  
        </ul><br>'''


def show_html(request):
    ask = askstories.objects.all().values_list('data')
    show = showstories.objects.all().values_list('data')
    new = newstories.objects.all().values_list('data')
    job = jobstories.objects.all().values_list('data')
    data = (ask, show, new, job)

    tags = ('askstories', 'showstories', 'newstories', 'jobstories')
    body = ''

    for part, tag in zip(data, tags):
        body += str(get_table(part, tag))

    return render(request, 'index.html', {'data': body})
