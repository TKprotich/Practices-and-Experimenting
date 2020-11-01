Python 3.7.6 (default, Jan  8 2020, 20:23:39) [MSC v.1916 64 bit (AMD64)] on win32
Type "help", "copyright", "credits" or "license()" for more information.
>>> 
= RESTART: C:\Users\user\Documents\Practice\General Programing\chromeexte\clipboard\reading.py
2020, Nov , 1, 9, 69, 1115 

>>> fh.iloc[0]
Traceback (most recent call last):
  File "<pyshell#0>", line 1, in <module>
    fh.iloc[0]
NameError: name 'fh' is not defined
>>> 
============== RESTART: C:/Users/user/Desktop/powerpointcharts.py ==============
                      No/P Biochemistry Hormone hematology serology Urine Stool Coag Semen Swab culture
DOCTOR                                                                                                 
Dr wasem                21           21      32         28       29    15     0    0     0    0       0
Dr gayath               13           89       8         20        9     9     9    0     0    0       0
Dr Heytham               0            0       0          0        0     0     0    0     0    0       0
Dr maalin                8           19       0         12        2     1     8    0     0    0       0
ER                      12           47       4         17       18     5     5    3     0    0       0
Dr khaled               15           73       0         18       10     3     6    0     0    0       0
Dr Diini                 1            4       0          0        0     0     0    0     0    0       0
Dr Ghannam               0            0       0          0        0     0     0    0     0    0       0
Dr Ahmed Mohamed         6           21       0          9        4     0     0    3     0    0       0
Dr mohamed Farah Jama    3            9       1          3        0     0     0    0     0    0       0
Dr Rabie                 0            0       0          0        0     0     0    0     0    0       0
Dr Amir jabir            3            3       0          1        8     0     0    0     0    0       0
Dr Nabil Safiah          5            0       0          3        7     0     0    0     0    0       0
Dr RAniBahjad            3            2       0          4        5     1     1    0     0    0       0
Dr Rani bahjad           4            0       0          7       12     2     0    0     0    0       0
Jazira Lab               1            1       0          0        0     0     0    0     0    0       0
M Hersi                  2            2       1          4        0     0     0    0     0    0       1
Dr Rami                  2            4       0          3        4     0     3    3     0    0       0
Dr Maan                 17           43      23         10        8    11     2    3     3    0       3
Out site                 4            1       0          2        8     0     0    0     0    0       0
ER                      10           46       2         17        9     2     8    3     0    0       0
Dr shacban               4           14       0          8        5     1     0    0     0    0       0
Traceback (most recent call last):
  File "C:\Users\user\Anaconda3\lib\site-packages\pandas\core\indexes\base.py", line 2646, in get_loc
    return self._engine.get_loc(key)
  File "pandas\_libs\index.pyx", line 111, in pandas._libs.index.IndexEngine.get_loc
  File "pandas\_libs\index.pyx", line 138, in pandas._libs.index.IndexEngine.get_loc
  File "pandas\_libs\hashtable_class_helper.pxi", line 1618, in pandas._libs.hashtable.PyObjectHashTable.get_item
  File "pandas\_libs\hashtable_class_helper.pxi", line 1626, in pandas._libs.hashtable.PyObjectHashTable.get_item
KeyError: 'Dr wasem'

During handling of the above exception, another exception occurred:

Traceback (most recent call last):
  File "C:/Users/user/Desktop/powerpointcharts.py", line 157, in <module>
    presentation(fh)
  File "C:/Users/user/Desktop/powerpointcharts.py", line 84, in presentation
    chart_data.add_series('Series 1', (k for k in fh[i][1:]))
  File "C:\Users\user\Anaconda3\lib\site-packages\pandas\core\frame.py", line 2800, in __getitem__
    indexer = self.columns.get_loc(key)
  File "C:\Users\user\Anaconda3\lib\site-packages\pandas\core\indexes\base.py", line 2648, in get_loc
    return self._engine.get_loc(self._maybe_cast_indexer(key))
  File "pandas\_libs\index.pyx", line 111, in pandas._libs.index.IndexEngine.get_loc
  File "pandas\_libs\index.pyx", line 138, in pandas._libs.index.IndexEngine.get_loc
  File "pandas\_libs\hashtable_class_helper.pxi", line 1618, in pandas._libs.hashtable.PyObjectHashTable.get_item
  File "pandas\_libs\hashtable_class_helper.pxi", line 1626, in pandas._libs.hashtable.PyObjectHashTable.get_item
KeyError: 'Dr wasem'
>>> fh.iloc[0]
No/P            21
Biochemistry    21
Hormone         32
hematology      28
serology        29
Urine           15
Stool            0
Coag             0
Semen            0
Swab             0
culture          0
Name: Dr wasem, dtype: object
>>> fh.iloc[[0]]
         No/P Biochemistry Hormone hematology serology Urine Stool Coag Semen Swab culture
DOCTOR                                                                                    
Dr wasem   21           21      32         28       29    15     0    0     0    0       0
>>> fh.iloc[[1]]
          No/P Biochemistry Hormone hematology serology Urine Stool Coag Semen Swab culture
DOCTOR                                                                                     
Dr gayath   13           89       8         20        9     9     9    0     0    0       0
>>> fh.iloc[0]
No/P            21
Biochemistry    21
Hormone         32
hematology      28
serology        29
Urine           15
Stool            0
Coag             0
Semen            0
Swab             0
culture          0
Name: Dr wasem, dtype: object
>>> fh.iloc[[1:]]
SyntaxError: invalid syntax
>>> fh.iloc[1: [1]]
Traceback (most recent call last):
  File "<pyshell#6>", line 1, in <module>
    fh.iloc[1: [1]]
  File "C:\Users\user\Anaconda3\lib\site-packages\pandas\core\indexing.py", line 1767, in __getitem__
    return self._getitem_axis(maybe_callable, axis=axis)
  File "C:\Users\user\Anaconda3\lib\site-packages\pandas\core\indexing.py", line 2117, in _getitem_axis
    return self._get_slice_axis(key, axis=axis)
  File "C:\Users\user\Anaconda3\lib\site-packages\pandas\core\indexing.py", line 1748, in _get_slice_axis
    indexer = self._convert_slice_indexer(slice_obj, axis)
  File "C:\Users\user\Anaconda3\lib\site-packages\pandas\core\indexing.py", line 745, in _convert_slice_indexer
    return ax._convert_slice_indexer(key, kind=self.name)
  File "C:\Users\user\Anaconda3\lib\site-packages\pandas\core\indexes\base.py", line 2914, in _convert_slice_indexer
    self._validate_indexer("slice", key.stop, kind),
  File "C:\Users\user\Anaconda3\lib\site-packages\pandas\core\indexes\base.py", line 4750, in _validate_indexer
    self._invalid_indexer(form, key)
  File "C:\Users\user\Anaconda3\lib\site-packages\pandas\core\indexes\base.py", line 3077, in _invalid_indexer
    f"cannot do {form} indexing on {type(self)} with these "
TypeError: cannot do slice indexing on <class 'pandas.core.indexes.base.Index'> with these indexers [[1]] of <class 'list'>
>>> fh.iloc[1, [1]]
Biochemistry    89
Name: Dr gayath, dtype: object
>>> fh.iloc[[1], 1]
DOCTOR
Dr gayath    89
Name: Biochemistry, dtype: object
>>> fh.iloc[:1]
         No/P Biochemistry Hormone hematology serology Urine Stool Coag Semen Swab culture
DOCTOR                                                                                    
Dr wasem   21           21      32         28       29    15     0    0     0    0       0
>>> fh.iloc[:13]
                      No/P Biochemistry Hormone hematology serology Urine Stool Coag Semen Swab culture
DOCTOR                                                                                                 
Dr wasem                21           21      32         28       29    15     0    0     0    0       0
Dr gayath               13           89       8         20        9     9     9    0     0    0       0
Dr Heytham               0            0       0          0        0     0     0    0     0    0       0
Dr maalin                8           19       0         12        2     1     8    0     0    0       0
ER                      12           47       4         17       18     5     5    3     0    0       0
Dr khaled               15           73       0         18       10     3     6    0     0    0       0
Dr Diini                 1            4       0          0        0     0     0    0     0    0       0
Dr Ahmed Mohamed         6           21       0          9        4     0     0    3     0    0       0
Dr mohamed Farah Jama    3            9       1          3        0     0     0    0     0    0       0
Dr Amir jabir            3            3       0          1        8     0     0    0     0    0       0
Dr Nabil Safiah          5            0       0          3        7     0     0    0     0    0       0
Dr RAniBahjad            3            2       0          4        5     1     1    0     0    0       0
Dr Rani bahjad           4            0       0          7       12     2     0    0     0    0       0
>>> fh.iloc[:1]
         No/P Biochemistry Hormone hematology serology Urine Stool Coag Semen Swab culture
DOCTOR                                                                                    
Dr wasem   21           21      32         28       29    15     0    0     0    0       0
>>> fh.iloc[:1][1:]
Empty DataFrame
Columns: [No/P, Biochemistry, Hormone, hematology, serology, Urine, Stool, Coag, Semen, Swab, culture]
Index: []
>>> fh.iloc[:1][1]
Traceback (most recent call last):
  File "C:\Users\user\Anaconda3\lib\site-packages\pandas\core\indexes\base.py", line 2646, in get_loc
    return self._engine.get_loc(key)
  File "pandas\_libs\index.pyx", line 111, in pandas._libs.index.IndexEngine.get_loc
  File "pandas\_libs\index.pyx", line 138, in pandas._libs.index.IndexEngine.get_loc
  File "pandas\_libs\hashtable_class_helper.pxi", line 1618, in pandas._libs.hashtable.PyObjectHashTable.get_item
  File "pandas\_libs\hashtable_class_helper.pxi", line 1626, in pandas._libs.hashtable.PyObjectHashTable.get_item
