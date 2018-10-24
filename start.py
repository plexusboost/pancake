from tkinter import *
import unittest
import time
import re
import random
from datetime import date
import sys
import os
import requests
import webbrowser
from selenium import webdriver
from selenium.webdriver.common.keys import Keys


browser = webdriver.Firefox()
now = date.today()
a = 0
b = 0
followNumber = 5000
CycleWaitTime = 70
UnfollowTime = 30


def Log_In():
    try:
        UserName = e1.get()
        Password = e2.get()
        usersearch = e3.get()
        time.sleep(5)
        browser.get('https://www.instagram.com/accounts/login/?source=auth_switcher')
        print('site opened')
        time.sleep(5)

        emailElem = browser.find_element_by_class_name('_2hvTZ') # enter user name
        emailElem.send_keys(UserName)
        print(UserName + ' logged in')
        time.sleep(2)

        #passwordElem = browser.find_element_by_name('password') # enter password
        #passwordElem.send_keys('Hawke65')
        passwordElem = browser.find_element_by_name('password') # enter password
        passwordElem.send_keys(Password)
        print('password entered')
        passwordElem.submit()
        time.sleep(3)
        NoNotify = browser.find_element_by_xpath("""/html/body/div[2]/div/div/div/div[3]/button[2]""").click()
    
    except:
        print('fail, continue')
        pass
    

def like(): # 20,000 comments liked at the end
    likeuser = l1.get()
    d = 0
    e = 0
    print('starting to like comments')
    try:
        #browser.find_element_by_xpath('//*[@id="react-root"]/section/nav/div[2]/div/div/div[3]/div/div[1]/a').click()  #explore button
        #time.sleep(8)
    
        
        searchUser = browser.find_element_by_class_name('XTCLo') # enter user name #XTCLo #x3qfX 
        time.sleep(3)
        searchUser.send_keys(likeuser)
        time.sleep(5)
#Discovery = browser.find_element_by_class_name('coreSpriteDesktopNavExplore') #open Discovery
#Discovery.click()
#print('your are now on Dicovery page')
#time.sleep(3)
        selecthandle = browser.find_element_by_xpath("""//*[@id="react-root"]/section/nav/div[2]/div/div/div[2]/div[2]/div[2]/div/a[1]""").click()
        time.sleep(10)    
        story = browser.find_element_by_class_name('v1Nh3') #select first story
        story.click()
        print('first story selectd')
        time.sleep(3)
        
    except:
        print('fail like, pass')
        pass

    finally:
        try:
            while d < 1000: # 1000 posts
                try:
                    while e < 20: # 20 comments liked per post
                        try:
                            comlike = browser.find_element_by_class_name('coreSpriteCommentLike')
                            comlike.click()
                            time.sleep(2)
                            
                            
                        except:
                            print('fail cycle, pass1')
                            pass
                        finally:
                            e += 1
                            print(e)
                            time.sleep(5)
                except:
                    print('fail cycle, pass2')
                    pass

                finally:
                    e = 0
                    d += 1
                    print(d)
                    rightArrow = browser.find_element_by_class_name('HBoOv') #click right arrow to scroll through discovery feed
                    time.sleep(2)
                    rightArrow.click()
                    print('right arrow')
                    time.sleep(5)
        except:
            pass
        
    
def comment():
    print('comment triggered')
def PFPU():
    
    try:
        
        time.sleep(3)
        Search = browser.find_element_by_xpath("""//*[@id="react-root"]/section/nav/div[2]/div/div/div[2]/input""").send_keys(usersearch)
        time.sleep(3)
        selecthandle = browser.find_element_by_xpath("""//*[@id="react-root"]/section/nav/div[2]/div/div/div[2]/div[2]/div[2]/div/a[1]""").click()
        time.sleep(8)
        Followers = browser.find_element_by_xpath("""//*[@id="react-root"]/section/main/div/header/section/ul/li[2]/a""").click()
        time.sleep(8)
    
        ff = browser.find_elements_by_xpath('/html/body/div[3]/div/div/div[2]/ul/div/li/div/div[2]/button')
        a = 0
        b = 0
        
        while a < followNumber:
            try:
                ff = browser.find_elements_by_xpath('/html/body/div[3]/div/div/div[2]/ul[1]/div/li/div/div[3]/button')
    
                for f in ff:
                    if f.text == 'Follow':
                        f.click()
                        break
                        
        
            except:
                print('while starting to follow something failed, continue')
                pass            
            finally:
                a += 1
                print('complete')
                time.sleep(random.uniform(50,60)) #
            
            if a == followNumber:
                try:
                    print('starting to unfollow')
                    browser.refresh()
                    time.sleep(3)
                    myprofile = browser.find_element_by_xpath('//*[@id="react-root"]/section/nav/div[2]/div/div/div[3]/div/div[3]/a').click()
                    Following = browser.find_element_by_xpath('//*[@id="react-root"]/section/main/div/header/section/ul/li[3]/a').click()
                    time.sleep(8)
                    while b < followNumber:
                        try:
                            ff = browser.find_elements_by_xpath('/html/body/div[3]/div/div/div[2]/ul[1]/div/li/div/div[3]/button')
                                                                
                            for f in ff:
                                if f.text == 'Following':
                                    f.click()
                                    unF = browser.find_element_by_xpath('/html/body/div[4]/div/div/div/div[3]/button[1]').click()
                                    break
                            
            
                    
                        finally:
                            b += 1
                            print('complete')
                            time.sleep(random.uniform(40,50)) # 1.66 minute cycle
            
                except:
                    print('while starting to follow something failed, continue')
                    pass
            
                finally:
                    print(a)
    except:
        print('failed, continue')
        pass
            
