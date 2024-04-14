import os 
from os import path
import socket ,time
from colorama import Fore,init

init(convert=True)


files_name_in_html = ''
uploads_folder = os.getcwd() + '\\Uploads'
for item in os.listdir(uploads_folder):
    files_name_in_html += f'<td><a href="{item}"> {path.basename(item)}</a></td> \n'



header = '''<!DOCTYPE html>
<html lang="en">
<head>
  <meta charset="UTF-8">
  <meta name="viewport" content="width=device-width, initial-scale=1.0">
  <title>Home Server</title>
  <link rel="stylesheet" href="{{ url_for('static', filename='style.css') }}">
</head>'''


to_write = f'''
{header}
<body>
  <table>
    <tr>
      <th>Songs</th>
    </tr>
    <tr id="files">
      {files_name_in_html}
    </tr>

  </table>

</body>
</html>

'''



dest_file = os.getcwd() + '\\templates\\index.html'
with open(dest_file,'w',encoding='utf-8') as html:
        
    html.write(to_write)
    time.sleep(.5)

    print(Fore.YELLOW + 'Writing To HTML File...' + Fore.RESET)
    time.sleep(.5)
    print(Fore.GREEN + 'All Set :)' + Fore.RESET)
