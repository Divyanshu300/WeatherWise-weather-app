# import streamlit as st
# import pandas as pd
# from sklearn.feature_extraction.text import CountVectorizer
# from sklearn.metrics.pairwise import cosine_similarity

# new_fashion = pd.read_csv('fashion.csv')
# df = pd.read_csv('fashion data.csv')

# cv = CountVectorizer(max_features=5000,stop_words='english')
# vector = cv.fit_transform(new_fashion['TAGS']).toarray()
# similarity = cosine_similarity(vector)
# ctr = 0

# def recommend(fashion,tags=''):
#   global ctr
#   new_fashion2 = new_fashion[new_fashion["PRODUCT_NAME"] == fashion]
#   if new_fashion2.empty == False:
#     if(tags==''):
#       ctr = 0
#       for x in list(new_fashion2):
#         st.write(x['PRODUCT_NAME']+'\t\t'+str(x['TAGS']))
#         ctr+=1

#     else:
#       ctr = 0
#       vector2 = cv.fit_transform(new_fashion2['TAGS']).toarray()
#       similarity2 = cosine_similarity(vector2)
#       df2=  pd.DataFrame({
#           "PRODUCT_NAME":[fashion],
#             "TAGS":[tags]
#       })
#       pd.concat([new_fashion2, df2], ignore_index=True)
#       index=len(new_fashion2["PRODUCT_NAME"])-1
#       distances = sorted(list(enumerate(similarity2[index])), reverse=True, key=lambda x: x[1])
#       for i in distances[:10]:
#         if i[0] < len(new_fashion2):
#             st.write(str(new_fashion2.iloc[i[0]]['PRODUCT_NAME'])+'\t\t'+str(new_fashion2.iloc[i[0]]['TAGS']))
#             ctr+=1
#         else:
#             print("Invalid index.")
#       index = new_fashion[new_fashion['PRODUCT_NAME'] == fashion].index[0]
#       distances = sorted(list(enumerate(similarity[index])),reverse=True,key = lambda x: x[1])
#       for i in distances[1:50-ctr+1]:
#         st.write(str(new_fashion.iloc[i[0]]['PRODUCT_NAME'])+'\t\t'+str(new_fashion.iloc[i[0]]['TAGS']))

#   index = new_fashion[new_fashion['PRODUCT_NAME'] == fashion].index[0]
#   distances = sorted(list(enumerate(similarity[index])),reverse=True,key = lambda x: x[1])
#   for i in distances[:30]:
#     st.write(str(new_fashion.iloc[i[0]]['PRODUCT_NAME'])+'\t\t'+str(new_fashion.iloc[i[0]]['TAGS']))

# # Create a textbox

# input_list2=["Color"]
# input_list3 = ["Pattern", "Gender", "Category", "Season","Personality","Material", "Occasion"]
# input_list = []
# tags =''
# # Create a textbox

# user_input = st.selectbox('PRODUCT_NAME',new_fashion["PRODUCT_NAME"].unique())
# input_list.append(user_input)
# for i in range (len(input_list2)):
#   user_input = st.text_input(f'Enter your text for {input_list2[i]}')
#   input_list.append(user_input)
# for i in range(len(input_list3)):
#   user_input = st.selectbox(input_list3[i],df[input_list3[i].upper()].unique())
#   input_list.append(user_input)
# user_input = st.slider('PRICE',int(df['PRICE'].min()),int(df['PRICE'].max()),step=50)
# input_list.append(user_input)

# for i in input_list[1:]:
#     if(i == "" or i=='nan'):
#         input_list.remove(i)
        
# tags = ""
# for i in input_list[1:]:
#   if(input_list[-1] == i):
#     tags+= str(i).lower()
#   else:
#     tags += str(i).lower()+'  ||  '

# if st.button('Submit',type='primary',use_container_width =True,disabled=False):
#     recommend(input_list[0],tags)