def fonly():
    usersearch = e3.get()
    print('Follow Only')
    a = 0
    time.sleep(3)
    Search = browser.find_element_by_xpath('//*[@id="react-root"]/section/nav/div[2]/div/div/div[2]/input').send_keys(usersearch)
    time.sleep(3)
    selecthandle = browser.find_element_by_xpath("""//*[@id="react-root"]/section/nav/div[2]/div/div/div[2]/div[2]/div[2]/div/a[1]""").click()
    time.sleep(8)
    Followers = browser.find_element_by_xpath("""//*[@id="react-root"]/section/main/div/header/section/ul/li[2]/a""").click()
    time.sleep(8)
    while a < 1000:
        try:
            ff = browser.find_elements_by_xpath('/html/body/div[3]/div/div/div[2]/ul[1]/div/li/div/div[3]/button')
            for f in ff:
                if f.text == 'Follow':
                    f.click()
                    break
        except:
            pass
                  
                    
        finally:
            a += 1
            print('complete')
            print(a)
            time.sleep(random.uniform(50,60))
            
        if a % 7 == 0:
            browser.refresh()
            Followers = browser.find_element_by_xpath("""//*[@id="react-root"]/section/main/div/header/section/ul/li[2]/a""").click()
            time.sleep(8)



def post_and_comment_liking():
    h = 0
    a = 0
    b = 0
    c = 0
    total = 0
    hashtags = 100
    posts = 200
    hashtag = [ "#modelphotography" , "#model" , "#modellife" , "#modelling" , "#modeling" , "#photography" , "#modelingagency" ,
     "#modelagency" , "#supermodel" , "#modelmanagement" , "#fashionmodel" , "#photomodel" , "#portrait" , "#fashionmodels" ,
      "#fashion" , "#models" , "#portraitphotography" , "#photo" , "#fashionphotography" , "#femalemodel" , "#modelo" , "#modeltest" ,
       "#fitmodel" , "#portraits" , "#like" , "#altgirl" , "#beautiful" , "#modelscout" , "#altmodel" , "#bhfyp" , "#ig" , "#testshoot" ,
        "#malemodels" , "#photoshoot" , "#modelsearch" , "#modelshoot" , "#modelos" , "#magazine" , "#prilaga" , "#photos" , "#pose" ,
         "#modelswanted" , "#modelstatus" , "#sexymodel" , "#follow" , "#face" , "#photoshooting" , "#photooftheday" , "#instamodel" ,
          "#fashionblogger" , "#bikinigirl" , "#wow" , "#camera" , "#poses" , "#posing" , "#photomodeling" , "#photogenic" ,
           "#fashioneditorial" , "#nikon" , "#beachbody" , "#model" , "#modeling" , "#highfashion" , "#pretty" , "#beautiful" ,
            "#sexy" , "#face" , "#beauty" , "#photoshoot" , "#studio" , "#studiolife" , "#bostonmodel" , "(or" , "wherever" ,
             "you’re" , "from)" , "#fashion" , "#editorial" , "#instamodel" , "#modeltowatch" , "#instamag" , "#magazine" ,
              "#catwalk" , "#runway" , "#fashionshow" , "#clavicles" , "#boudoir" , "#catalog" , "#vogue" , "#MAKEUP" , "#MUA" ,
               "#MAKEUPARTIST" , "#COSMETICS" , "#EYESHADOW" , "#EYES" , "#LIPS" , "#LIPSTICK" , "#MAKEUPADDICT" , "#MAKEUPJUNKIE" ,
                "#INSTAMAKEUP" , "#BEAUTIFUL" , "#BYME" , "#LOVE" , "#FACE" , "#PRETTY" , "#PICOFTHEDAY" , "#BLUSH" , "#HAIR" , "#FACE" ,
                 "#STYLIST" , "#STYLE" , "#WEDDING" , "#PORTRAIT" , "#BEAUTY" , "#ONFLEEK" , "#ONPOINT"]

    print('starting to like posts')
    while a < hashtags: #hashtags number of hashtags to be searched
        try:
            browser.refresh()
            time.sleep(5)
            print('hashtags')
            #search hashtage
            searchUser = browser.find_element_by_class_name('XTCLo') # enter user name #XTCLo #x3qfX 
            time.sleep(3)
            searchUser.send_keys(hashtag[a])
            time.sleep(5)
            #select hashtag
            selecthandle = browser.find_element_by_xpath("""//*[@id="react-root"]/section/nav/div[2]/div/div/div[2]/div[2]/div[2]/div/a[1]""").click()
            time.sleep(10)    
            story = browser.find_element_by_class_name('v1Nh3') #select first story
            story.click()
            print('first story selectd')
            time.sleep(3)
           

            #select first post
            while b < posts: #posts number of posts to be liked for each hashtag
                print(hashtag[a])
                try:
                    print('liking Comments')
                    #like post comments 20 of them
                    comlike = browser.find_element_by_class_name('coreSpriteCommentLike')
                    comlike.click()
                    total += 1
                    time.sleep(5)

                    

                except:
                    print('fail cycle, pass')
                    pass

                finally:
                    print(b)
                    b += 1
                    time.sleep(2)
                    # a += 1 next hashtage to be searched
                    
                if b % 20 == 0:
                    try:
                        heart = browser.find_element_by_class_name('glyphsSpriteHeart__outline__24__grey_9') #like story
                        heart.click()
                        print('Post liked')
                        time.sleep(2)
                        comment = browser.find_element_by_xpath('/html/body/div[3]/div/div[2]/div/article/div[2]/section[3]/div/form/textarea')
                        comment.send_keys('this is awesome! @offerohandbags #love #offerohandbags')
                        time.sleep(1)
                        comment.submit()
                        time.sleep(1)
                        total += 1
                        rightArrow = browser.find_element_by_class_name('HBoOv') #click right arrow to scroll through discovery feed
                        time.sleep(2)
                        rightArrow.click()
                        print('right arrow')
                    except:
                        pass

        except:
            print('pass')
            pass

        finally: # b reset for next loop. 
            print(hashtag[a] + ' cycle finished')
            print(a)
            print('total likes ' + total)
            b = 0
            a += 1
            time.sleep(2)
            
    
