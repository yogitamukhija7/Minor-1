import cv2
import numpy as np

def load_image(letter):
    path = r"dataset\\" + letter + ".png"
    template = cv2.imread(path,0)
    return template

def func1():
    print("This is how its gonna work")
    print("all 26 letters will be displayed on screen ")
    img_rgb = cv2.imread("dataset//image001.png")
    print("Enter a letter which you want program to recognize")
    ch = raw_input("Enter charcter")
    img_gray = cv2.cvtColor(img_rgb, cv2.COLOR_BGR2GRAY)
    
    template = load_image(ch)
    w, h = template.shape[::-1]
    res = cv2.matchTemplate(img_gray,template,cv2.TM_CCOEFF_NORMED)
    print res
    threshold = float(raw_input("Enter Threshold value for comparision. for eg: if you want 80% matching enter 0.8"))
    loc = np.where( res >= threshold)
    print loc
    for pt in zip(*loc[::-1]):
        cv2.rectangle(img_rgb, pt, (pt[0] + w, pt[1] + h), (0,255,255), 2)
    cv2.imshow('Detected',img_rgb)
    cv2.waitKey(0)
    cv2.destroyAllWindows()

def func3(ch,main_image):
    img_rgb = cv2.imread(main_image)
    img_gray = cv2.cvtColor(img_rgb, cv2.COLOR_BGR2GRAY)
    path = "dataset\\" + ch + ".png"
    template = cv2.imread(path,0)
    res = cv2.matchTemplate(img_gray,template,cv2.TM_CCOEFF_NORMED)
    threshold = 0.8
    loc = np.where( res >= threshold)
    #cv2.destroyAllWindows()
    try:
        cords = zip(*loc[::-1])[0][0]
    except:
        cords = -1
    return cords
def func2():
    db = {}
    db2 = []
    for i in range(97,123):
        ch = chr(i)
        cords = func3(ch,"dataset\\test-1.png")
        #print cords
        #print "abc"
        if(cords > 0):
            db2.append(cords)
            db[str(cords)] = ch
            #print str(cords)
            #print "..."
    #db2.sort()
    #print db2
    string = ""
    for i in db2:
        string += db[str(i)]
    print(string)
def main():
    answer = True
    while(answer):
        print ("Available Options : \n")
        print ("1 - test single letter")
        print ("2 - test complete string(Beta version)")
        print ("3 - Exit")
        print ("Enter Your choice")
        ans = int(raw_input())
        if(ans == 1):
            func1()
        if(ans == 2):
            func2()
        if(ans == 3):
            answer = False

main()
