# instagram_sotries_views

**Update Feb 6:** I combined all the csvs obtained from meta and started the sentiment analysis for the captions of the stories. So in the final dataset I will have the emotion expressed by the image and the sentiment given by the words. 
I have the program that analyzes the sentiment on the text of the story
Next step: export this information to a csv and then using the Identificador de la publicación, add it to the archivo_combinado.csv file.
**Update Feb 8:** Sentiment analysis for captions done. Next step: clean the dataset with analytics + sentiment. I will remove statistics for videos and then combine with the image Dataset.
I created the final dataset. Next Step: Add manually the "Category".
** Update March 2:** I realized that I need to validate the information on the Image dataset and add the categories so I created a streamlit app to helm me do it.

Files:
1) Instagram_stories_image_dataset.ipynb (Image Analysis and DatasetCreation)
2) app.py (Streamoit app to validate the Image data, edit it if needed and add categories)
3) approve_data.ipynb (to run app.py since images are on a google drive and it is easier to access using Google Colab)
4) combinefiles.ipynb (Program to combine serveral csv files from Meta)
5) sentiment_analysis_caption (Analyse the sentiment on the captions)
6) cleanandcombine.ipynb (Clean the Dataset from meta and combine it with the sentiment and also Image Dataset)
7) ig_stories_training.ipynb
