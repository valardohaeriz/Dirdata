import os
import json

"""
Dirdata:

is the file where you are going to save your data example>> D: or a file directory 
example--> 'C:\\Users\\User\\Desktop\\New folder'

Find(D:, id) 
find('C:\\Users\\User\\Desktop\\New folder', id)

>>find.loads: will give you a json as dictionary

>>find.string(2, True): will give you a json as string
  (2, True) ---> (indent=2, sort_keys=True) in the json.dumps method
  the default value is (indent=2, sort_keys=False)

---------
>>Generate

get_id() #function

"""


class Location:
    def __init__(self, path):
        self.path = '{}\\__DATA__'.format(path)
        make_directory = r'{}'.format(self.path)
        if not os.path.isdir(make_directory):
            os.mkdir(make_directory)


class Find(Location):

    def __init__(self, path, _id_):
        super().__init__(path)
        self.id = _id_

    def split_id(self):
        """this function split the id and give us the directory id ex: '3:1:1:1:2:3:1:1:1:4'"""
        dir_id = self.id.split('|')[0].split(':')
        return dir_id

    def counter(self):
        """this function give us a number that will help to separate the id from JSON in the _K_ file"""
        count = 1
        for _ in self.id:
            count += 1
        return count

    @property
    def loads(self):
        value = self.split_id()
        dir_path = "{}\\_Nonillion_{}\\_Octillion_{}\\_Septillion_{}\\_Sextillion_{}\\_Quintillion_{}" \
                   "\\_Quantillion_{}\\_Trillion_{}\\_Billion_{}\\_Million_{}\\_K_{}.json".format(self.path, value[0],
                                                                                                  value[1], value[2],
                                                                                                  value[3], value[4],
                                                                                                  value[5], value[6],
                                                                                                  value[7], value[8],
                                                                                                  value[9])
        _data_ = {}
        try:
            file = open(dir_path, 'r')
            for line in file:
                if line.startswith(self.id):
                    _data_ = line[self.counter():]
                    break
            file.close()
        except OSError as err:
            print('OS error: {0}'.format(err))
        return json.loads(_data_)

    def string(self, value=2, bol=False):
        return json.dumps(self.loads, indent=value, sort_keys=bol)

    def delete(self):
        value = self.split_id()
        dir_path = "{}\\_Nonillion_{}\\_Octillion_{}\\_Septillion_{}\\_Sextillion_{}\\_Quintillion_{}" \
                   "\\_Quantillion_{}\\_Trillion_{}\\_Billion_{}\\_Million_{}\\_K_{}.json".format(self.path, value[0],
                                                                                                  value[1], value[2],
                                                                                                  value[3], value[4],
                                                                                                  value[5], value[6],
                                                                                                  value[7], value[8],
                                                                                                  value[9])
        with open(dir_path, "r") as f:
            lines = f.readlines()
        with open(dir_path, "w") as f:
            for line in lines:
                if not line.startswith(self.id):
                    f.write(line)
        save_in = open('{}\\_SaveD_.txt'.format(self.path), 'a')
        save_in.write(self.id+'\n')
        save_in.close()


