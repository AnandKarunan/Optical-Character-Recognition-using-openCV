import pytesseract
import cv2

pytesseract.pytesseract.tesseract_cmd = 'C:\\Program Files\\Tesseract-OCR\\tesseract.exe'
#Path of the Tesseract-OCR


'''Function to remove unwanted characters'''
def remove_char(arr):
    final= []
    for i in range(len(arr)):
        if arr[i][0]!='' and arr[i][0]!=' ' and arr[i][0] != '.' and arr[i][0] != '‘' and arr[i][0]!= '(' and arr[i][0]!=')' and arr[i][0]!=',' and arr[i][0]!='-' and arr[i][0]!='?' and arr[i][0]!='~' and arr[i][0]!=':' and arr[i][0]!='"':
            final.append(arr[i])
    return final

'''Detect lines using this function'''
def detect_lines(img):
    arr_lines = []
    himg,wimg,_ = img.shape
    # configuration = r'--oem 3--psm 6 outputbase digits'
    #Use the commented code if only digits are to be detected or cropped. Also add a second arguement to the next code as config=configuration
    contour = pytesseract.image_to_string(img)
    for lines in contour.splitlines():
        lines = lines.split('/n')
        arr_lines.append(lines)
    arr_lines = remove_char(arr_lines)
    return arr_lines

'''Function used to save the output'''
#Takes arguments file-to-be-saved-on,data-to-be-saved and flag to determine whether it is a string or not
def save_file(file,final_array,flag):
    save_lines = open(file, "w")
    if flag==1:
        save_lines.write(final_array)
    else :
        save_lines.write("\n".join(i for i in final_array))
    save_lines.close()

if __name__ == '__main__':
    '''Input image'''
    img = cv2.imread('in1.png', cv2.COLOR_RGB2GRAY)

    '''Add required mask if necessary'''
    # gray = img.copy()
    # ret, gray = cv2.threshold(gray, 200, 255, cv2.THRESH_BINARY_INV)

    '''Detecting and Obtaining lines'''
    arr_lines = detect_lines(img)
    final_lines = ''
    for i in range(len(arr_lines)):
        final_lines += str(arr_lines[i][0]) + "\n"
    final_lines = final_lines.replace("‘","")
    save_file("lines.txt",final_lines,1)

    '''Obtaining Words'''
    words_final =[]
    a = final_lines.split("\n")
    '''Remove the unwanted characters as follows'''
    for i in range(len(a)):
        b = a[i].replace('.',"")
        b = b.replace(',',"")
        b = b.replace('?', "")
        b = b.replace(':', "")
        b = b.replace('-', "")
        b = b.replace(')', "")
        b = b.replace('(', "")
        b = b.replace('“', "")
        b = b.replace('”', "")
        b = b.replace(';', "")
        b = b.replace('!', "")
        b = b.replace('~', "")
        c = b.split(" ")
        for j in range(len(c)):
            words_final.append(c[j])
    save_file("words.txt",words_final,0)

    '''Obtaining Letters'''
    letter_final = []
    for i in range(len(words_final)):
        for j in words_final[i]:
            letter_final.append(j)
    while "'" in letter_final:
        letter_final.remove("'")
    save_file("letters.txt",letter_final,0)

'''To Display the input image'''
cv2.imshow("in1",img)
cv2.waitKey(0)

'''//////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////'''
'''///////////////////////////////////////////////////////////////////          ALTERNATE METHOD           //////////////////////////////////////////////////////////////////'''
'''//////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////'''

'''For this funtions, a separate main codes are to be structured accordingly'''

'''
#Independantly crop the words using the function below
def crop_the_words(img):
    arr_words = []
    himg,wimg,_ = img.shape
    # configuration = r'--oem 3--psm 6 outputbase digits'
    #Use the commented code if only digits are to be detected or cropped. Also add a second arguement to the next code as config=configuration
    contour = pytesseract.image_to_data(img)
    for i,word in enumerate(contour.splitlines()):
        if i>0:
            word = word.split()
            if len(word)==12:
                x, y, w, h = int(word[6]), int(word[7]), int(word[8]), int(word[9])
                cv2.rectangle(img, (x, y), (x+w, y+h), (0, 255, 0), 1)
                cv2.putText(img,word[11],(x,y),cv2.FONT_HERSHEY_SIMPLEX,0.3,(0,0,0),1)
                arr_words.append(word[11])
    return arr_words


#Independantly crop the letters using the function below
def crop_the_letters(img):
    arr_letters = []
    himg,wimg,_ = img.shape
    # configuration = r'--oem 3--psm 6 outputbase digits'
    #Use the commented code if only digits are to be detected or cropped. Also add a second arguement to the next code as config=configuration
    contour = pytesseract.image_to_boxes(img)
    for letter in contour.splitlines():
        l = letter.split(' ')
        x,y,w,h = int(l[1]),int(l[2]),int(l[3]),int(l[4])
        cv2.rectangle(img,(x,himg - y), (w,himg-h), (0,255,0),1)
        arr_letters.append(l[0])
    arr_letters = remove_char(arr_letters)
    return arr_letters
'''
'''//////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////'''
'''//////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////'''
'''//////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////'''