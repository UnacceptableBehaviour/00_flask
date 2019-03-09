#! /usr/bin/env python

# load a csv file into a list of dictionaries

from pprint import pprint # giza a look

def get_nutridata():
             #  0          1              2             3             4    5    6    7    8    9
    header = 'rcp_id,image_filename,recipe_title,txt_ingredient_file,n_En,n_Fa,n_Ca,n_Su,n_Pr,n_Sa'
    text = '1,20190306_145901_seabass kale and potato dinner.jpg,seabass kale and potato dinner,20190306_145901_seabass kale and potato dinner.txt,55,1.6,2.74,0.32,7.28,0.45'    
    
    header_list = header.split(',') 
    rcp_list = text.split(',')

    info = {}
    
    for i in range(0,10):        
        info[ header_list[i] ] = rcp_list[i]
        #print(f"{ header_list[i] } = { info[ header_list[i] ] }")
    
    return info


def main():
    info = get_nutridata()
 
    #pprint(info)
 
    for k,v in info.items():        
        print(f"{ k } = { v }")

if __name__ == '__main__':
    main()
