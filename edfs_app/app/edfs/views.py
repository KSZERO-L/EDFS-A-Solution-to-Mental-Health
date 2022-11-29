from django.shortcuts import render
from django.http import JsonResponse
from django.http import HttpResponse
from django.template.loader import render_to_string
from edfs.firebase_cmd import ls, cat, mkdir, rm, readPartition, getPartitionLocations
from edfs.sql_cmd import sql_ls, sql_cat, sql_mkdir, sql_rm, sql_readPartition, sql_getPartition
from edfs.firebase_search import show
from edfs.firebase_analytics import analytics
from edfs.sql_search_analytics import sql_main
import json
from numpyencoder import NumpyEncoder

# Create your views here.
def index(request):
    return render(request, 'index.html')

# Endpoint 1 for form
def form_ajax(request):
    if request.method == 'POST':
        command_input = request.POST.get('command_input', None)
        type1 = request.POST.get('type', None)
        if command_input:
            response = {
                 'command_input': command_input,
                 'type': type1
            }
            return JsonResponse(response)


def firebase(cmd, loc):
    final_output = []
    # ls
    if cmd == "ls":
        output = ls.main(loc)
        print(output)
        for val in output:
            print(val)
            if '.' not in val:
                final_output.append({'location': val, 'type': 'Folder'})
            else:
                final_output.append({'location': val, 'type': 'File'})

        context = {
            'data': final_output,
        }
        table_name = 'gt_table.html'

    elif cmd == "cat":
        output = cat.main(loc)
        print(output)
        final_output = []
        cols = list(output.columns)
        fd_cols = {}
        for i, c in enumerate(cols):
            fd_cols['col'+str(i)] = c
        print(cols)
        for i in output.iterrows():
            final_output.append({
                'col0': i[1][cols[0]],
                'col1': i[1][cols[1]],
                'col2': i[1][cols[2]],
                'col3': i[1][cols[3]],
                'col4': i[1][cols[4]]
            })

        print(final_output)
        context = {
            'data': final_output,
            'cols': fd_cols
        }
        table_name = 'cat_table.html'

    elif cmd == "mkdir":

        output = mkdir.main(loc)
        print(output)
        for val in output:
            print(val)
            if '.' not in val:
                final_output.append({'location': val, 'type': 'Folder'})
            else:
                final_output.append({'location': val, 'type': 'File'})

        context = {
            'data': final_output,
        }
        table_name = 'gt_table.html'

    elif cmd == "rm":

        output = rm.main(loc)
        print(output)
        for val in output:
            print(val)
            if '.' not in val:
                final_output.append({'location': val, 'type': 'Folder'})
            else:
                final_output.append({'location': val, 'type': 'File'})

        context = {
            'data': final_output,
        }
        table_name = 'gt_table.html'

    elif cmd == "readPartition":
        loc_split = loc.split()
        loc = ' '.join(loc_split[:-1])
        num = int(loc_split[-1])
        print(loc, num)
        output = readPartition.main(loc, num)
        print(output)
        final_output = []
        cols = list(output.columns)
        fd_cols = {}
        for i, c in enumerate(cols):
            fd_cols['col'+str(i)] = c
        print(cols)
        for i in output.iterrows():
            final_output.append({
                'col0': i[1][cols[0]],
                'col1': i[1][cols[1]],
                'col2': i[1][cols[2]],
                'col3': i[1][cols[3]],
                'col4': i[1][cols[4]]
            })

        print(final_output)
        context = {
            'data': final_output,
            'cols': fd_cols
        }
        table_name = 'cat_table.html'

    elif cmd == "getPartitionLocations":

        file, output = getPartitionLocations.main(loc)
        print(output)
        for val in output:
            print(val)
            final_output.append({'file': file, 'location': val})

        context = {
            'data': final_output,
        }
        table_name = 'getPartition_table.html'

    return table_name, context