KeyError: 1

During handling of the above exception, another exception occurred:

Traceback (most recent call last):
  File "<pyshell#13>", line 1, in <module>
    fh.iloc[:1][1]
  File "C:\Users\user\Anaconda3\lib\site-packages\pandas\core\frame.py", line 2800, in __getitem__
    indexer = self.columns.get_loc(key)
  File "C:\Users\user\Anaconda3\lib\site-packages\pandas\core\indexes\base.py", line 2648, in get_loc
    return self._engine.get_loc(self._maybe_cast_indexer(key))
  File "pandas\_libs\index.pyx", line 111, in pandas._libs.index.IndexEngine.get_loc
  File "pandas\_libs\index.pyx", line 138, in pandas._libs.index.IndexEngine.get_loc
  File "pandas\_libs\hashtable_class_helper.pxi", line 1618, in pandas._libs.hashtable.PyObjectHashTable.get_item
  File "pandas\_libs\hashtable_class_helper.pxi", line 1626, in pandas._libs.hashtable.PyObjectHashTable.get_item
KeyError: 1
>>> fh.iloc[:1][2:]
Empty DataFrame
Columns: [No/P, Biochemistry, Hormone, hematology, serology, Urine, Stool, Coag, Semen, Swab, culture]
Index: []
>>> fh[fh[3]]
Traceback (most recent call last):
  File "C:\Users\user\Anaconda3\lib\site-packages\pandas\core\indexes\base.py", line 2646, in get_loc
    return self._engine.get_loc(key)
  File "pandas\_libs\index.pyx", line 111, in pandas._libs.index.IndexEngine.get_loc
  File "pandas\_libs\index.pyx", line 138, in pandas._libs.index.IndexEngine.get_loc
  File "pandas\_libs\hashtable_class_helper.pxi", line 1618, in pandas._libs.hashtable.PyObjectHashTable.get_item
  File "pandas\_libs\hashtable_class_helper.pxi", line 1626, in pandas._libs.hashtable.PyObjectHashTable.get_item
KeyError: 3

During handling of the above exception, another exception occurred:

Traceback (most recent call last):
  File "<pyshell#15>", line 1, in <module>
    fh[fh[3]]
  File "C:\Users\user\Anaconda3\lib\site-packages\pandas\core\frame.py", line 2800, in __getitem__
    indexer = self.columns.get_loc(key)
  File "C:\Users\user\Anaconda3\lib\site-packages\pandas\core\indexes\base.py", line 2648, in get_loc
    return self._engine.get_loc(self._maybe_cast_indexer(key))
  File "pandas\_libs\index.pyx", line 111, in pandas._libs.index.IndexEngine.get_loc
  File "pandas\_libs\index.pyx", line 138, in pandas._libs.index.IndexEngine.get_loc
  File "pandas\_libs\hashtable_class_helper.pxi", line 1618, in pandas._libs.hashtable.PyObjectHashTable.get_item
  File "pandas\_libs\hashtable_class_helper.pxi", line 1626, in pandas._libs.hashtable.PyObjectHashTable.get_item
KeyError: 3
>>> fh[fh.columns[0]]
DOCTOR
Dr wasem                 21
Dr gayath                13
Dr Heytham                0
Dr maalin                 8
ER                       12
Dr khaled                15
Dr Diini                  1
Dr Ahmed Mohamed          6
Dr mohamed Farah Jama     3
Dr Amir jabir             3
Dr Nabil Safiah           5
Dr RAniBahjad             3
Dr Rani bahjad            4
Jazira Lab                1
M Hersi                   2
Dr Rami                   2
Dr Maan                  17
Out site                  4
ER                       10
Dr shacban                4
Name: No/P, dtype: object
>>> fh[fh.columns[5]]
DOCTOR
Dr wasem                 15
Dr gayath                 9
Dr Heytham                0
Dr maalin                 1
ER                        5
Dr khaled                 3
Dr Diini                  0
Dr Ahmed Mohamed          0
Dr mohamed Farah Jama     0
Dr Amir jabir             0
Dr Nabil Safiah           0
Dr RAniBahjad             1
Dr Rani bahjad            2
Jazira Lab                0
M Hersi                   0
Dr Rami                   0
Dr Maan                  11
Out site                  0
ER                        2
Dr shacban                1
Name: Urine, dtype: object
>>> 
===================================== RESTART: C:\Users\user\Documents\Practice\General Programing\chromeexte\clipboard\reading.py ====================================
2020, Nov , 1, 9, 22, 423 

>>> 
===================================== RESTART: C:\Users\user\Documents\Practice\General Programing\chromeexte\clipboard\reading.py ====================================
2020, Nov , 1, 9, 40, 769 

>>> 
===================================== RESTART: C:\Users\user\Documents\Practice\General Programing\chromeexte\clipboard\reading.py ====================================
2020, Nov , 1, 9, 18, 325 

>>> fh[1:3]
Traceback (most recent call last):
  File "<pyshell#18>", line 1, in <module>
    fh[1:3]
NameError: name 'fh' is not defined
>>> 
========================================================== RESTART: C:/Users/user/Desktop/powerpointcharts.py =========================================================
                      No/P Biochemistry Hormone hematology serology Urine Stool Coag Semen Swab culture
DOCTOR                                                                                                 
Dr wasem                21           21      32         28       29    15     0    0     0    0       0
Dr gayath               13           89       8         20        9     9     9    0     0    0       0
Dr Heytham               0            0       0          0        0     0     0    0     0    0       0
Dr maalin                8           19       0         12        2     1     8    0     0    0       0
ER                      12           47       4         17       18     5     5    3     0    0       0
Dr khaled               15           73       0         18       10     3     6    0     0    0       0
Dr Diini                 1            4       0          0        0     0     0    0     0    0       0
Dr Ghannam               0            0       0          0        0     0     0    0     0    0       0
Dr Ahmed Mohamed         6           21       0          9        4     0     0    3     0    0       0
Dr mohamed Farah Jama    3            9       1          3        0     0     0    0     0    0       0
Dr Rabie                 0            0       0          0        0     0     0    0     0    0       0
Dr Amir jabir            3            3       0          1        8     0     0    0     0    0       0
Dr Nabil Safiah          5            0       0          3        7     0     0    0     0    0       0
Dr RAniBahjad            3            2       0          4        5     1     1    0     0    0       0
Dr Rani bahjad           4            0       0          7       12     2     0    0     0    0       0
Jazira Lab               1            1       0          0        0     0     0    0     0    0       0
M Hersi                  2            2       1          4        0     0     0    0     0    0       1
Dr Rami                  2            4       0          3        4     0     3    3     0    0       0
Dr Maan                 17           43      23         10        8    11     2    3     3    0       3
Out site                 4            1       0          2        8     0     0    0     0    0       0
ER                      10           46       2         17        9     2     8    3     0    0       0
Dr shacban               4           14       0          8        5     1     0    0     0    0       0
Traceback (most recent call last):
  File "C:\Users\user\Anaconda3\lib\site-packages\pandas\core\indexes\base.py", line 2646, in get_loc
    return self._engine.get_loc(key)
  File "pandas\_libs\index.pyx", line 111, in pandas._libs.index.IndexEngine.get_loc
  File "pandas\_libs\index.pyx", line 138, in pandas._libs.index.IndexEngine.get_loc
  File "pandas\_libs\hashtable_class_helper.pxi", line 1618, in pandas._libs.hashtable.PyObjectHashTable.get_item
  File "pandas\_libs\hashtable_class_helper.pxi", line 1626, in pandas._libs.hashtable.PyObjectHashTable.get_item
KeyError: 'Dr wasem'

During handling of the above exception, another exception occurred:

Traceback (most recent call last):
  File "C:/Users/user/Desktop/powerpointcharts.py", line 157, in <module>
    presentation(fh)
  File "C:/Users/user/Desktop/powerpointcharts.py", line 84, in presentation
    chart_data.add_series('Series 1', (k for k in fh[i][1:]))
  File "C:\Users\user\Anaconda3\lib\site-packages\pandas\core\frame.py", line 2800, in __getitem__
    indexer = self.columns.get_loc(key)
  File "C:\Users\user\Anaconda3\lib\site-packages\pandas\core\indexes\base.py", line 2648, in get_loc
    return self._engine.get_loc(self._maybe_cast_indexer(key))
  File "pandas\_libs\index.pyx", line 111, in pandas._libs.index.IndexEngine.get_loc
  File "pandas\_libs\index.pyx", line 138, in pandas._libs.index.IndexEngine.get_loc
  File "pandas\_libs\hashtable_class_helper.pxi", line 1618, in pandas._libs.hashtable.PyObjectHashTable.get_item
  File "pandas\_libs\hashtable_class_helper.pxi", line 1626, in pandas._libs.hashtable.PyObjectHashTable.get_item
KeyError: 'Dr wasem'
>>> fh.[1:3]
SyntaxError: invalid syntax
>>> fh[1:3]
           No/P Biochemistry Hormone hematology serology Urine Stool Coag Semen Swab culture
