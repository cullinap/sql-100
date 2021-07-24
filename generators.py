import os
import nbformat as nbf
import mdutils

def ktx_to_dict(input_file, keystarter='<'):
    answer = {}

    with open(input_file, 'r+', encoding='utf-8') as f:
        lines = f.readlines()

    k,val = '',''
    for line in lines:
        if line.startswith(keystarter):
            k = line.replace(keystarter, '').strip()
            val = ''
        else:
            val += line
        if k:
            answer.update({k:val.strip()})

    return answer        

HEADERS = ktx_to_dict(os.path.join('headers.ktx'))
QHA = ktx_to_dict(os.path.join('exercises.ktx'))

def create_jupyter_notebook_random_question(destination_filename='100_Numpy_random.ipynb'):
    
    # delete file if one with same name exists
    if os.path.exists(destination_filename):
        os.remove(destination_filename)

    # create cells sequence
    nb = nbf.v4.new_notebook()

    nb['cells'] = []

    nb['cells'].append(nbf.v4.new_markdown_cell(HEADERS["header"]))

    # code cell
    nb['cells'].append(nbf.v4.new_code_cell('%run initialize.py'))
    nb['cells'].append(nbf.v4.new_code_cell('pick()'))

    nbf.write(nb, destination_filename)

if __name__ == '__main__':
    create_jupyter_notebook_random_question()


