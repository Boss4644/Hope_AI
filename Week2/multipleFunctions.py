class multipleFunctions:
    def Subfields():
        lists1 = ['Machine Learning', 'Neural Network', 'Vision', 'Robotics', 'Speech Processiong', 'Nature Language Processing']
        print("Sub-Fields in AI are: " )
        for temp in lists1:
            print(temp)

    def OddorEven():
        i = int(input("Enter a number"))
        if((i%2) == 0):
            print("The given number is even")
        else:
            print("The given number is odd")

    def percentage():
        s1 = int(input("subject1: "))
        s2 = int(input("subject2: "))
        s3 = int(input("subject3: "))
        s4 = int(input("subject4: "))
        s5 = int(input("subject5: "))
        total = s1 + s2 + s3 + s4 + s5
        per = float(total/5)
        print("Total: ", total)
        print("Percentage: ", per)

    def triangle():
        height = int(input("Height: "))
        breadth = int(input("Breadth: "))
        print("Area formula: (height*breadth)/2")
        area = (height*breadth)/2
        print("Area of triangle: ", area)
        height1 = int(input("height1: "))
        height2 = int(input("height2: "))
        breadth = int(input("breadth: "))
        print("primeter formula: height1+height2+breadth")
        perimeter = height1 + height2 + breadth
        print("perimeter of triangle: ", perimeter)

    def BMI():
        weight=int(input("Enter Weight"))
        height=int(input("Enter Height in CM"))
        heightInMtr = float(height/100)
        bmi= weight/float(heightInMtr*heightInMtr)
        print("Your BMI", bmi)
        if bmi<18.5:
            print("Underweight")
        elif bmi>=18.5 and bmi<25:
            print("Normal")
        elif bmi>=25 and bmi<30:
            print("Overweight")
        else:
            print("Very Over Weight")