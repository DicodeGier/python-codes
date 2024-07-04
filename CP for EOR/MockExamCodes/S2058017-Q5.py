def countProduct(filename,prod_name):    
    fh=open("Q5.txt", 'r')                    
    content=fh.read()                      
    fh.close                                
    return content.count(prod_name.lower())      
    