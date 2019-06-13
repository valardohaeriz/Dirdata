# Dirdata
Dirdata is a lightweight and efficient database inside windows system using directory method to find data that can store up to (10^33) decillion JSON data.
Dir Data is a simple database for windows users, to store json in json files in the directory you choose.
it can support up to (10^33) Decillion JSON data.
i compare it with mysql, and this is what i got.

important: i am using lenovo x250 core i5 5 generation 8 gb Ram,
and using pycharm for collecting this data  .

>>>Dirdata:

-> Dirdata minimum:
The data : {'hello world!': {'debug': 'on', 'window': {'title': 'Sample Konfabulator Widget', 'name': 'main_window', 'width': 500, 'height': 500}, 'image': {'src': 'Images/Sun.png', 'name': 'sun1', 'hOffset': 250, 'vOffset': 250, 'alignment': 'center'}, 'text': {'data': 'Click Here', 'size': 36, 'style': 'bold', 'name': 'text1', 'hOffset': 250, 'vOffset': 100, 'alignment': 'center', 'onMouseUp': 'sun1.opacity = (sun1.opacity / 100) * 90;'}}}

Memory (Before): [13.234375] MB
Time it took: 0.0004976999999999898 Seconds
Memory (After): [13.24] MB

-> Dirdata maximum:
The data : {'hello world!': {'debug': 'on', 'window': {'title': 'Sample Konfabulator Widget', 'name': 'main_window', 'width': 500, 'height': 500}, 'image': {'src': 'Images/Sun.png', 'name': 'sun1', 'hOffset': 250, 'vOffset': 250, 'alignment': 'center'}, 'text': {'data': 'Click Here', 'size': 36, 'style': 'bold', 'name': 'text1', 'hOffset': 250, 'vOffset': 100, 'alignment': 'center', 'onMouseUp': 'sun1.opacity = (sun1.opacity / 100) * 90;'}}}

Memory (Before): [13.203125] MB
Time it took: 0.0041317 Seconds
Memory (After): [13.21875] MB

>>>mysql :
[(134932, 'Isaac', '11', 56)]

Memory (Before): [14.2109375] MB
Time: 0.004913400000000012 Seconds
Memory (After): [14.60546875] MB

the cool thing about Dirdata is the numbers in(Dirdata minimum, Dirdata maximum) will still be the same even if you are looking through a trillions of json.

i just started learning programming four months ago and i thought it would be fun to make something like this, and share it with you.
give me your thoughts guys.
