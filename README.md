# Dirdata
Dirdata is a lightweight and efficient simple database inside windows system using directory method to find data that can store up to (10^33) decillion JSON data.

Dirdata is a simple database for windows users, for storing json in json files in the directory you choose.
it can support up to (10^33) one Decillion JSON data.

I compare it with mysql, this is the result :

important: i am using lenovo x250 core i5 5 generation 8 gb Ram,
and using pycharm for collecting this data  .

>>>taking data out of Dirdata :

-> Dirdata minimum :
The data : {'hello world!': {'debug': 'on', 'window': {'title': 'Sample Konfabulator Widget', 'name': 'main_window', 'width': 500, 'height': 500}, 'image': {'src': 'Images/Sun.png', 'name': 'sun1', 'hOffset': 250, 'vOffset': 250, 'alignment': 'center'}, 'text': {'data': 'Click Here', 'size': 36, 'style': 'bold', 'name': 'text1', 'hOffset': 250, 'vOffset': 100, 'alignment': 'center', 'onMouseUp': 'sun1.opacity = (sun1.opacity / 100) * 90;'}}}

Memory (Before): [13.234375] MB
Time it took: 0.0004976999999999898 Seconds
Memory (After): [13.24] MB

-> Dirdata maximum:
The data : {'hello world!': {'debug': 'on', 'window': {'title': 'Sample Konfabulator Widget', 'name': 'main_window', 'width': 500, 'height': 500}, 'image': {'src': 'Images/Sun.png', 'name': 'sun1', 'hOffset': 250, 'vOffset': 250, 'alignment': 'center'}, 'text': {'data': 'Click Here', 'size': 36, 'style': 'bold', 'name': 'text1', 'hOffset': 250, 'vOffset': 100, 'alignment': 'center', 'onMouseUp': 'sun1.opacity = (sun1.opacity / 100) * 90;'}}}

Memory (Before): [13.203125] MB
Time it took: 0.0041317 Seconds
Memory (After): [13.21875] MB

>>>taking data out of mysql :
[(134932, 'Isaac', '11', 56)]

Memory (Before): [14.2109375] MB
Time: 0.004913400000000012 Seconds
Memory (After): [14.60546875] MB

The cool thing about Dirdata is the numbers in (Dirdata minimum, Dirdata maximum) will still be the same even if you are looking through a trillions of json.

I just started learning programming four months ago and i thought it would be fun to make something like this, and share it with the community.
How to use:
_inserting data in database:

x_json = {"hello world!": {
         "something": "on",
         "window": {
            "name": "main_window",
            "width": 500,
            "height": 500
         }}}
example: C:\\Users\\User\\Desktop\\New folder --> Change this directory into the folder in your computer
that you want the data to be placed.
data = Dirdata.Generate('C:\\Users\\User\\Desktop\\New folder', x_json)
>> data.insert() --> Calling this method will insert the data x_json in the database and it will return the data id 
>> print(data.insert()) --> will insert the data in database and print its id

_finding & deleting:

data = Dirdata.Find('C:\\Users\\User\\Desktop\\New folder', '1:1:1:1:1:1:1:1:1:1:666')
 '1:1:1:1:1:1:1:1:1:1:666' --> is the data unique id.
>> data.loads --> Calling this method will give you the json as a dictionary (same as json.loads(data)).
>> data.string(2, True) --> Calling this method will give you the json as string.
   (2, True) ---> (indent=2, sort_keys=True) in the json.dumps method
   the default value is (indent=2, sort_keys=False).
>> data.delete() --> Calling this method will delete the json that has the id '1:1:1:1:1:1:1:1:1:1:666'

give me your thoughts guys.
