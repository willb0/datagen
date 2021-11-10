import random
import string
import numpy as np


def dummy_json(schema_string):
    ## Example string name str|age int|salary float|60
    data_types = schema_string.split('|')
    data_dict = {}
    generation_length = int(data_types.pop())
    print(data_types)
    ## iterate through data types passed and create data
    for type_string in data_types:
        name, dtype = type_string.split(' ')
        if dtype == 'int':
            gen = random.sample(range(0,generation_length),generation_length)
            data_dict.update({name:gen})
        elif dtype == 'str':
            gen = [''.join(random.sample(string.ascii_letters,8)) for _ in range(generation_length)]
            data_dict.update({name:gen})
        elif dtype == 'float':
            gen = [random.random() * 10000 for _ in range(generation_length)]
            data_dict.update({name:gen})
        else:
            return {'data':'invalid dtype'}
    return data_dict
            
def dummy_sql(schema_string):
    data_types = schema_string.split('|')
    print(data_types)
    generation_length = int(data_types.pop())
    create_s = []
    data = []
    names = []
    for type_string in data_types:
        name, dtype = type_string.split(' ')
        names.append(name)
        if dtype == 'int':
            create_s.append(f'{name} int')
            gen = random.sample(range(0,generation_length),generation_length)
            data.append(gen)
        elif dtype == 'str':
            gen = [f'\'{"".join(random.sample(string.ascii_letters,8))}\'' for _ in range(generation_length)]
            create_s.append(f'{name} varchar')
            data.append(gen)
        elif dtype == 'float':
            gen = [random.random() * 10000 for _ in range(generation_length)]
            create_s.append(f'{name} float')
            data.append(gen)
        else:
            return {'data':'invalid dtype'}

    create_s = f'create table A({",".join(create_s)});'
    insert_s = f'insert into A ({",".join(names)}) values '
    data = np.array(data).T
    lines = []
    for row in data:
        lines.append(f'({",".join(row)}),')
    lines = ''.join(lines)[:-1]
    return ''.join([create_s,insert_s,lines]) + ';'



#c print(dummy_json('name str|age int|salary float|60'))

#def dummy_dbfiddle(schema_string):


