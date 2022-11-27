from django.shortcuts import render
from django.http import JsonResponse
from django.http import HttpResponse
from django.template.loader import render_to_string
from edfs.firebase_cmd import ls, cat, mkdir, rm, readPartition, getPartitionLocations

# Create your views here.
def index(request):
    return render(request, 'index.html')

# Endpoint 1 for form
def form_ajax(request):
    if request.method == 'POST':
        command_input = request.POST.get('command_input', None)
        if command_input:
            response = {
                 'command_input': command_input,
            }
            return JsonResponse(response)

# Endpoint 2 for message
def message_ajax(request):
    if request.method == 'POST':
        command_input = request.POST.get('command_input', None)

        # get command and location
        cmd = command_input.split()[0]
        loc = ' '.join(command_input.split()[1:])
        print("CMD: ", cmd)
        print("LOC: ", loc)
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
            

        
        data = {'rendered_data': render_to_string(table_name, context=context)}

        return JsonResponse(data)
