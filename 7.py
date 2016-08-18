def get_data(path):
    data_list=[]
    with open(path) as f:
        for line in f:
            data_list.append(line.strip())
    return data_list

def extract_data(data_list):
    new_list=[]
    in_quot=False
    word=""
    for line in data_list:
        temp_list=[]
        for c in line:
            if c in('"',"'") and in_quot==False:
                in_quot=True
                continue
            elif c in('"',"'") and in_quot:
                in_quot=False
                continue
            elif c==',' and in_quot:
                pass
            elif c==',' and in_quot==False:
                temp_list.append(word.title())
                word=""
                continue
            word+=c
        if word:
            temp_list.append(word.title())
            word=""
            new_list.append(temp_list)
    return new_list

def write_data(path,data_list):
    html_text=""
    html_text += '<table border="1">\n'
    index=0
    color_choice=['white','lightyellow']
    for line in data_list:
        if index==0:
            html_text += '<tr bgcolor="lightgreen">\n'
        else:
            html_text += '<tr bgcolor="{}">\n'.format(color_choice[index%2])
        html_text += ("<td>{}</td>\n"
                 "<td align='right'>{}</td>\n"
                 "<td align='right'>{}</td>\n"
                 "<td align='right'>{}</td>\n"
                 "<td align='right'>{}</td></tr>\n").format(*line)
        index += 1
    with open(path,'w') as f:
        f.write(html_text)
    
def main(in_file,out_file):
    data_list=extract_data(get_data(in_file))
    write_data(out_file,data_list)
    
main('data.csv','file.html')  
    
