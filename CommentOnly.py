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
    


def post_and_comment_liking():
    h = 0
    a = 0
    b = 0
    c = 0
    total = 0
    comcom = c3.get()
    hashtags = 100
    posts = 200
    hashtag = ["#handbags" , "#fashion" , "#bags" , "#handbag" , "#bag" , "#accessories" , "#shopping" , "#purse" , "#style" , "#clutch" , "#shoes" , "#fashionista" , "#instagood" , "#luxury" , "#backpack" , "#fashionblogger" , "#ootd" , "#purses" , "#wallet" , "#slingbag" , "#love" , "#totebag" , "#onlineshopping" , "#handmade" , "#luxurybag" , "#fashionbag" , "#womensfashion" , "#instafashion" , "#sunglasses" , "#bhfyp" , "#handbagsforsale" , "#instastyle" , "#watches" , "#leather" , "#summer" , "#leatherbags" , "#wallets" , "#clutchbag" , "#luxurybags" , "#designer" , "#dress" , "#belts" , "#designerbags" , "#womenbags" , "#satchel" , "#jewelry" , "#clutches" , "#trendy" , "#leatherbag" , "#fashionstyle" , "#handbagshop" , "#folow" , "#slingbags" , "#gucci" , "#crossbodybag" , "#classy" , "#sale" , "#fashionbags" , "#highquality" , "#unique" , "#luxury" , "#fashion" , "#gucci" , "#chanel" , "#style" , "#luxurylife" , "#love" , "#yeezy" , "#hermes" , "#prada" , "#dior" , "#luxurylifestyle" , "#summer" , "#chanelbag" , "#lv" , "#cute" , "#design" , "#louisvuitton" , "#instagood" , "#beautiful" , "#lifestyle" , "#givenchy" , "#gift" , "#interiordesign" , "#best" , "#Valentino" , "#luxuryshoes" , "#guccimarmont" , "#fendi" , "#bhfyp" , "#burberry" , "#cheap" , "#v" , "#bags" , "#bag" , "#interior" , "#christianlouboutin" , "#miumiushoes" , "#slippers" , "#Balenciaga" , "#Gucci" , "#McQueen" , "#McQueenshoes" , "#Valentinosandals" , "#redsoles" , "#chanelsandals" , "#shoes" , "#giuseppezanotti" , "#buscemi" , "#Fendi" , "#pensonalshipping" , "#philippines" , "#Chanel" , "#balenciagasneakers" , "#sandals" , "#louisvuittonshoes" , "#givenchyshoes" , "#instapic" , "#guccidionysus" , "#fashionblogger" , "#acting" , "#actors" , "#auditions" , "#friends" , "#casting" , "#peace" , "#yoga" , "#science" , "#equality" , "#mindfulness" , "#meditation" , "#evolution" , "#resist" , "#stevennbeck" , "#peacesign" , "#globalwarming" , "#enough" , "#equalrights" , "#payitforward" , "#freedomofreligion" , "#marchforourlives" , "#freedom" , "#impeachment" , "#hippies" , "#animalrights" , "#freedomofspeech" , "#freedomofthepress" , "#babyboomer" , "#lgbt" , "#bhfyp" , "#film" , "#actress" , "#hollywood" , "#actorslife" , "#comedy" , "#photography" , "#love" , "#movies" , "#artist" , "#training" , "#theater" , "#television" , "#movie" , "#music" , "#model" , "#fashion" , "#drama" , "#inspiration" , "#thebigbangtheory" , "#director" , "#filmgenre" , "#auditioning" , "#setlife" , "#thehellerapproach" , "#cinema" , "#bradheller" , "#nonmethodacting" , "#grouptheater" , "#art" , "#filmmaking"]
    
    #hashtag = [ "#modelphotography" , "#model" , "#modellife" , "#modelling" , "#modeling" , "#photography" , "#modelingagency" ,
     #"#modelagency" , "#supermodel" , "#modelmanagement" , "#fashionmodel" , "#photomodel" , "#portrait" , "#fashionmodels" ,
      #"#fashion" , "#models" , "#portraitphotography" , "#photo" , "#fashionphotography" , "#femalemodel" , "#modelo" , "#modeltest" ,
       #"#fitmodel" , "#portraits" , "#like" , "#altgirl" , "#beautiful" , "#modelscout" , "#altmodel" , "#bhfyp" , "#ig" , "#testshoot" ,
        #"#malemodels" , "#photoshoot" , "#modelsearch" , "#modelshoot" , "#modelos" , "#magazine" , "#prilaga" , "#photos" , "#pose" ,
         #"#modelswanted" , "#modelstatus" , "#sexymodel" , "#follow" , "#face" , "#photoshooting" , "#photooftheday" , "#instamodel" ,
          #"#fashionblogger" , "#bikinigirl" , "#wow" , "#camera" , "#poses" , "#posing" , "#photomodeling" , "#photogenic" ,
           #"#fashioneditorial" , "#nikon" , "#beachbody" , "#model" , "#modeling" , "#highfashion" , "#pretty" , "#beautiful" ,
            #"#sexy" , "#face" , "#beauty" , "#photoshoot" , "#studio" , "#studiolife" , "#bostonmodel" , "(or" , "wherever" ,
             #"you’re" , "from)" , "#fashion" , "#editorial" , "#instamodel" , "#modeltowatch" , "#instamag" , "#magazine" ,
              #"#catwalk" , "#runway" , "#fashionshow" , "#clavicles" , "#boudoir" , "#catalog" , "#vogue" , "#MAKEUP" , "#MUA" ,
               #"#MAKEUPARTIST" , "#COSMETICS" , "#EYESHADOW" , "#EYES" , "#LIPS" , "#LIPSTICK" , "#MAKEUPADDICT" , "#MAKEUPJUNKIE" ,
                #"#INSTAMAKEUP" , "#BEAUTIFUL" , "#BYME" , "#LOVE" , "#FACE" , "#PRETTY" , "#PICOFTHEDAY" , "#BLUSH" , "#HAIR" , "#FACE" ,
                 #"#STYLIST" , "#STYLE" , "#WEDDING" , "#PORTRAIT" , "#BEAUTY" , "#ONFLEEK" , "#ONPOINT"]

    print('starting to like posts')
    while a < 100: #hashtags number of hashtags to be searched
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
            while b < 50: #posts number of posts to be liked for each hashtag
                print(hashtag[a])
                try:
                    while c < 20:
                        try:
                            print('liking Comments')
                            #like post comments 20 of them
                            time.sleep(3)
                            comlike = browser.find_element_by_class_name('glyphsSpriteComment_like')
                            comlike.click()
                            total += 1
                            time.sleep(2)
                        except:
                            print('comment like failed')
                            pass
                        finally:
                            c += 1
                            print(c)

                    

                except:
                    print('fail cycle, pass')
                    
                    pass

                finally:
                    c = 0
                    b += 1
                    print(b)
                    time.sleep(2)
                    # a += 1 next hashtage to be searched
                    try:
                        heart = browser.find_element_by_class_name('glyphsSpriteHeart__outline__24__grey_9') #like story
                        heart.click()
                        print('Post liked')
                        time.sleep(2)
                        print('com')
                        time.sleep(2)
                    except:
                        pass
                    
                    try:
                        selectcom = browser.find_element_by_xpath('/html/body/div[2]/div/div[2]/div/article/div[2]/section[1]/span[2]/button/span').click()
                        time.sleep(3)
                        commenthashtag = browser.find_element_by_xpath('/html/body/div[2]/div/div[2]/div/article/div[2]/section[3]/div/form/textarea')
                        commenthashtag.send_keys(' ')
                        commenthashtag = browser.find_element_by_xpath('/html/body/div[2]/div/div[2]/div/article/div[2]/section[3]/div/form/textarea')
                        commenthashtag.send_keys(comcom)
                        time.sleep(3)
                        commenthashtag.submit()
                        
                        time.sleep(4)
                      
                        print('commented')
                        total += 1
                        
                    except:
                        pass
                    
                    try:
                        rightArrow = browser.find_element_by_class_name('HBoOv') #click right arrow to scroll through discovery feed
                        time.sleep(2)
                        rightArrow.click()
                        print('right arrow')
                        time.sleep(3)
                    except:    
                        pass

        except:
            print('pass')
            browser.get('https://www.instagram.com/accounts/login/?source=auth_switcher')
            print('site opened')
            time.sleep(5)
            pass

        finally: # b reset for next loop. 
            print(hashtag[a] + ' cycle finished')
            print(a)
            b = 0
            a += 1
            time.sleep(2)
            
    


