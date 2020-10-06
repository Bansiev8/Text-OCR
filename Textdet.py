#!/usr/bin/env python
# coding: utf-8

# In[1]:


import pytesseract
import cv2
import streamlit as st
import os


# In[2]:


pytesseract.pytesseract.tesseract_cmd = 'G:\\condapython\\textOCR\\tesseract files\\Tesseract-OCR\\tesseract.exe'


# In[5]:


#img = cv2.imread('test4.png')
#img = cv2.cvtColor(img,cv2.COLOR_BGR2RGB)
#print(pytesseract.image_to_string(img)

def detect_chars(img):
    #detection of characters
    img = cv2.imread(img)
    img = cv2.cvtColor(img,cv2.COLOR_BGR2RGB)
    heightimg, widthimg,nah = img.shape
    boxes = pytesseract.image_to_boxes(img)
    for b in boxes.splitlines():
        #print(b)
        b= b.split(' ')
        #print(b)
        x,y,w,h = int(b[1]),int(b[2]),int(b[3]),int(b[4])
        cv2.rectangle(img,(x,heightimg-y), (w,heightimg-h), (0,255,0),2)
        cv2.putText(img,b[0],(x,heightimg-y+25),cv2.FONT_HERSHEY_COMPLEX, 1,(0,0,255),2)
    cv2.imshow('result',img)
    cv2.imwrite("result_chars.png", img)
    cv2.waitKey(0)



def detect_words(img):
    #detection of words
    img = cv2.imread(img)
    img = cv2.cvtColor(img,cv2.COLOR_BGR2RGB)
    heightimg, widthimg,nah = img.shape
    boxes = pytesseract.image_to_data(img)
    #print(boxes)
    for x,b in enumerate(boxes.splitlines()):
        if x!= 0:
            b = b.split()
            #print(b)
            if(len(b)==12):
                x,y,w,h = int(b[6]),int(b[7]),int(b[8]),int(b[9])
                cv2.rectangle(img,(x,y), (w+x,h+y), (0,255,0),2)
                cv2.putText(img,b[11],(x,y),cv2.FONT_HERSHEY_COMPLEX, 1,(0,0,255),2)
    cv2.imshow('result',img)
    cv2.imwrite("result_words.png", img)
    cv2.waitKey(0)


# In[ ]:


folder_path = '.'

def main():
    st.title("")

    page_bg_img = '''
    <style>
    body {
    background-image: url("https://images.unsplash.com/photo-1542281286-9e0a16bb7366");
    background-size: cover;
    padding=100px
    }
    </style>
    '''

    st.markdown(page_bg_img, unsafe_allow_html=True)

    html_temp = """
    <div style="background-color: black; background-size: cover; padding=100px">
    <h2 style="color:white; text-align:center;">Text OCR</h2>
    </div>
    """
    st.markdown(html_temp, unsafe_allow_html = True)
    
    # select image
    file_name = os.listdir(folder_path)
    selected_file = st.selectbox("Select a image file", file_name)
    img_file = os.path.join(folder_path, selected_file)
    
    #get the message
    #secret_message = st.text_input("Secret message", "Type here")
   
    complete_message = """
    <div style = "background-color:white"
    <h2 style="color:white;text-align:center;">Process Complete</h2>
    </div>
    """
    
    if st.button("Detect Characters"):
        detect_chars(img_file)
        st.success("Detection complete")
        st.success("The image will be saved as result_chars")
    
    if st.button("Detect Words"):
        detect_words(img_file)
        st.success("Detection complete")
        st.success("The image will be saved as result_words")
        
if __name__ =='__main__':
    main()