DOCTOR                                                                                      
Dr gayath    13           89       8         20        9     9     9    0     0    0       0
Dr Heytham    0            0       0          0        0     0     0    0     0    0       0
>>> fh.iloc[2]
No/P            0
Biochemistry    0
Hormone         0
hematology      0
serology        0
Urine           0
Stool           0
Coag            0
Semen           0
Swab            0
culture         0
Name: Dr Heytham, dtype: object
>>> [i for i in fh.iloc[2]]
[0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
>>> [i for i in fh.iloc[1]]
[13, 89, 8, 20, 9, 9, 9, 0, 0, 0, 0]
>>> [i for i in fh.iloc[0]]
[21, 21, 32, 28, 29, 15, 0, 0, 0, 0, 0]
>>> [i for i in fh.iloc[1, [1]]
 ]
[89]
>>> fh.iloc[1, [1]]
Biochemistry    89
Name: Dr gayath, dtype: object
>>> fh.iloc[[1:], [1]]
SyntaxError: invalid syntax
>>> [i for i in fh.iloc[0]]
[21, 21, 32, 28, 29, 15, 0, 0, 0, 0, 0]
>>> [i for i in fh.drop(columns = 0).iloc[0]]
Traceback (most recent call last):
  File "<pyshell#30>", line 1, in <module>
    [i for i in fh.drop(columns = 0).iloc[0]]
  File "C:\Users\user\Anaconda3\lib\site-packages\pandas\core\frame.py", line 3997, in drop
    errors=errors,
  File "C:\Users\user\Anaconda3\lib\site-packages\pandas\core\generic.py", line 3936, in drop
    obj = obj._drop_axis(labels, axis, level=level, errors=errors)
  File "C:\Users\user\Anaconda3\lib\site-packages\pandas\core\generic.py", line 3970, in _drop_axis
    new_axis = axis.drop(labels, errors=errors)
  File "C:\Users\user\Anaconda3\lib\site-packages\pandas\core\indexes\base.py", line 5018, in drop
    raise KeyError(f"{labels[mask]} not found in axis")
KeyError: '[0] not found in axis'
>>> [i for i in fh.drop(columns = 0)]
Traceback (most recent call last):
  File "<pyshell#31>", line 1, in <module>
    [i for i in fh.drop(columns = 0)]
  File "C:\Users\user\Anaconda3\lib\site-packages\pandas\core\frame.py", line 3997, in drop
    errors=errors,
  File "C:\Users\user\Anaconda3\lib\site-packages\pandas\core\generic.py", line 3936, in drop
    obj = obj._drop_axis(labels, axis, level=level, errors=errors)
  File "C:\Users\user\Anaconda3\lib\site-packages\pandas\core\generic.py", line 3970, in _drop_axis
    new_axis = axis.drop(labels, errors=errors)
  File "C:\Users\user\Anaconda3\lib\site-packages\pandas\core\indexes\base.py", line 5018, in drop
    raise KeyError(f"{labels[mask]} not found in axis")
KeyError: '[0] not found in axis'
>>> fh.iloc[3:5, 0:2
	]
          No/P Biochemistry
DOCTOR                     
Dr maalin    8           19
ER          12           47
>>> f.iloc[0:, 0:2]
Traceback (most recent call last):
  File "<pyshell#34>", line 1, in <module>
    f.iloc[0:, 0:2]
NameError: name 'f' is not defined
>>> 
>>> fh.iloc[0:, 0:2]
                      No/P Biochemistry
DOCTOR                                 
Dr wasem                21           21
Dr gayath               13           89
Dr Heytham               0            0
Dr maalin                8           19
ER                      12           47
Dr khaled               15           73
Dr Diini                 1            4
Dr Ahmed Mohamed         6           21
Dr mohamed Farah Jama    3            9
Dr Amir jabir            3            3
Dr Nabil Safiah          5            0
Dr RAniBahjad            3            2
Dr Rani bahjad           4            0
Jazira Lab               1            1
M Hersi                  2            2
Dr Rami                  2            4
Dr Maan                 17           43
Out site                 4            1
ER                      10           46
Dr shacban               4           14
>>> 
>>> fh.iloc[0:, 0:]
                      No/P Biochemistry Hormone hematology serology Urine Stool Coag Semen Swab culture
DOCTOR                                                                                                 
Dr wasem                21           21      32         28       29    15     0    0     0    0       0
Dr gayath               13           89       8         20        9     9     9    0     0    0       0
Dr Heytham               0            0       0          0        0     0     0    0     0    0       0
Dr maalin                8           19       0         12        2     1     8    0     0    0       0
ER                      12           47       4         17       18     5     5    3     0    0       0
Dr khaled               15           73       0         18       10     3     6    0     0    0       0
Dr Diini                 1            4       0          0        0     0     0    0     0    0       0
Dr Ahmed Mohamed         6           21       0          9        4     0     0    3     0    0       0
Dr mohamed Farah Jama    3            9       1          3        0     0     0    0     0    0       0
Dr Amir jabir            3            3       0          1        8     0     0    0     0    0       0
Dr Nabil Safiah          5            0       0          3        7     0     0    0     0    0       0
Dr RAniBahjad            3            2       0          4        5     1     1    0     0    0       0
Dr Rani bahjad           4            0       0          7       12     2     0    0     0    0       0
Jazira Lab               1            1       0          0        0     0     0    0     0    0       0
M Hersi                  2            2       1          4        0     0     0    0     0    0       1
Dr Rami                  2            4       0          3        4     0     3    3     0    0       0
Dr Maan                 17           43      23         10        8    11     2    3     3    0       3
Out site                 4            1       0          2        8     0     0    0     0    0       0
ER                      10           46       2         17        9     2     8    3     0    0       0
Dr shacban               4           14       0          8        5     1     0    0     0    0       0
>>> fh.iloc[1:, 0:]
                      No/P Biochemistry Hormone hematology serology Urine Stool Coag Semen Swab culture
DOCTOR                                                                                                 
Dr gayath               13           89       8         20        9     9     9    0     0    0       0
Dr Heytham               0            0       0          0        0     0     0    0     0    0       0
Dr maalin                8           19       0         12        2     1     8    0     0    0       0
ER                      12           47       4         17       18     5     5    3     0    0       0
Dr khaled               15           73       0         18       10     3     6    0     0    0       0
Dr Diini                 1            4       0          0        0     0     0    0     0    0       0
Dr Ahmed Mohamed         6           21       0          9        4     0     0    3     0    0       0
Dr mohamed Farah Jama    3            9       1          3        0     0     0    0     0    0       0
Dr Amir jabir            3            3       0          1        8     0     0    0     0    0       0
Dr Nabil Safiah          5            0       0          3        7     0     0    0     0    0       0
Dr RAniBahjad            3            2       0          4        5     1     1    0     0    0       0
Dr Rani bahjad           4            0       0          7       12     2     0    0     0    0       0
Jazira Lab               1            1       0          0        0     0     0    0     0    0       0
M Hersi                  2            2       1          4        0     0     0    0     0    0       1
Dr Rami                  2            4       0          3        4     0     3    3     0    0       0
Dr Maan                 17           43      23         10        8    11     2    3     3    0       3
Out site                 4            1       0          2        8     0     0    0     0    0       0
ER                      10           46       2         17        9     2     8    3     0    0       0
Dr shacban               4           14       0          8        5     1     0    0     0    0       0
>>> fh.iloc[0:, 1:]
                      Biochemistry Hormone hematology serology Urine Stool Coag Semen Swab culture
DOCTOR                                                                                            
Dr wasem                        21      32         28       29    15     0    0     0    0       0
Dr gayath                       89       8         20        9     9     9    0     0    0       0
Dr Heytham                       0       0          0        0     0     0    0     0    0       0
Dr maalin                       19       0         12        2     1     8    0     0    0       0
ER                              47       4         17       18     5     5    3     0    0       0
Dr khaled                       73       0         18       10     3     6    0     0    0       0
Dr Diini                         4       0          0        0     0     0    0     0    0       0
Dr Ahmed Mohamed                21       0          9        4     0     0    3     0    0       0
Dr mohamed Farah Jama            9       1          3        0     0     0    0     0    0       0
Dr Amir jabir                    3       0          1        8     0     0    0     0    0       0
Dr Nabil Safiah                  0       0          3        7     0     0    0     0    0       0
Dr RAniBahjad                    2       0          4        5     1     1    0     0    0       0
Dr Rani bahjad                   0       0          7       12     2     0    0     0    0       0
Jazira Lab                       1       0          0        0     0     0    0     0    0       0
M Hersi                          2       1          4        0     0     0    0     0    0       1
Dr Rami                          4       0          3        4     0     3    3     0    0       0
Dr Maan                         43      23         10        8    11     2    3     3    0       3
Out site                         1       0          2        8     0     0    0     0    0       0
ER                              46       2         17        9     2     8    3     0    0       0
Dr shacban                      14       0          8        5     1     0    0     0    0       0
>>> fh.iloc[0, 1:]
Biochemistry    21
Hormone         32
hematology      28
serology        29
Urine           15
Stool            0
Coag             0
Semen            0
Swab             0
culture          0
Name: Dr wasem, dtype: object
>>> fh
                      No/P Biochemistry Hormone hematology serology Urine Stool Coag Semen Swab culture
DOCTOR                                                                                                 
Dr wasem                21           21      32         28       29    15     0    0     0    0       0
Dr gayath               13           89       8         20        9     9     9    0     0    0       0
Dr Heytham               0            0       0          0        0     0     0    0     0    0       0
Dr maalin                8           19       0         12        2     1     8    0     0    0       0
ER                      12           47       4         17       18     5     5    3     0    0       0
Dr khaled               15           73       0         18       10     3     6    0     0    0       0
Dr Diini                 1            4       0          0        0     0     0    0     0    0       0
Dr Ahmed Mohamed         6           21       0          9        4     0     0    3     0    0       0
Dr mohamed Farah Jama    3            9       1          3        0     0     0    0     0    0       0
Dr Amir jabir            3            3       0          1        8     0     0    0     0    0       0
Dr Nabil Safiah          5            0       0          3        7     0     0    0     0    0       0
Dr RAniBahjad            3            2       0          4        5     1     1    0     0    0       0
Dr Rani bahjad           4            0       0          7       12     2     0    0     0    0       0
Jazira Lab               1            1       0          0        0     0     0    0     0    0       0
M Hersi                  2            2       1          4        0     0     0    0     0    0       1
Dr Rami                  2            4       0          3        4     0     3    3     0    0       0
Dr Maan                 17           43      23         10        8    11     2    3     3    0       3
Out site                 4            1       0          2        8     0     0    0     0    0       0
ER                      10           46       2         17        9     2     8    3     0    0       0
Dr shacban               4           14       0          8        5     1     0    0     0    0       0
>>> [i for i in fh.iloc[0, 1:]]
[21, 32, 28, 29, 15, 0, 0, 0, 0, 0]
>>> 
========================================================== RESTART: C:/Users/user/Desktop/powerpointcharts.py =========================================================
                      No/P Biochemistry Hormone hematology serology Urine Stool Coag Semen Swab culture
DOCTOR                                                                                                 
Dr wasem                21           21      32         28       29    15     0    0     0    0       0
Dr gayath               13           89       8         20        9     9     9    0     0    0       0
Dr Heytham               0            0       0          0        0     0     0    0     0    0       0
Dr maalin                8           19       0         12        2     1     8    0     0    0       0
ER                      12           47       4         17       18     5     5    3     0    0       0
Dr khaled               15           73       0         18       10     3     6    0     0    0       0
Dr Diini                 1            4       0          0        0     0     0    0     0    0       0
Dr Ghannam               0            0       0          0        0     0     0    0     0    0       0
Dr Ahmed Mohamed         6           21       0          9        4     0     0    3     0    0       0
Dr mohamed Farah Jama    3            9       1          3        0     0     0    0     0    0       0
Dr Rabie                 0            0       0          0        0     0     0    0     0    0       0
Dr Amir jabir            3            3       0          1        8     0     0    0     0    0       0
Dr Nabil Safiah          5            0       0          3        7     0     0    0     0    0       0
Dr RAniBahjad            3            2       0          4        5     1     1    0     0    0       0
Dr Rani bahjad           4            0       0          7       12     2     0    0     0    0       0
Jazira Lab               1            1       0          0        0     0     0    0     0    0       0
M Hersi                  2            2       1          4        0     0     0    0     0    0       1
Dr Rami                  2            4       0          3        4     0     3    3     0    0       0
Dr Maan                 17           43      23         10        8    11     2    3     3    0       3
Out site                 4            1       0          2        8     0     0    0     0    0       0
ER                      10           46       2         17        9     2     8    3     0    0       0
Dr shacban               4           14       0          8        5     1     0    0     0    0       0
Traceback (most recent call last):
  File "C:\Users\user\Anaconda3\lib\site-packages\pandas\core\indexes\base.py", line 2646, in get_loc
    return self._engine.get_loc(key)
  File "pandas\_libs\index.pyx", line 111, in pandas._libs.index.IndexEngine.get_loc
  File "pandas\_libs\index.pyx", line 138, in pandas._libs.index.IndexEngine.get_loc
  File "pandas\_libs\hashtable_class_helper.pxi", line 1618, in pandas._libs.hashtable.PyObjectHashTable.get_item
  File "pandas\_libs\hashtable_class_helper.pxi", line 1626, in pandas._libs.hashtable.PyObjectHashTable.get_item
KeyError: 'Dr wasem'

During handling of the above exception, another exception occurred:

Traceback (most recent call last):
  File "C:/Users/user/Desktop/powerpointcharts.py", line 157, in <module>
    presentation(fh)
  File "C:/Users/user/Desktop/powerpointcharts.py", line 99, in presentation
    chart.chart_title.text_frame.text= 'Total Patients {}'.format(fh1[i][0])
  File "C:\Users\user\Anaconda3\lib\site-packages\pandas\core\frame.py", line 2800, in __getitem__
    indexer = self.columns.get_loc(key)
  File "C:\Users\user\Anaconda3\lib\site-packages\pandas\core\indexes\base.py", line 2648, in get_loc
    return self._engine.get_loc(self._maybe_cast_indexer(key))
  File "pandas\_libs\index.pyx", line 111, in pandas._libs.index.IndexEngine.get_loc
  File "pandas\_libs\index.pyx", line 138, in pandas._libs.index.IndexEngine.get_loc
  File "pandas\_libs\hashtable_class_helper.pxi", line 1618, in pandas._libs.hashtable.PyObjectHashTable.get_item
  File "pandas\_libs\hashtable_class_helper.pxi", line 1626, in pandas._libs.hashtable.PyObjectHashTable.get_item
KeyError: 'Dr wasem'
>>> 
========================================================== RESTART: C:/Users/user/Desktop/powerpointcharts.py =========================================================
                      No/P Biochemistry Hormone hematology serology Urine Stool Coag Semen Swab culture
DOCTOR                                                                                                 
Dr wasem                21           21      32         28       29    15     0    0     0    0       0
Dr gayath               13           89       8         20        9     9     9    0     0    0       0
Dr Heytham               0            0       0          0        0     0     0    0     0    0       0
Dr maalin                8           19       0         12        2     1     8    0     0    0       0
ER                      12           47       4         17       18     5     5    3     0    0       0
Dr khaled               15           73       0         18       10     3     6    0     0    0       0
Dr Diini                 1            4       0          0        0     0     0    0     0    0       0
Dr Ghannam               0            0       0          0        0     0     0    0     0    0       0
Dr Ahmed Mohamed         6           21       0          9        4     0     0    3     0    0       0
Dr mohamed Farah Jama    3            9       1          3        0     0     0    0     0    0       0
Dr Rabie                 0            0       0          0        0     0     0    0     0    0       0
Dr Amir jabir            3            3       0          1        8     0     0    0     0    0       0
Dr Nabil Safiah          5            0       0          3        7     0     0    0     0    0       0
Dr RAniBahjad            3            2       0          4        5     1     1    0     0    0       0
Dr Rani bahjad           4            0       0          7       12     2     0    0     0    0       0
Jazira Lab               1            1       0          0        0     0     0    0     0    0       0
M Hersi                  2            2       1          4        0     0     0    0     0    0       1
Dr Rami                  2            4       0          3        4     0     3    3     0    0       0
Dr Maan                 17           43      23         10        8    11     2    3     3    0       3
Out site                 4            1       0          2        8     0     0    0     0    0       0
ER                      10           46       2         17        9     2     8    3     0    0       0
Dr shacban               4           14       0          8        5     1     0    0     0    0       0
Traceback (most recent call last):
  File "C:\Users\user\Anaconda3\lib\site-packages\pandas\core\indexing.py", line 702, in _has_valid_tuple
    self._validate_key(k, i)
  File "C:\Users\user\Anaconda3\lib\site-packages\pandas\core\indexing.py", line 2010, in _validate_key
    raise ValueError(f"Can only index by location with a [{self._valid_types}]")
ValueError: Can only index by location with a [integer, integer slice (START point is INCLUDED, END point is EXCLUDED), listlike of integers, boolean array]

During handling of the above exception, another exception occurred:

Traceback (most recent call last):
  File "C:/Users/user/Desktop/powerpointcharts.py", line 157, in <module>
    presentation(fh)
  File "C:/Users/user/Desktop/powerpointcharts.py", line 84, in presentation
    chart_data.add_series('Series 1', (k for k in fh.iloc[i, 1:]))
  File "C:\Users\user\Anaconda3\lib\site-packages\pandas\core\indexing.py", line 1761, in __getitem__
    return self._getitem_tuple(key)
  File "C:\Users\user\Anaconda3\lib\site-packages\pandas\core\indexing.py", line 2066, in _getitem_tuple
    self._has_valid_tuple(tup)
  File "C:\Users\user\Anaconda3\lib\site-packages\pandas\core\indexing.py", line 705, in _has_valid_tuple
    "Location based indexing can only have "
ValueError: Location based indexing can only have [integer, integer slice (START point is INCLUDED, END point is EXCLUDED), listlike of integers, boolean array] types
>>> fh.iloc[i, 1:]
Traceback (most recent call last):
  File "<pyshell#44>", line 1, in <module>
    fh.iloc[i, 1:]
NameError: name 'i' is not defined
>>> fh.iloc[2, 1:]
Biochemistry    0
Hormone         0
hematology      0
serology        0
Urine           0
Stool           0
Coag            0
Semen           0
Swab            0
culture         0
Name: Dr Heytham, dtype: object
>>> 
========================================================== RESTART: C:/Users/user/Desktop/powerpointcharts.py =========================================================
                      No/P Biochemistry Hormone hematology serology Urine Stool Coag Semen Swab culture
DOCTOR                                                                                                 
Dr wasem                21           21      32         28       29    15     0    0     0    0       0
Dr gayath               13           89       8         20        9     9     9    0     0    0       0
Dr Heytham               0            0       0          0        0     0     0    0     0    0       0
Dr maalin                8           19       0         12        2     1     8    0     0    0       0
ER                      12           47       4         17       18     5     5    3     0    0       0
Dr khaled               15           73       0         18       10     3     6    0     0    0       0
Dr Diini                 1            4       0          0        0     0     0    0     0    0       0
Dr Ghannam               0            0       0          0        0     0     0    0     0    0       0
Dr Ahmed Mohamed         6           21       0          9        4     0     0    3     0    0       0
Dr mohamed Farah Jama    3            9       1          3        0     0     0    0     0    0       0
Dr Rabie                 0            0       0          0        0     0     0    0     0    0       0
Dr Amir jabir            3            3       0          1        8     0     0    0     0    0       0
Dr Nabil Safiah          5            0       0          3        7     0     0    0     0    0       0
Dr RAniBahjad            3            2       0          4        5     1     1    0     0    0       0
Dr Rani bahjad           4            0       0          7       12     2     0    0     0    0       0
Jazira Lab               1            1       0          0        0     0     0    0     0    0       0
M Hersi                  2            2       1          4        0     0     0    0     0    0       1
Dr Rami                  2            4       0          3        4     0     3    3     0    0       0
Dr Maan                 17           43      23         10        8    11     2    3     3    0       3
Out site                 4            1       0          2        8     0     0    0     0    0       0
ER                      10           46       2         17        9     2     8    3     0    0       0
Dr shacban               4           14       0          8        5     1     0    0     0    0       0
Traceback (most recent call last):
  File "C:\Users\user\Anaconda3\lib\site-packages\pandas\core\indexes\base.py", line 2646, in get_loc
    return self._engine.get_loc(key)
  File "pandas\_libs\index.pyx", line 111, in pandas._libs.index.IndexEngine.get_loc
  File "pandas\_libs\index.pyx", line 138, in pandas._libs.index.IndexEngine.get_loc
  File "pandas\_libs\hashtable_class_helper.pxi", line 1618, in pandas._libs.hashtable.PyObjectHashTable.get_item
  File "pandas\_libs\hashtable_class_helper.pxi", line 1626, in pandas._libs.hashtable.PyObjectHashTable.get_item
KeyError: 0

During handling of the above exception, another exception occurred:

Traceback (most recent call last):
  File "C:/Users/user/Desktop/powerpointcharts.py", line 157, in <module>
    presentation(fh)
  File "C:/Users/user/Desktop/powerpointcharts.py", line 99, in presentation
    chart.chart_title.text_frame.text= 'Total Patients {}'.format(fh1[i][0])
  File "C:\Users\user\Anaconda3\lib\site-packages\pandas\core\frame.py", line 2800, in __getitem__
    indexer = self.columns.get_loc(key)
  File "C:\Users\user\Anaconda3\lib\site-packages\pandas\core\indexes\base.py", line 2648, in get_loc
    return self._engine.get_loc(self._maybe_cast_indexer(key))
  File "pandas\_libs\index.pyx", line 111, in pandas._libs.index.IndexEngine.get_loc
  File "pandas\_libs\index.pyx", line 138, in pandas._libs.index.IndexEngine.get_loc
  File "pandas\_libs\hashtable_class_helper.pxi", line 1618, in pandas._libs.hashtable.PyObjectHashTable.get_item
  File "pandas\_libs\hashtable_class_helper.pxi", line 1626, in pandas._libs.hashtable.PyObjectHashTable.get_item
KeyError: 0
>>> [l for l in fh.columns[1:]]
['Biochemistry', 'Hormone', 'hematology', 'serology', 'Urine', 'Stool', 'Coag', 'Semen', 'Swab', 'culture']
>>> fh.iloc[1, 2]
8
>>> fh.iloc[1, 2:]
Hormone        8
hematology    20
serology       9
Urine          9
Stool          9
Coag           0
Semen          0
Swab           0
culture        0
Name: Dr gayath, dtype: object
>>> fh.iloc[1:, 2]
DOCTOR
Dr gayath                 8
Dr Heytham                0
Dr maalin                 0
ER                        4
Dr khaled                 0
Dr Diini                  0
Dr Ahmed Mohamed          0
Dr mohamed Farah Jama     1
Dr Amir jabir             0
Dr Nabil Safiah           0
Dr RAniBahjad             0
Dr Rani bahjad            0
Jazira Lab                0
M Hersi                   1
Dr Rami                   0
Dr Maan                  23
Out site                  0
ER                        2
Dr shacban                0
Name: Hormone, dtype: object
>>> fh.iloc[1:, 0]
DOCTOR
Dr gayath                13
Dr Heytham                0
Dr maalin                 8
ER                       12
Dr khaled                15
Dr Diini                  1
Dr Ahmed Mohamed          6
Dr mohamed Farah Jama     3
Dr Amir jabir             3
Dr Nabil Safiah           5
Dr RAniBahjad             3
Dr Rani bahjad            4
Jazira Lab                1
M Hersi                   2
Dr Rami                   2
Dr Maan                  17
Out site                  4
ER                       10
Dr shacban                4
Name: No/P, dtype: object
>>> fh.iloc[0:, 0]
DOCTOR
Dr wasem                 21
Dr gayath                13
Dr Heytham                0
Dr maalin                 8
ER                       12
Dr khaled                15
Dr Diini                  1
Dr Ahmed Mohamed          6
Dr mohamed Farah Jama     3
Dr Amir jabir             3
Dr Nabil Safiah           5
Dr RAniBahjad             3
Dr Rani bahjad            4
Jazira Lab                1
M Hersi                   2
Dr Rami                   2
Dr Maan                  17
Out site                  4
ER                       10
Dr shacban                4
Name: No/P, dtype: object
>>> fh[0][0]
Traceback (most recent call last):
  File "C:\Users\user\Anaconda3\lib\site-packages\pandas\core\indexes\base.py", line 2646, in get_loc
    return self._engine.get_loc(key)
  File "pandas\_libs\index.pyx", line 111, in pandas._libs.index.IndexEngine.get_loc
  File "pandas\_libs\index.pyx", line 138, in pandas._libs.index.IndexEngine.get_loc
  File "pandas\_libs\hashtable_class_helper.pxi", line 1618, in pandas._libs.hashtable.PyObjectHashTable.get_item
  File "pandas\_libs\hashtable_class_helper.pxi", line 1626, in pandas._libs.hashtable.PyObjectHashTable.get_item
KeyError: 0

During handling of the above exception, another exception occurred:

Traceback (most recent call last):
  File "<pyshell#52>", line 1, in <module>
    fh[0][0]
  File "C:\Users\user\Anaconda3\lib\site-packages\pandas\core\frame.py", line 2800, in __getitem__
    indexer = self.columns.get_loc(key)
  File "C:\Users\user\Anaconda3\lib\site-packages\pandas\core\indexes\base.py", line 2648, in get_loc
    return self._engine.get_loc(self._maybe_cast_indexer(key))
  File "pandas\_libs\index.pyx", line 111, in pandas._libs.index.IndexEngine.get_loc
  File "pandas\_libs\index.pyx", line 138, in pandas._libs.index.IndexEngine.get_loc
  File "pandas\_libs\hashtable_class_helper.pxi", line 1618, in pandas._libs.hashtable.PyObjectHashTable.get_item
  File "pandas\_libs\hashtable_class_helper.pxi", line 1626, in pandas._libs.hashtable.PyObjectHashTable.get_item
KeyError: 0
>>> fh.index
Index(['Dr wasem', 'Dr gayath', 'Dr Heytham', 'Dr maalin', 'ER', 'Dr khaled',
       'Dr Diini', 'Dr Ahmed Mohamed', 'Dr mohamed Farah Jama',
       'Dr Amir jabir', 'Dr Nabil Safiah', 'Dr RAniBahjad', 'Dr Rani bahjad',
       'Jazira Lab', 'M Hersi', 'Dr Rami', 'Dr Maan', 'Out site', 'ER',
       'Dr shacban'],
      dtype='object', name='DOCTOR')
>>> fh[0]
Traceback (most recent call last):
  File "C:\Users\user\Anaconda3\lib\site-packages\pandas\core\indexes\base.py", line 2646, in get_loc
    return self._engine.get_loc(key)
  File "pandas\_libs\index.pyx", line 111, in pandas._libs.index.IndexEngine.get_loc
  File "pandas\_libs\index.pyx", line 138, in pandas._libs.index.IndexEngine.get_loc
  File "pandas\_libs\hashtable_class_helper.pxi", line 1618, in pandas._libs.hashtable.PyObjectHashTable.get_item
  File "pandas\_libs\hashtable_class_helper.pxi", line 1626, in pandas._libs.hashtable.PyObjectHashTable.get_item
KeyError: 0

During handling of the above exception, another exception occurred:

Traceback (most recent call last):
  File "<pyshell#54>", line 1, in <module>
    fh[0]
  File "C:\Users\user\Anaconda3\lib\site-packages\pandas\core\frame.py", line 2800, in __getitem__
    indexer = self.columns.get_loc(key)
  File "C:\Users\user\Anaconda3\lib\site-packages\pandas\core\indexes\base.py", line 2648, in get_loc
    return self._engine.get_loc(self._maybe_cast_indexer(key))
  File "pandas\_libs\index.pyx", line 111, in pandas._libs.index.IndexEngine.get_loc
  File "pandas\_libs\index.pyx", line 138, in pandas._libs.index.IndexEngine.get_loc
  File "pandas\_libs\hashtable_class_helper.pxi", line 1618, in pandas._libs.hashtable.PyObjectHashTable.get_item
  File "pandas\_libs\hashtable_class_helper.pxi", line 1626, in pandas._libs.hashtable.PyObjectHashTable.get_item
KeyError: 0
>>> fh.columns
Index(['No/P', 'Biochemistry', 'Hormone', 'hematology', 'serology', 'Urine',
       'Stool', 'Coag', 'Semen', 'Swab', 'culture'],
      dtype='object')
>>> fh['No/P']
DOCTOR
Dr wasem                 21
Dr gayath                13
Dr Heytham                0
Dr maalin                 8
ER                       12
Dr khaled                15
Dr Diini                  1
Dr Ahmed Mohamed          6
Dr mohamed Farah Jama     3
Dr Amir jabir             3
Dr Nabil Safiah           5
Dr RAniBahjad             3
Dr Rani bahjad            4
Jazira Lab                1
M Hersi                   2
Dr Rami                   2
Dr Maan                  17
Out site                  4
ER                       10
Dr shacban                4
Name: No/P, dtype: object
>>> fh['No/P'][0]
21
>>> 
========================================================== RESTART: C:/Users/user/Desktop/powerpointcharts.py =========================================================
                      No/P Biochemistry Hormone hematology serology Urine Stool Coag Semen Swab culture
DOCTOR                                                                                                 
Dr wasem                21           21      32         28       29    15     0    0     0    0       0
Dr gayath               13           89       8         20        9     9     9    0     0    0       0
Dr Heytham               0            0       0          0        0     0     0    0     0    0       0
Dr maalin                8           19       0         12        2     1     8    0     0    0       0
ER                      12           47       4         17       18     5     5    3     0    0       0
Dr khaled               15           73       0         18       10     3     6    0     0    0       0
Dr Diini                 1            4       0          0        0     0     0    0     0    0       0
Dr Ghannam               0            0       0          0        0     0     0    0     0    0       0
Dr Ahmed Mohamed         6           21       0          9        4     0     0    3     0    0       0
Dr mohamed Farah Jama    3            9       1          3        0     0     0    0     0    0       0
Dr Rabie                 0            0       0          0        0     0     0    0     0    0       0
Dr Amir jabir            3            3       0          1        8     0     0    0     0    0       0
Dr Nabil Safiah          5            0       0          3        7     0     0    0     0    0       0
Dr RAniBahjad            3            2       0          4        5     1     1    0     0    0       0
Dr Rani bahjad           4            0       0          7       12     2     0    0     0    0       0
Jazira Lab               1            1       0          0        0     0     0    0     0    0       0
M Hersi                  2            2       1          4        0     0     0    0     0    0       1
Dr Rami                  2            4       0          3        4     0     3    3     0    0       0
Dr Maan                 17           43      23         10        8    11     2    3     3    0       3
Out site                 4            1       0          2        8     0     0    0     0    0       0
ER                      10           46       2         17        9     2     8    3     0    0       0
Dr shacban               4           14       0          8        5     1     0    0     0    0       0
>>> fh.index[0]
'Dr wasem'
>>> 
========================================================== RESTART: C:/Users/user/Desktop/powerpointcharts.py =========================================================
                      No/P Biochemistry Hormone hematology serology Urine Stool Coag Semen Swab culture
DOCTOR                                                                                                 
Dr wasem                21           21      32         28       29    15     0    0     0    0       0
Dr gayath               13           89       8         20        9     9     9    0     0    0       0
Dr Heytham               0            0       0          0        0     0     0    0     0    0       0
Dr maalin                8           19       0         12        2     1     8    0     0    0       0
ER                      12           47       4         17       18     5     5    3     0    0       0
Dr khaled               15           73       0         18       10     3     6    0     0    0       0
Dr Diini                 1            4       0          0        0     0     0    0     0    0       0
Dr Ghannam               0            0       0          0        0     0     0    0     0    0       0
Dr Ahmed Mohamed         6           21       0          9        4     0     0    3     0    0       0
Dr mohamed Farah Jama    3            9       1          3        0     0     0    0     0    0       0
Dr Rabie                 0            0       0          0        0     0     0    0     0    0       0
Dr Amir jabir            3            3       0          1        8     0     0    0     0    0       0
Dr Nabil Safiah          5            0       0          3        7     0     0    0     0    0       0
Dr RAniBahjad            3            2       0          4        5     1     1    0     0    0       0
Dr Rani bahjad           4            0       0          7       12     2     0    0     0    0       0
Jazira Lab               1            1       0          0        0     0     0    0     0    0       0
M Hersi                  2            2       1          4        0     0     0    0     0    0       1
Dr Rami                  2            4       0          3        4     0     3    3     0    0       0
Dr Maan                 17           43      23         10        8    11     2    3     3    0       3
Out site                 4            1       0          2        8     0     0    0     0    0       0
ER                      10           46       2         17        9     2     8    3     0    0       0
Dr shacban               4           14       0          8        5     1     0    0     0    0       0
>>> 
========================================================== RESTART: C:/Users/user/Desktop/powerpointcharts.py =========================================================
                      No/P Biochemistry Hormone hematology serology Urine Stool Coag Semen Swab culture
DOCTOR                                                                                                 
Dr wasem                21           21      32         28       29    15     0    0     0    0       0
Dr gayath               13           89       8         20        9     9     9    0     0    0       0
Dr Heytham               0            0       0          0        0     0     0    0     0    0       0
Dr maalin                8           19       0         12        2     1     8    0     0    0       0
Dr khaled               15           73       0         18       10     3     6    0     0    0       0
Dr Diini                 1            4       0          0        0     0     0    0     0    0       0
Dr Ghannam               0            0       0          0        0     0     0    0     0    0       0
Dr Ahmed Mohamed         6           21       0          9        4     0     0    3     0    0       0
Dr mohamed Farah Jama    3            9       1          3        0     0     0    0     0    0       0
Dr Rabie                 0            0       0          0        0     0     0    0     0    0       0
Dr Amir jabir            3            3       0          1        8     0     0    0     0    0       0
Dr Nabil Safiah          5            0       0          3        7     0     0    0     0    0       0
Dr RAniBahjad            3            2       0          4        5     1     1    0     0    0       0
Dr Rani bahjad           4            0       0          7       12     2     0    0     0    0       0
Jazira Lab               1            1       0          0        0     0     0    0     0    0       0
M Hersi                  2            2       1          4        0     0     0    0     0    0       1
Dr Rami                  2            4       0          3        4     0     3    3     0    0       0
Dr Maan                 17           43      23         10        8    11     2    3     3    0       3
Out site                 4            1       0          2        8     0     0    0     0    0       0
Dr shacban               4           14       0          8        5     1     0    0     0    0       0
ER                      22           93       6         34       27     7    13    6     0    0       0
>>> 
========================================= RESTART: C:\Users\user\Documents\Practice\Data Science\powerpoint charts-general.py =========================================
                       No/P  Biochemistry  Hormone  hematology  Urine  Stool  Coag  Semen  Swab  culture
DOCTOR                                                                                                  
Dr Abdikadir Ali          0             0        0           0      0      0     0      0     0        0
Dr Ahmed Mohamed        144           610       16         198     10      0    12      0     2        0
Dr Amir jabir             3             3        0           1      0      0     0      0     0        0
Dr Diini                  9            48        6           8      2      1     1      0     0        0
Dr Ghannam               63           121       12          70      2      0    42      2     0        0
Dr Heytham                2             0        0           2      1      0     0      1     0        0
Dr Maan                  17            43       23          10     11      2     3      3     0        3
Dr Mohamed Farah Jama    20            34       12          28      2      6     0      0     0        0
Dr Nabil Safiah           5             0        0           3      0      0     0      0     0        0
Dr Nabil safiah          48            35        8          32      0      0    28      0     0        0
Dr RAniBahjad             3             2        0           4      1      1     0      0     0        0
Dr Rabie                 13            43        0          14      0      4     0      0     0        0
Dr Rami                  23            94        0          42      0      3    39      0     0        0
Dr Rani bahjad           34             4        0          59      9      0     6      0     0        0
Dr abdel nasser           1             0        0           0      0      1     0      0     0        0
Dr amir Jabir            40             0        0          15      4      0     0      0     0        0
Dr gayath               398          2241      209         687    270    167    18      0     0        4
Dr khaled               291          1188       33         295     57     91    18      0     0        0
Dr maalin               310           646       14         430     37    120   104      0     1       21
Dr maan                 248           567      373         106    129      4    57     83     0        7
Dr mohamed Farah Jama     3             9        1           3      0      0     0      0     0        0
Dr shacban               81           347        8         141      6      2     7      0     0        1
Dr wasem                584           555      491         839    388      6     9      0     0        1
DrM Hersi                25            40       16          32      5     14     0      0     0        1
ER                      312          1367      147         386     87    158    46      0     0        0
Jazira Hosopital         23            17        9           1      0      0     0      0     0        0
Jazira Lab                1             1        0           0      0      0     0      0     0        0
M Hersi                   2             2        1           4      0      0     0      0     0        1
Out site                  4             1        0           2      0      0     0      0     0        0
Outsite                 185            62       23          76     19      1     6      0     0        0
>>> 
========================================= RESTART: C:\Users\user\Documents\Practice\Data Science\powerpoint charts-general.py =========================================
                       No/P  Biochemistry  Hormone  hematology  Urine  Stool  Coag  Semen  Swab  culture
DOCTOR                                                                                                  
Dr Abdikadir Ali          0             0        0           0      0      0     0      0     0        0
Dr Ahmed Mohamed        144           610       16         198     10      0    12      0     2        0
Dr Amir jabir             3             3        0           1      0      0     0      0     0        0
Dr Diini                  9            48        6           8      2      1     1      0     0        0
Dr Ghannam               63           121       12          70      2      0    42      2     0        0
Dr Heytham                2             0        0           2      1      0     0      1     0        0
Dr Maan                  17            43       23          10     11      2     3      3     0        3
Dr Mohamed Farah Jama    20            34       12          28      2      6     0      0     0        0
Dr Nabil Safiah           5             0        0           3      0      0     0      0     0        0
Dr Nabil safiah          48            35        8          32      0      0    28      0     0        0
Dr RAniBahjad             3             2        0           4      1      1     0      0     0        0
Dr Rabie                 13            43        0          14      0      4     0      0     0        0
Dr Rami                  23            94        0          42      0      3    39      0     0        0
Dr Rani bahjad           34             4        0          59      9      0     6      0     0        0
Dr abdel nasser           1             0        0           0      0      1     0      0     0        0
Dr amir Jabir            40             0        0          15      4      0     0      0     0        0
Dr gayath               398          2241      209         687    270    167    18      0     0        4
Dr khaled               291          1188       33         295     57     91    18      0     0        0
Dr maalin               310           646       14         430     37    120   104      0     1       21
Dr maan                 248           567      373         106    129      4    57     83     0        7
Dr mohamed Farah Jama     3             9        1           3      0      0     0      0     0        0
Dr shacban               81           347        8         141      6      2     7      0     0        1
Dr wasem                584           555      491         839    388      6     9      0     0        1
DrM Hersi                25            40       16          32      5     14     0      0     0        1
ER                      312          1367      147         386     87    158    46      0     0        0
Jazira Hosopital         23            17        9           1      0      0     0      0     0        0
Jazira Lab                1             1        0           0      0      0     0      0     0        0
M Hersi                   2             2        1           4      0      0     0      0     0        1
Out site                  4             1        0           2      0      0     0      0     0        0
Outsite                 185            62       23          76     19      1     6      0     0        0
>>> 
===================================== RESTART: C:\Users\user\Documents\Practice\General Programing\chromeexte\clipboard\reading.py ====================================
2020, Nov , 1, 11, 195, 4016 

>>> 
===================================== RESTART: C:\Users\user\Documents\Practice\General Programing\chromeexte\clipboard\reading.py ====================================
2020, Nov , 1, 11, 25, 441 

>>> 
===================================== RESTART: C:\Users\user\Documents\Practice\General Programing\chromeexte\clipboard\reading.py ====================================
2020, Nov , 1, 11, 37, 673 

>>> 
========================================================== RESTART: C:/Users/user/Desktop/powerpointcharts.py =========================================================
                      No/P Biochemistry Hormone hematology serology Urine Stool Coag Semen Swab culture
DOCTOR                                                                                                 
Dr wasem                21           21      32         28       29    15     0    0     0    0       0
Dr gayath               13           89       8         20        9     9     9    0     0    0       0
Dr Heytham               0            0       0          0        0     0     0    0     0    0       0
Dr maalin                8           19       0         12        2     1     8    0     0    0       0
Dr khaled               15           73       0         18       10     3     6    0     0    0       0
Dr Diini                 1            4       0          0        0     0     0    0     0    0       0
Dr Ghannam               0            0       0          0        0     0     0    0     0    0       0
Dr Ahmed Mohamed         6           21       0          9        4     0     0    3     0    0       0
Dr mohamed Farah Jama    3            9       1          3        0     0     0    0     0    0       0
Dr Rabie                 0            0       0          0        0     0     0    0     0    0       0
Dr Amir jabir            3            3       0          1        8     0     0    0     0    0       0
Dr Nabil Safiah          5            0       0          3        7     0     0    0     0    0       0
Dr RAniBahjad            3            2       0          4        5     1     1    0     0    0       0
Dr Rani bahjad           4            0       0          7       12     2     0    0     0    0       0
Jazira Lab               1            1       0          0        0     0     0    0     0    0       0
M Hersi                  2            2       1          4        0     0     0    0     0    0       1
Dr Rami                  2            4       0          3        4     0     3    3     0    0       0
Dr Maan                 17           43      23         10        8    11     2    3     3    0       3
Out site                 4            1       0          2        8     0     0    0     0    0       0
Dr shacban               4           14       0          8        5     1     0    0     0    0       0
ER                      22           93       6         34       27     7    13    6     0    0       0
>>> fh.shape
(19, 11)
>>> fh.iloc[3, 2: fh.shape[1]]
Hormone        0
hematology    12
serology       2
Urine          1
Stool          8
Coag           0
Semen          0
Swab           0
culture        0
Name: Dr maalin, dtype: object
>>> fh.iloc[3:fh.shape[1], -1]
DOCTOR
Dr maalin                0
Dr khaled                0
Dr Diini                 0
Dr Ahmed Mohamed         0
Dr mohamed Farah Jama    0
Dr Amir jabir            0
Dr Nabil Safiah          0
Dr RAniBahjad            0
Name: culture, dtype: object
>>> 
===================================== RESTART: C:\Users\user\Documents\Practice\General Programing\chromeexte\clipboard\reading.py ====================================
2020, Nov , 1, 11, 50, 845 

>>> 
===================================== RESTART: C:\Users\user\Documents\Practice\General Programing\chromeexte\clipboard\reading.py ====================================
2020, Nov , 1, 11, 50, 845 

>>> 
===================================== RESTART: C:\Users\user\Documents\Practice\General Programing\chromeexte\clipboard\reading.py ====================================
2020, Nov , 1, 11, 42, 667 

>>> 
===================================== RESTART: C:\Users\user\Documents\Practice\General Programing\chromeexte\clipboard\reading.py ====================================
2020, Nov , 1, 11, 42, 667 

>>> 
========================================================== RESTART: C:/Users/user/Desktop/powerpointcharts.py =========================================================
                      No/P Biochemistry Hormone hematology serology Urine Stool Coag Semen Swab culture
DOCTOR                                                                                                 
Dr wasem                21           21      32         28       29    15     0    0     0    0       0
Dr gayath               13           89       8         20        9     9     9    0     0    0       0
Dr Heytham               0            0       0          0        0     0     0    0     0    0       0
Dr maalin                8           19       0         12        2     1     8    0     0    0       0
Dr khaled               15           73       0         18       10     3     6    0     0    0       0
Dr Diini                 1            4       0          0        0     0     0    0     0    0       0
Dr Ghannam               0            0       0          0        0     0     0    0     0    0       0
Dr Ahmed Mohamed         6           21       0          9        4     0     0    3     0    0       0
Dr mohamed Farah Jama    3            9       1          3        0     0     0    0     0    0       0
Dr Rabie                 0            0       0          0        0     0     0    0     0    0       0
Dr Amir jabir            3            3       0          1        8     0     0    0     0    0       0
Dr Nabil Safiah          5            0       0          3        7     0     0    0     0    0       0
Dr RAniBahjad            3            2       0          4        5     1     1    0     0    0       0
Dr Rani bahjad           4            0       0          7       12     2     0    0     0    0       0
Jazira Lab               1            1       0          0        0     0     0    0     0    0       0
M Hersi                  2            2       1          4        0     0     0    0     0    0       1
Dr Rami                  2            4       0          3        4     0     3    3     0    0       0
Dr Maan                 17           43      23         10        8    11     2    3     3    0       3
Out site                 4            1       0          2        8     0     0    0     0    0       0
Dr shacban               4           14       0          8        5     1     0    0     0    0       0
ER                      22           93       6         34       27     7    13    6     0    0       0
>>> fh.shape
(19, 11)
>>> fh.loc['Dr wasem']
No/P            21
Biochemistry    21
Hormone         32
hematology      28
serology        29
Urine           15
Stool            0
Coag             0
Semen            0
Swab             0
culture          0
Name: Dr wasem, dtype: object
>>> fh.loc[['Dr Wasem'], ['Serology']]
Traceback (most recent call last):
  File "<pyshell#64>", line 1, in <module>
    fh.loc[['Dr Wasem'], ['Serology']]
  File "C:\Users\user\Anaconda3\lib\site-packages\pandas\core\indexing.py", line 1761, in __getitem__
    return self._getitem_tuple(key)
  File "C:\Users\user\Anaconda3\lib\site-packages\pandas\core\indexing.py", line 1280, in _getitem_tuple
    return self._multi_take(tup)
  File "C:\Users\user\Anaconda3\lib\site-packages\pandas\core\indexing.py", line 1339, in _multi_take
    for (key, axis) in zip(tup, o._AXIS_ORDERS)
  File "C:\Users\user\Anaconda3\lib\site-packages\pandas\core\indexing.py", line 1339, in <dictcomp>
    for (key, axis) in zip(tup, o._AXIS_ORDERS)
  File "C:\Users\user\Anaconda3\lib\site-packages\pandas\core\indexing.py", line 1552, in _get_listlike_indexer
    keyarr, indexer, o._get_axis_number(axis), raise_missing=raise_missing
  File "C:\Users\user\Anaconda3\lib\site-packages\pandas\core\indexing.py", line 1639, in _validate_read_indexer
    raise KeyError(f"None of [{key}] are in the [{axis_name}]")
KeyError: "None of [Index(['Dr Wasem'], dtype='object', name='DOCTOR')] are in the [index]"
>>> fh.loc[['Dr Wasem'], ['serology', ]]
Traceback (most recent call last):
  File "<pyshell#65>", line 1, in <module>
    fh.loc[['Dr Wasem'], ['serology', ]]
  File "C:\Users\user\Anaconda3\lib\site-packages\pandas\core\indexing.py", line 1761, in __getitem__
    return self._getitem_tuple(key)
  File "C:\Users\user\Anaconda3\lib\site-packages\pandas\core\indexing.py", line 1280, in _getitem_tuple
    return self._multi_take(tup)
  File "C:\Users\user\Anaconda3\lib\site-packages\pandas\core\indexing.py", line 1339, in _multi_take
    for (key, axis) in zip(tup, o._AXIS_ORDERS)
  File "C:\Users\user\Anaconda3\lib\site-packages\pandas\core\indexing.py", line 1339, in <dictcomp>
    for (key, axis) in zip(tup, o._AXIS_ORDERS)
  File "C:\Users\user\Anaconda3\lib\site-packages\pandas\core\indexing.py", line 1552, in _get_listlike_indexer
    keyarr, indexer, o._get_axis_number(axis), raise_missing=raise_missing
  File "C:\Users\user\Anaconda3\lib\site-packages\pandas\core\indexing.py", line 1639, in _validate_read_indexer
    raise KeyError(f"None of [{key}] are in the [{axis_name}]")
KeyError: "None of [Index(['Dr Wasem'], dtype='object', name='DOCTOR')] are in the [index]"
>>> h.loc[['Dr Wasem'], ['serology']]
Traceback (most recent call last):
  File "<pyshell#66>", line 1, in <module>
    h.loc[['Dr Wasem'], ['serology']]
NameError: name 'h' is not defined
>>> fh.loc[['Dr Wasem'], ['serology']]
Traceback (most recent call last):
  File "<pyshell#67>", line 1, in <module>
    fh.loc[['Dr Wasem'], ['serology']]
  File "C:\Users\user\Anaconda3\lib\site-packages\pandas\core\indexing.py", line 1761, in __getitem__
    return self._getitem_tuple(key)
  File "C:\Users\user\Anaconda3\lib\site-packages\pandas\core\indexing.py", line 1280, in _getitem_tuple
    return self._multi_take(tup)
  File "C:\Users\user\Anaconda3\lib\site-packages\pandas\core\indexing.py", line 1339, in _multi_take
    for (key, axis) in zip(tup, o._AXIS_ORDERS)
  File "C:\Users\user\Anaconda3\lib\site-packages\pandas\core\indexing.py", line 1339, in <dictcomp>
    for (key, axis) in zip(tup, o._AXIS_ORDERS)
  File "C:\Users\user\Anaconda3\lib\site-packages\pandas\core\indexing.py", line 1552, in _get_listlike_indexer
    keyarr, indexer, o._get_axis_number(axis), raise_missing=raise_missing
  File "C:\Users\user\Anaconda3\lib\site-packages\pandas\core\indexing.py", line 1639, in _validate_read_indexer
    raise KeyError(f"None of [{key}] are in the [{axis_name}]")
KeyError: "None of [Index(['Dr Wasem'], dtype='object', name='DOCTOR')] are in the [index]"
>>> fh.loc[['Dr Wasem']]
Traceback (most recent call last):
  File "<pyshell#68>", line 1, in <module>
    fh.loc[['Dr Wasem']]
  File "C:\Users\user\Anaconda3\lib\site-packages\pandas\core\indexing.py", line 1767, in __getitem__
    return self._getitem_axis(maybe_callable, axis=axis)
  File "C:\Users\user\Anaconda3\lib\site-packages\pandas\core\indexing.py", line 1953, in _getitem_axis
    return self._getitem_iterable(key, axis=axis)
  File "C:\Users\user\Anaconda3\lib\site-packages\pandas\core\indexing.py", line 1594, in _getitem_iterable
    keyarr, indexer = self._get_listlike_indexer(key, axis, raise_missing=False)
  File "C:\Users\user\Anaconda3\lib\site-packages\pandas\core\indexing.py", line 1552, in _get_listlike_indexer
    keyarr, indexer, o._get_axis_number(axis), raise_missing=raise_missing
  File "C:\Users\user\Anaconda3\lib\site-packages\pandas\core\indexing.py", line 1639, in _validate_read_indexer
    raise KeyError(f"None of [{key}] are in the [{axis_name}]")
KeyError: "None of [Index(['Dr Wasem'], dtype='object', name='DOCTOR')] are in the [index]"
>>> fh.loc['Dr Wasem']
Traceback (most recent call last):
  File "C:\Users\user\Anaconda3\lib\site-packages\pandas\core\indexes\base.py", line 2646, in get_loc
    return self._engine.get_loc(key)
  File "pandas\_libs\index.pyx", line 111, in pandas._libs.index.IndexEngine.get_loc
  File "pandas\_libs\index.pyx", line 138, in pandas._libs.index.IndexEngine.get_loc
  File "pandas\_libs\hashtable_class_helper.pxi", line 1618, in pandas._libs.hashtable.PyObjectHashTable.get_item
  File "pandas\_libs\hashtable_class_helper.pxi", line 1626, in pandas._libs.hashtable.PyObjectHashTable.get_item
KeyError: 'Dr Wasem'

During handling of the above exception, another exception occurred:

Traceback (most recent call last):
  File "<pyshell#69>", line 1, in <module>
    fh.loc['Dr Wasem']
  File "C:\Users\user\Anaconda3\lib\site-packages\pandas\core\indexing.py", line 1767, in __getitem__
    return self._getitem_axis(maybe_callable, axis=axis)
  File "C:\Users\user\Anaconda3\lib\site-packages\pandas\core\indexing.py", line 1964, in _getitem_axis
    return self._get_label(key, axis=axis)
  File "C:\Users\user\Anaconda3\lib\site-packages\pandas\core\indexing.py", line 624, in _get_label
    return self.obj._xs(label, axis=axis)
  File "C:\Users\user\Anaconda3\lib\site-packages\pandas\core\generic.py", line 3537, in xs
    loc = self.index.get_loc(key)
  File "C:\Users\user\Anaconda3\lib\site-packages\pandas\core\indexes\base.py", line 2648, in get_loc
    return self._engine.get_loc(self._maybe_cast_indexer(key))
  File "pandas\_libs\index.pyx", line 111, in pandas._libs.index.IndexEngine.get_loc
  File "pandas\_libs\index.pyx", line 138, in pandas._libs.index.IndexEngine.get_loc
  File "pandas\_libs\hashtable_class_helper.pxi", line 1618, in pandas._libs.hashtable.PyObjectHashTable.get_item
  File "pandas\_libs\hashtable_class_helper.pxi", line 1626, in pandas._libs.hashtable.PyObjectHashTable.get_item
KeyError: 'Dr Wasem'
>>> fh.loc['Dr wasem']
No/P            21
Biochemistry    21
Hormone         32
hematology      28
serology        29
Urine           15
Stool            0
Coag             0
Semen            0
Swab             0
culture          0
Name: Dr wasem, dtype: object
>>> fh.loc[['Dr wasem'], ['serology']]
         serology
DOCTOR           
Dr wasem       29
>>> 
===================================== RESTART: C:\Users\user\Documents\Practice\General Programing\chromeexte\clipboard\reading.py ====================================
2020, Nov , 1, 12, 22, 401 

>>> fh.loc[['Dr wasem'], ['serology', 'Hormone']]
Traceback (most recent call last):
  File "<pyshell#72>", line 1, in <module>
    fh.loc[['Dr wasem'], ['serology', 'Hormone']]
NameError: name 'fh' is not defined
>>> 
========================================================== RESTART: C:/Users/user/Desktop/powerpointcharts.py =========================================================
                      No/P Biochemistry Hormone hematology serology Urine Stool Coag Semen Swab culture
DOCTOR                                                                                                 
Dr wasem                21           21      32         28       29    15     0    0     0    0       0
Dr gayath               13           89       8         20        9     9     9    0     0    0       0
Dr Heytham               0            0       0          0        0     0     0    0     0    0       0
Dr maalin                8           19       0         12        2     1     8    0     0    0       0
Dr khaled               15           73       0         18       10     3     6    0     0    0       0
Dr Diini                 1            4       0          0        0     0     0    0     0    0       0
Dr Ghannam               0            0       0          0        0     0     0    0     0    0       0
Dr Ahmed Mohamed         6           21       0          9        4     0     0    3     0    0       0
Dr mohamed Farah Jama    3            9       1          3        0     0     0    0     0    0       0
Dr Rabie                 0            0       0          0        0     0     0    0     0    0       0
Dr Amir jabir            3            3       0          1        8     0     0    0     0    0       0
Dr Nabil Safiah          5            0       0          3        7     0     0    0     0    0       0
Dr RAniBahjad            3            2       0          4        5     1     1    0     0    0       0
Dr Rani bahjad           4            0       0          7       12     2     0    0     0    0       0
Jazira Lab               1            1       0          0        0     0     0    0     0    0       0
M Hersi                  2            2       1          4        0     0     0    0     0    0       1
Dr Rami                  2            4       0          3        4     0     3    3     0    0       0
Dr Maan                 17           43      23         10        8    11     2    3     3    0       3
Out site                 4            1       0          2        8     0     0    0     0    0       0
Dr shacban               4           14       0          8        5     1     0    0     0    0       0
ER                      22           93       6         34       27     7    13    6     0    0       0
>>> fh.loc[['Dr wasem'], ['serology', 'Hormone']]
         serology Hormone
DOCTOR                   
Dr wasem       29      32
>>> fh.loc[['Dr wasem'], ['serology', 'Hormone', 'Urine']]
         serology Hormone Urine
DOCTOR                         
Dr wasem       29      32    15
>>> 