def Run_Program():
    try:
        name = e1.get()
        password = e2.get()
        command = Log_In()
        
    except:
        pass
    
    #try:
        #time.sleep(5)
        #command = Fonly()
    #except:
        #pass
    
    try:
            
        time.sleep(5)
        command = post_and_comment_liking()
        
    except:
        pass
    
    try:
        time.sleep(5)
        command = Uonly()
        time.sleep(5)
        
    except:
        pass


master = Tk()

Label(master, text="User Name").grid(row=0)
Label(master, text="Password").grid(row=1)
Label(master, text="Follow from this user -").grid(row=2)
Label(master, text="like comments from this user -").grid(row=12)
Label(master, text=" insert comment ").grid(row=7)
#Label(master, text="How many people to follow?").grid(row=3)
#Label(master, text="cycle wait time").grid(row=4)

submit = Button(master, text = 'Log In - Full program', command = Run_Program).grid(row=6)
submit2 = Button(master, text = 'Log In - Only', command = Log_In).grid(row=8)
#CustomF = Button(master, text = 'Follow Unfollow Cycle', command = PFPU).grid(row=10)
#like1 = Button(master, text = 'like comments', command = like).grid(row=12)
Unfollow = Button(master, text = 'Unfollow Only', command = Uonly).grid(row=9)
followonly = Button(master, text = 'Follow Only', command = fonly).grid(row=11)
#commenting = Button(master, text = 'like all', command = post_and_comment_liking).grid(row=13)

e1 = Entry(master)
e2 = Entry(master)
e3 = Entry(master)
l1 = Entry(master)
c3 = Entry(master)
#e4 = Entry(master)
#e5 = Entry(master)

e1.grid(row=0, column=1)
e2.grid(row=1, column=1)
e3.grid(row=2, column=1)
l1.grid(row=12, column=1)
c3.grid(row=7, column=1)
#e4.grid(row=3, column=1)
#e5.grid(row=4, column=1)

mainloop( )
