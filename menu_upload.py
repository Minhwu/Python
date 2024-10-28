# This script is transfer the content from the word or excel to the sheet in html format.
# Upload it to the cmssite.jsedu.sh.cn
# Athor: Minhui     2024/10/15

import re
import sys
import pandas as pd
from docx import Document 


# def word_to_html(file_path):  
#     try:  
#         doc = Document(file_path)
#         html_content = "<html><body>"
#         in_list =  False  

#         for para in doc.paragraphs:  
#             if 'ListBullet' in para.style.name or 'ListNumber' in para.style.name:
#                 if not in_list:
#                     html_content += "<ul>" if 'ListBullet' in para.style.name else "<ol>"
#                     in_list = True
#                 html_content += f"<li>{para.text}</li>"
#             else:
#                 if in_list:
#                     html_content += "</ul>"
          
#         return html_content
      
#     except Exception as e:  
#         print(f"Read file failed: {e}", file=sys.stderr)  
#         return None


def read_excel_file(file_path):
    try:
        df = pd.read_excel(file_path)

        menu_dict = {}

        for day in df.columns:
            menu_dict[day] = df[day].dropna().tolist()

        return menu_dict

    except Exception as e:  
        print(f"Read file failed: {e}", file=sys.stderr)  
        return None



def date_to_html(data):
    html_header = '''<p style="text-align: center;">
    <br/>
    </p>
<table border="0" cellpadding="0" cellspacing="0" width="-153">
    <colgroup>
        <col width="102" style=";width:103px"/>
        <col width="113" style=";width:113px"/>
        <col width="175" style=";width:175px"/>
        <col width="124" style=";width:124px"/>
        <col width="147" style=";width:147px"/>
        <col width="132" style=";width:132px"/>
    </colgroup>
    <tbody>
        <tr height="27" style="height:27px" class="firstRow">
            <td height="27" style="border-width: 1px; border-style: solid; border-color: rgb(187, 187, 187);">
                {first_day_content}
            </td>
        '''

    remaining_days_html = ''
    is_first_day = True

    for day in data.keys():
        if is_first_day:
            f_html = html_header.replace('{first_day_content}', day)
            is_first_day = False
        else:
            remaining_day_format = f'''    <td style="border-left: none; border-right: 1px solid rgb(187, 187, 187); border-top: 1px solid rgb(187, 187, 187); border-bottom: 1px solid rgb(187, 187, 187);">
                {day}
            </td>
        '''
            remaining_days_html += remaining_day_format
    
    if remaining_days_html:
        return f_html + remaining_days_html + "</tr>"
    else:
        return f_html + "</tr>"


def foods_to_html(date, data):
    html_format = date + '\n        <tr height="114" style="height:114px">'
    food_html = '''            <td height="114" style="border-top: none; border-left: 1px solid rgb(187, 187, 187); border-right: 1px solid rgb(187, 187, 187); border-bottom: 1px solid rgb(187, 187, 187);">
    {food}<br/> &nbsp; &nbsp; 重量：（{weight}）
</td>'''

    foods_html = ''
    for foods in data.values():
        for food in foods:
            print(food)






if len(sys.argv) != 2:  
    print("Usage: main.py <file path>", file=sys.stderr)  
    sys.exit(1)  
  
file_path = sys.argv[1]

word_file = r'.*\.(doc|docx)'
excel_file = r'.*\.xls' 

document_content = None

# Check the file format
if re.search(word_file, file_path, re.IGNORECASE):
    document_content = word_to_html(file_path)

elif re.search(excel_file, file_path, re.IGNORECASE):
    print("Found excel file")
    document_content = read_excel_file(file_path)

else:
    print("Incorrect file format") 



date = date_to_html(document_content)

foods_to_html(date, document_content)

# Read the file
# if document_content is not None:  
#     for paragraph in document_content:  
#         print(paragraph)  
# else:  
#     print("Can not read the file", file=sys.stderr)
