def caculate_bmi (height, weight):
    print ("Height = " + str(height))
    print ("Weight = " + str(weight))

    bmi = weight/(height*height)

    print ("The bmi is = " + str(bmi))

    if bmi < 18.5:
        print ("Under Weight")
    if 18.5 <= bmi <= 25.0:
        print ("Normal Weight")
    if bmi > 25.0:
        print ("Over Weight")

caculate_bmi(weight=57 , height =1.73)