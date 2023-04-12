#machine learning

#2 types of programming

#A traditional method  ==== only logic and output is needed we have to addd the input
#B machine learning method  === we have input and output the same time and study both input and output


#2 types of machine learning
#      1. Supervsed machine learning
#      2. unsupervised machine learning

#1.   supervised machine learning ====>  it is based on input and output together we create a machine learning model
# then machine will automatically  predict the model
#      input + output => Model_create
#      model_create ======> new_value =====> output_predicted

#eg: specias prediction
#diabatic prediction

  # 2 types of superrvised machine learning
   #A. classification
   #B. regression

#A. classification  =======>
#input_+ output ====> machine learning model
#model =====> predicted  =======>
#to predict a catagorical data such as [True or False ] or [0 or 1]
# nadako elle enna pareyu
#id          credit score      intrest rate
# 101         750                     8.2
#102          850                     7.5
#103           900                       7
#104          600                       9.2

#diabetic file classification example anu
#iris flower also classificaton


# B. regression====>
##input_+ output ====> machine learning model
# to predict a numerical data
#id          credit score      intrest rate
# 101         750                     8.2
#102          850                     7.5
#103           900                       7
#104          600                       9.2

#here it predict a similar numarical value
#stoct market growth etra enn predict cheiyum
#proper value pareyan pattum using regression

#classificaton

 #decision tree
 # KNN
 # random forest
 # SVM
 #naive bayes algorithm

#regression
  # simple linear regression
  # multiple linear regression
  #polyomial regression


####2. Unsupervised Machine Learning
#>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>
#here only input is given  =======> output_produce

 #Cluster =================> imp concrpt anu
     #UN_ORDERED DATA na ellam order aki mattum
     #mainly used in Market segmentation
        #Market segmentation ====================>
          # eg if we purcare from max or trends they give offer msg to our no
          #this is one of the major advantage of market segmentation

#Inputlabell Class_labell
        #input ======> input_labells
        #output ========> class labell


#Machine Learning.....
#........................................
    #1) Data collection ==========
       #normal datas are colleting from kaggle  for a STEADY Purpose
       #github
       #for a research area we collect datas from that field
     #2) Data cleaning or Data preprocessing ============
       #handling mssing values, handling wrong format data
     #3) Model creation =========
         #applying machine learning algorithms
     #4) Performance evaluation
     #>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>
       #correct ayit wrk cheiyyunoenn analyse cheiyan vendi use cheiyum
       #Model Testing
    #5) Performance improvements
    #>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>

#Training Dta and Testing Data==========>
#machine naml padipich kodukunna datas anu training data ::::
# check the datas that we are trained is testing datas

#Data set  =========>
 #training data =====70%
 #Testing data  ====30%i


#supervised Machine Learning
#,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,
#1) classificaton
   #1) KNN : K Nearest Neighbours
     #supervised Machine Learning algorithms
     #used for both classification and regression
     #mainly used for clssifications
     # k is always an odd number
     #most repeated shapes are taken as a unspecified shape

# distance etween two points
# root of  |(x1-x2)^2 + (y2-y1)^2  ========>ECUclidean formula

# points   x1       y1            target
# p1        7        7            bad
# p2        7        4           bad
# p3        3        4            good
# p4        1        4            good
# p5      3          7            ???     find using KNN


# p1 ------------------- p5
# (7,7)                   (3,7)   = (7-3)*2 + (7-7) ==4
# p2--------------------p5
# (7,4)                 (3,7)  =5
# p3-------------------p5
# (3,4)               (3,7) = 3
# p4-------------------p5
# (1,4)                 (3,7)= root13=3.6
#
# taking nearest 3 ===>
# p3----------good
# p4 ------------good     so by KNN its---------------------->>> good
# p1-------------bad

 #p5===========>GOOD