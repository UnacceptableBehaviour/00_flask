#! /usr/bin/env python

# load a csv file into a list of dictionaries

from pprint import pprint # giza a look

def get_nutridata():
             #  0          1              2             3             4    5    6    7    8    9     10   11   12   13   14   15   16    17 
    header = 'rcp_id,image_filename,recipe_title,txt_ingredient_file,n_En,n_Fa,n_Fs,n_Fm,n_Fp,n_Fo3,n_Ca,n_Su,n_Fb,n_St,n_Pr,n_Sa,n_Al,serving_size'
    text = '1,20190306_145901_seabass kale and potato dinner.jpg,seabass kale and potato dinner,20190306_145901_seabass kale and potato dinner.txt,55,1.6,0.44,0.5,0.43,0.4,2.74,0.32,0.47,0.0,7.28,0.45,0.0,450.0'
    
    header_list = header.split(',') 
    rcp_list = text.split(',')

    info = {}
    
    for i in range( len(header_list) ):        
        info[ header_list[i] ] = rcp_list[i]
        #print(f"{ header_list[i] } = { info[ header_list[i] ] }")
    
    return info


def get_nutrients_per_serving():
    info = get_nutridata()
    
    nutrient_keys = 'n_En,n_Fa,n_Fs,n_Fm,n_Fp,n_Fo3,n_Ca,n_Su,n_Fb,n_St,n_Pr,n_Sa,n_Al'.split(',')
    
    multiplier = float( info['serving_size'] ) / 100.0
    
    b4 = 0
    
    for key in nutrient_keys:
        b4 = info[key]
        info[key] = round( ( float( info[key] ) * multiplier ), 1 )
        print(f"key:{key} - b4:{b4} - x:{multiplier} - conv:{info[key]}- conv:{info[key].__class__.__name__}")

    return info


def main():
    info = get_nutridata()
 
    #pprint(info)
 
    for k,v in info.items():        
        print(f"{ k } = { v }")
        
    print(f"__name__ is: {__name__}")
    print(f"__file__ is: {__file__}")
    print(f"__loader__ is: {__loader__}")
    print(f"__package__ is: {__package__}")
        
    info['n_EnkJ'] = str( round( float( info['n_En'] ) * 4.184 ) )
    info['serving_size'] = str( round( float( info['serving_size'] ) ) )
    
    print(f"n_EnkJ:       {info['n_EnkJ']}")
    print(f"serving_size: {info['serving_size']}")
    
    print(f"{1}")
    
    get_nutrients_per_serving()
    

if __name__ == '__main__':
    main()                      # call main if this is being executed directly 
