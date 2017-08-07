



def dictIngredients ():
        start = '''Ready to write a recipe?? Impress your parents?? Then follow the steps to make recipe!
        '''
        print (start)
        dict = {'pineapple': '1/2 cup', 'apple': '1 cup', 'milk': '1/2 cup'}
        for ingredient in dict:
            print (ingredient,":",dict[ingredient])

def listDirections ():
    list = ['pour', 'grate', 'mix']
    for line in list:
        print (line)
dictIngredients ()
listDirections ()