class Generate(Location):

    def __init__(self, path, data):
        super().__init__(path)
        self.data = data

    def __folder_creator__(self, n, o, sep, sex, qui, qua, t, b, m):

        _n_ = r'{}\\_Nonillion_{}'.format(self.path, n)
        if not os.path.isdir(_n_):
            os.mkdir(_n_)

        _o_ = r'{}\\_Nonillion_{}\\_Octillion_{}'.format(self.path, n, o)
        if not os.path.isdir(_o_):
            os.mkdir(_o_)

        _sep_ = r'{}\\_Nonillion_{}\\_Octillion_{}\\_Septillion_{}'.format(self.path, n, o, sep)
        if not os.path.isdir(_sep_):
            os.mkdir(_sep_)

        _sex_ = r'{}\\_Nonillion_{}\\_Octillion_{}\\_Septillion_{}\\_Sextillion_{}'.format(self.path, n, o, sep, sex)
        if not os.path.isdir(_sex_):
            os.mkdir(_sex_)

        _qui_ = r'{}\\_Nonillion_{}\\_Octillion_{}\\_Septillion_{}\\_Sextillion_{}\\_Quintillion_{}'. \
            format(self.path, n, o, sep, sex, qui)
        if not os.path.isdir(_qui_):
            os.mkdir(_qui_)

        _qua_ = r'{}\\_Nonillion_{}\\_Octillion_{}\\_Septillion_{}\\_Sextillion_{}\\_Quintillion_{}\\_Quantillion_{}' \
            .format(self.path, n, o, sep, sex, qui, qua)
        if not os.path.isdir(_qua_):
            os.mkdir(_qua_)

        _t_ = r'{}\\_Nonillion_{}\\_Octillion_{}\\_Septillion_{}\\_Sextillion_{}\\_Quintillion_{}\\_Quantillion_{}\\' \
              r'_Trillion_{}'.format(self.path, n, o, sep, sex, qui, qua, t)
        if not os.path.isdir(_t_):
            os.mkdir(_t_)
        _b_ = r'{}\\_Nonillion_{}\\_Octillion_{}\\_Septillion_{}\\_Sextillion_{}\\_Quintillion_{}\\_Quantillion_{}\\' \
              r'_Trillion_{}\\_Billion_{}'.format(self.path, n, o, sep, sex, qui, qua, t, b)
        if not os.path.isdir(_b_):
            os.mkdir(_b_)
        _m_ = r'{}\\_Nonillion_{}\\_Octillion_{}\\_Septillion_{}\\_Sextillion_{}\\_Quintillion_{}\\_Quantillion_{}\\' \
              r'_Trillion_{}\\_Billion_{}\\_Million_{}'.format(self.path, n, o, sep, sex, qui, qua, t, b, m)
        if not os.path.isdir(_m_):
            os.mkdir(_m_)

        folder_dir = r'{}\\_Nonillion_{}\\_Octillion_{}\\_Septillion_{}\\_Sextillion_{}\\_Quintillion_{}\\' \
                     r'_Quantillion_{}\\_Trillion_{}\\_Billion_{}\\_Million_{}'.format(self.path, n, o, sep, sex,
                                                                                       qui, qua, t, b, m)
        return folder_dir

    @staticmethod
    def split_id(_id_):
        dir_id = _id_.split('|')[0].split(':')
        return dir_id

    def insert(self):
        if os.path.isfile('{}\\_SaveD_.txt'.format(self.path)):
            file = open('{}\\_SaveD_.txt'.format(self.path), "r")
            lines = file.readlines()
            file.close()
            count = 0
            for _ in lines:
                count += 1
            if count == 0:
                os.remove('{}\\_SaveD_.txt'.format(self.path))

        if os.path.isfile('{}\\_SaveD_.txt'.format(self.path)):
            save_out = open('{}\\_SaveD_.txt'.format(self.path))
            id_path = save_out.readline()
            save_out.close()
            value = self.split_id(id_path)
            k = int(value[9])
            m = int(value[8])
            b = int(value[7])
            t = int(value[6])
            qua = int(value[5])
            qui = int(value[4])
            sex = int(value[3])
            sep = int(value[2])
            o = int(value[1])
            non = int(value[0])
            data_count = int(value[10])

        elif os.path.isfile('{}\\_SaveID_.txt'.format(self.path)):
            save_out = open('{}\\_SaveID_.txt'.format(self.path))
            id_path = save_out.readline()
            save_out.close()
            value = self.split_id(id_path)
            k = int(value[9])
            m = int(value[8])
            b = int(value[7])
            t = int(value[6])
            qua = int(value[5])
            qui = int(value[4])
            sex = int(value[3])
            sep = int(value[2])
            o = int(value[1])
            non = int(value[0])
            data_count = int(value[10])
        else:
            k = 1
            m = 1
            b = 1
            t = 1
            qua = 1
            qui = 1
            sex = 1
            sep = 1
            o = 1
            non = 1
            data_count = 0
        path = ''
        for _ in range(1):
            if not os.path.isfile('{}\\_SaveD_.txt'.format(self.path)):
                data_count += 1

            path = '{}:{}:{}:{}:{}:{}:{}:{}:{}:{}:{}'.format(non, o, sep, sex, qui,
                                                             qua, t, b, m, k,
                                                             data_count)
            if not os.path.isfile('{}\\_SaveD_.txt'.format(self.path)):
                save_in = open('{}\\_SaveID_.txt'.format(self.path), 'w')
                save_in.write(path)
                save_in.close()
                if data_count == 1001:
                    data_count = 1
                    k += 1
                    path = '{}:{}:{}:{}:{}:{}:{}:{}:{}:{}:{}'.format(non, o, sep, sex, qui,
                                                                     qua, t, b, m, k,
                                                                     data_count)
                    save_in = open('{}\\_SaveID_.txt'.format(self.path), 'w')
                    save_in.write(path)
                    save_in.close()
                if k == 1001:
                    data_count = 1
                    k = 1
                    m += 1
                    path = '{}:{}:{}:{}:{}:{}:{}:{}:{}:{}:{}'.format(non, o, sep, sex, qui,
                                                                     qua, t, b, m, k,
                                                                     data_count)
                    save_in = open('{}\\_SaveID_.txt'.format(self.path), 'w')
                    save_in.write(path)
                    save_in.close()
                if m == 1001:
                    data_count = 1
                    k = 1
                    m = 1
                    b += 1
                    path = '{}:{}:{}:{}:{}:{}:{}:{}:{}:{}:{}'.format(non, o, sep, sex, qui,
                                                                     qua, t, b, m, k,
                                                                     data_count)
                    save_in = open('{}\\_SaveID_.txt'.format(self.path), 'w')
                    save_in.write(path)
                    save_in.close()
                if b == 1001:
                    data_count = 1
                    k = 1
                    m = 1
                    b = 1
                    t += 1
                    path = '{}:{}:{}:{}:{}:{}:{}:{}:{}:{}:{}'.format(non, o, sep, sex, qui,
                                                                     qua, t, b, m, k,
                                                                     data_count)
                    save_in = open('{}\\_SaveID_.txt'.format(self.path), 'w')
                    save_in.write(path)
                    save_in.close()
                if t == 1001:
                    data_count = 1
                    k = 1
                    m = 1
                    b = 1
                    t = 1
                    qua += 1
                    path = '{}:{}:{}:{}:{}:{}:{}:{}:{}:{}:{}'.format(non, o, sep, sex, qui,
                                                                     qua, t, b, m, k,
                                                                     data_count)
                    save_in = open('{}\\_SaveID_.txt'.format(self.path), 'w')
                    save_in.write(path)
                    save_in.close()
                if qua == 1001:
                    data_count = 1
                    k = 1
                    m = 1
                    b = 1
                    t = 1
                    qua = 1
                    qui += 1
                    path = '{}:{}:{}:{}:{}:{}:{}:{}:{}:{}:{}'.format(non, o, sep, sex, qui,
                                                                     qua, t, b, m, k,
                                                                     data_count)
                    save_in = open('{}\\_SaveID_.txt'.format(self.path), 'w')
                    save_in.write(path)
                    save_in.close()
                if qui == 1001:
                    data_count = 1
                    k = 1
                    m = 1
                    b = 1
                    t = 1
                    qua = 1
                    qui = 1
                    sex += 1
                    path = '{}:{}:{}:{}:{}:{}:{}:{}:{}:{}:{}'.format(non, o, sep, sex, qui,
                                                                     qua, t, b, m, k,
                                                                     data_count)
                    save_in = open('{}\\_SaveID_.txt'.format(self.path), 'w')
                    save_in.write(path)
                    save_in.close()
                if sex == 1001:
                    data_count = 1
                    k = 1
                    m = 1
                    b = 1
                    t = 1
                    qua = 1
                    qui = 1
                    sex = 1
                    sep += 1
                    path = '{}:{}:{}:{}:{}:{}:{}:{}:{}:{}:{}'.format(non, o, sep, sex, qui,
                                                                     qua, t, b, m, k,
                                                                     data_count)
                    save_in = open('{}\\_SaveID_.txt'.format(self.path), 'w')
                    save_in.write(path)
                    save_in.close()
                if sep == 1001:
                    data_count = 1
                    k = 1
                    m = 1
                    b = 1
                    t = 1
                    qua = 1
                    qui = 1
                    sex = 1
                    sep = 1
                    o += 1
                    path = '{}:{}:{}:{}:{}:{}:{}:{}:{}:{}:{}'.format(non, o, sep, sex, qui,
                                                                     qua, t, b, m, k,
                                                                     data_count)
                    save_in = open('{}\\_SaveID_.txt'.format(self.path), 'w')
                    save_in.write(path)
                    save_in.close()
                if o == 1001:
                    data_count = 1
                    k = 1
                    m = 1
                    b = 1
                    t = 1
                    qua = 1
                    qui = 1
                    sex = 1
                    sep = 1
                    o = 1
                    non += 1
                    path = '{}:{}:{}:{}:{}:{}:{}:{}:{}:{}:{}'.format(non, o, sep, sex, qui,
                                                                     qua, t, b, m, k,
                                                                     data_count)
                    save_in = open('{}\\_SaveID_.txt'.format(self.path), 'w')
                    save_in.write(path)
                    save_in.close()
            if os.path.isfile('{}\\_SaveD_.txt'.format(self.path)):

                with open('{}\\_SaveD_.txt'.format(self.path), "r") as f:
                    lines = f.readlines()
                with open('{}\\_SaveD_.txt'.format(self.path), "w") as f:
                    for line in lines:
                        if not line.startswith(path):
                            f.write(line)

        dire = self.__folder_creator__(non, o, sep, sex, qui, qua, t, b, m)
        os.chdir(str(dire))
        file_name = '_K_{}.json'.format(k)
        append_file = open(file_name, 'a')
        append_file.write(path + '|' + json.dumps(self.data) + '\n')
        append_file.close()
        return path
