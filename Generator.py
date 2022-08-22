

class password_manage:
    import random
    password=""
    def __init__(self, length):
        self.length=length

    #defualt value for length of password is 8
    

    list_lowCase=[chr(i) for i in range(97,97+26)]
    list_uppCase=[chr(i) for i in range(65, 65+26)]
    list_special=[ "@", "#", "$", "&", "_","!", "." ]
    list_numbers=[str(i) for i in range(10)]

    big_ele_all=list_lowCase + list_uppCase + list_special + list_numbers
    random.shuffle(big_ele_all)
    def generate(self):
        import random
        for i in range(self.length):
            self.password+=random.choice(self.big_ele_all)

        return self.password
       





if __name__ == "__main__":
    I=True

    while I:
        length=int(input("Enter Length of password:"))
        if length>=8:
        
            obj=password_manage(length)
            password=obj.generate()
            print(f"Output: {password}")
            I=False

        else:
            print("Length should be greater than or equals to 8!")

    
    
    
                  
