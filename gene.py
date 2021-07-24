import os
import pandas as pd
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
SQLQHA = ktx_to_dict(os.path.join('sqlexercises.ktx'))

def create_jupyter_notebook_random_question(destination_filename='random.ipynb'):
    
    # delete file if one with same name exists
    if os.path.exists(destination_filename):
        os.remove(destination_filename)

    # create cells sequence
    nb = nbf.v4.new_notebook()

    nb['cells'] = []

    #nb['cells'].append(nbf.v4.new_markdown_cell(HEADERS["header"]))

    # code cell
    nb['cells'].append(nbf.v4.new_code_cell('%run initialise.py'))
    nb['cells'].append(nbf.v4.new_code_cell('pick()'))

    nbf.write(nb, destination_filename)

# create a random sql notebook
# create a random data set for that notebook
def create_jupyter_notebook_sql_questions(destination_filename='sql_random.ipynb'):

    # delete file if one with same name exists
    if os.path.exists(destination_filename):
        os.remove(destination_filename)

    from sqlalchemy import create_engine
    engine = create_engine('sqlite://', echo=False)

    #     # join warmups
    url1 = 'https://raw.githubusercontent.com/CSSEGISandData/COVID-19/master/csse_covid_19_data/csse_covid_19_daily_reports/12-31-2020.csv'
    url2 = 'https://raw.githubusercontent.com/CSSEGISandData/COVID-19/master/csse_covid_19_data/csse_covid_19_daily_reports/12-27-2020.csv'

    # sqlimports = 'from sqlalchemy import create_engine\nengine = create_engine(\'sqlite://\', echo=False)'
    dfimports = '\ndf1 = pd.read_csv(url1)\ndf2 = pd.read_csv(url2)'
    sqlimports = 'from sqlalchemy import create_engine\nengine = create_engine(\'sqlite://\', echo=False)\nimport pandas as pd'
    dfsqlimports  = '\ndf1.to_sql(\'df1\',con=engine)\ndf2.to_sql(\'df2\',con=engine)'

    delete1 = '\nengine.execute(\'DROP TABLE IF EXISTS df1;\')'
    delete2 = '\nengine.execute(\'DROP TABLE IF EXISTS df2;\')'

     # create cells sequence
    nb = nbf.v4.new_notebook()

    nb['cells'] = []

    nb['cells'].append(nbf.v4.new_code_cell('%run initialise.py'))
    nb['cells'].append(nbf.v4.new_code_cell('intializeSQL()'))
    nb['cells'].append(nbf.v4.new_markdown_cell(HEADERS["header"]))
    nb['cells'].append(nbf.v4.new_code_cell(f'{sqlimports} {delete1} {delete2} \nurl1 = "{url1}" \nurl2 = "{url2}"' + dfimports + dfsqlimports))

    # code cell
    nb['cells'].append(nbf.v4.new_code_cell('pickSQL()'))

    nbf.write(nb, destination_filename)


if __name__ == '__main__':
    create_jupyter_notebook_random_question()
    create_jupyter_notebook_sql_questions()

