def sql(cmd, loc):

    if cmd == "ls":
        output = sql_ls.ls(loc)
        print(output)
        for val in output:
            print(val)
            if '.' not in val:
                final_output.append({'location': val, 'type': 'Folder'})
            else:
                final_output.append({'location': val, 'type': 'File'})

        context = {
            'data': final_output,
        }
        table_name = 'gt_table.html'

    elif cmd == "cat":
        output = sql_cat.cat(loc)
        print(output)
        final_output = []
        cols = list(output.columns)
        fd_cols = {}
        for i, c in enumerate(cols):
            fd_cols['col'+str(i)] = c
        print(cols)
        for i in output.iterrows():
            final_output.append({
                'col0': i[1][cols[0]],
                'col1': i[1][cols[1]],
                'col2': i[1][cols[2]],
                'col3': i[1][cols[3]],
                'col4': i[1][cols[4]]
            })

        print(final_output)
        context = {
            'data': final_output,
            'cols': fd_cols
        }
        table_name = 'cat_table.html'

    elif cmd == "mkdir":

        output = sql_mkdir.mkdir(loc)
        print(output)
        for val in output:
            print(val)
            if '.' not in val:
                final_output.append({'location': val, 'type': 'Folder'})
            else:
                final_output.append({'location': val, 'type': 'File'})

        context = {
            'data': final_output,
        }
        table_name = 'gt_table.html'

    elif cmd == "rm":

        output = sql_rm.rm(loc)
        print(output)
        for val in output:
            print(val)
            if '.' not in val:
                final_output.append({'location': val, 'type': 'Folder'})
            else:
                final_output.append({'location': val, 'type': 'File'})

        context = {
            'data': final_output,
        }
        table_name = 'gt_table.html'

    elif cmd == "readPartition":
        loc_split = loc.split()
        loc = ' '.join(loc_split[:-1])
        num = int(loc_split[-1])
        print(loc, num)
        output = sql_readPartition.readPartition(loc, num)
        print(output)
        final_output = []
        cols = list(output.columns)
        fd_cols = {}
        for i, c in enumerate(cols):
            fd_cols['col'+str(i)] = c
        print(cols)
        for i in output.iterrows():
            final_output.append({
                'col0': i[1][cols[0]],
                'col1': i[1][cols[1]],
                'col2': i[1][cols[2]],
                'col3': i[1][cols[3]],
                'col4': i[1][cols[4]]
            })

        print(final_output)
        context = {
            'data': final_output,
            'cols': fd_cols
        }
        table_name = 'cat_table.html'

    elif cmd == "getPartitionLocations":

        file, output = sql_getPartition.getPartitionLocations(loc)
        print(output)
        for val in output:
            print(val)
            final_output.append({'file': file, 'location': val})

        context = {
            'data': final_output,
        }
        table_name = 'getPartition_table.html'

    return table_name, context

# Endpoint 2 for message
def message_ajax(request):
    if request.method == 'POST':
        command_input = request.POST.get('command_input', None)
        type1 = request.POST.get('type', None)

        # get command and location
        cmd = command_input.split()[0]
        loc = ' '.join(command_input.split()[1:])
        print("CMD: ", cmd)
        print("LOC: ", loc)
        
        # print(command_input, type1)
        if type1 == 'sql':
            table_name, context = sql(cmd, loc)
        else:
            table_name, context = firebase(cmd, loc) 
            

        
        data = {'rendered_data': render_to_string(table_name, context=context)}

        return JsonResponse(data)



# Endpoint 1 for form
def form_ajax2(request):
    print(request.method)
    if request.method == 'POST':
        select = request.POST.get('select')
        from1 = request.POST.get('from')
        where = request.POST.get('where')
        sign = request.POST.get('sign')
        value = request.POST.get('value')
        type1 = request.POST.get('type')

        print(select, from1, where, sign, value, type1)
        response = {
                'select': select,
                'from': from1,
                'where': where,
                'sign': sign,
                'value': value,
                'type': type1,
        }
        print(response)
        return JsonResponse(response)

def firebase_search(select, from1, where, sign, value):

    output = show.main(select, from1, where, sign, value)
    print(output)
    final_output = []
    cols = list(output.columns)
    fd_cols = {}
    for i, c in enumerate(cols):
        fd_cols['col'+str(i)] = c
    print(cols)
    for i in output.iterrows():
        final_output.append({
            'col0': i[1][cols[0]],
            'col1': i[1][cols[1]],
            'col2': i[1][cols[2]],
            'col3': i[1][cols[3]],
            'col4': i[1][cols[4]]
        })

    print(final_output)
    context = {
        'data': final_output,
        'cols': fd_cols
    }
    table_name = 'cat_table.html'

    return table_name, context

# Endpoint 2 for message
def message_ajax2(request):
    print(request.method)
    if request.method == 'POST':
        select = request.POST.get('select')
        from1 = request.POST.get('from')
        where = request.POST.get('where')
        sign = request.POST.get('sign')
        value = request.POST.get('value')
        type1 = request.POST.get('type')
        
        print(select, from1, where, sign, value, type1)
        if type1 == 'sql':
            table_name, context = sql(select, from1, where, sign, value)
        else:
            table_name, context = firebase_search(select, from1, where, sign, value)
            

        # data = {}
        data = {'rendered_data': render_to_string(table_name, context=context)}

        return JsonResponse(data)





# Endpoint 1 for form
def form_ajax3(request):
    print(request.method)
    if request.method == 'POST':
        q = request.POST.get('q')
        type1 = request.POST.get('type')

        print(q, type1)
        response = {
                'q': q,
                'type': type1,
        }
        print(response)
        return JsonResponse(response)



# Endpoint 2 for message
def message_ajax3(request):
    print(request.method)
    if request.method == 'POST':
        q = request.POST.get('q')
        type1 = request.POST.get('type')

        print(q, type1)
        if type1 == 'sql':
            final = sql_main(q)
        else:
            final = analytics.firebase_analytics(q)

        responsejson = json.dumps(final, cls=NumpyEncoder)

    return JsonResponse(responsejson, safe=False)