def Uonly():
    b = 0
    print('Unfollow only')
    myprofile = browser.find_element_by_xpath('//*[@id="react-root"]/section/nav/div[2]/div/div/div[3]/div/div[3]/a').click()
    time.sleep(3)
    Following = browser.find_element_by_xpath('//*[@id="react-root"]/section/main/div/header/section/ul/li[3]/a').click()
    time.sleep(8)
    while b < 1000:
        try:
            ff = browser.find_elements_by_xpath('/html/body/div[3]/div/div/div[2]/ul[1]/div/li/div/div[3]/button')
            for f in ff:
                if f.text == 'Following':
                    f.click()
                    unF = browser.find_element_by_xpath('/html/body/div[4]/div/div/div/div[3]/button').click()
                    break
        except:
            pass
                  
                    
        finally:
            b += 1
            print('complete')
            print(b)
            time.sleep(random.uniform(50,60))
            
        if b % 7 == 0:
            browser.refresh()
            Following = browser.find_element_by_xpath('//*[@id="react-root"]/section/main/div/header/section/ul/li[3]/a').click()
            time.sleep(8)
            

def Run_Program():
    try:
        name = e1.get()
        password = e2.get()
        command = Log_In()
    except:
        pass


master = Tk()

Label(master, text="User Name").grid(row=0)
Label(master, text="Password").grid(row=1)
Label(master, text="List from this User").grid(row=2)
Label(master, text="Profile to like comments").grid(row=11)
#Label(master, text="How many people to follow?").grid(row=3)
#Label(master, text="cycle wait time").grid(row=4)

submit = Button(master, text = 'Log In', command = Run_Program).grid(row=6)
CustomF = Button(master, text = 'Follow Unfollow Cycle', command = PFPU).grid(row=10)
like1 = Button(master, text = 'like comments', command = like).grid(row=12)
Unfollow = Button(master, text = 'Unfollow Only', command = Uonly).grid(row=8)
followonly = Button(master, text = 'Follow Only', command = fonly).grid(row=7)
commenting = Button(master, text = 'like all', command = post_and_comment_liking).grid(row=13)

e1 = Entry(master)
e2 = Entry(master)
e3 = Entry(master)
l1 = Entry(master)
#e4 = Entry(master)
#e5 = Entry(master)

e1.grid(row=0, column=1)
e2.grid(row=1, column=1)
e3.grid(row=2, column=1)
l1.grid(row=11, column=1)
#e4.grid(row=3, column=1)
#e5.grid(row=4, column=1)

mainloop( )
