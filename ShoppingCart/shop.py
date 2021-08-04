products = []
def accept():
    ele = input("Enter the product to add into cart or q to quit\n")
    if len(ele) != 1 and ele != 'q':
        products.append(ele)
        accept()
    else:
        print(products)
        quit()

accept()