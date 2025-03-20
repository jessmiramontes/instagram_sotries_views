# instagram_sotries_views

**Update Feb 6:** I combined all the csvs obtained from meta and started the sentiment analysis for the captions of the stories. So in the final dataset I will have the emotion expressed by the image and the sentiment given by the words. 
I have the program that analyzes the sentiment on the text of the story
Next step: export this information to a csv and then using the Identificador de la publicación, add it to the archivo_combinado.csv file.
**Update Feb 8:** Sentiment analysis for captions done. Next step: clean the dataset with analytics + sentiment. I will remove statistics for videos and then combine with the image Dataset.
I created the final dataset. Next Step: Add manually the "Category".
**Update March 19:** I have the final dataset to start the EDA and the training. 

Files:
1) Instagram_stories_image_dataset.ipynb (Image Analysis and DatasetCreation)
2) approve_data.ipynb
3) combinefiles.ipynb (Program to combine serveral csv files from Meta)
4) sentiment_analysis_caption (Analyse the sentiment on the captions)
5) cleanandcombine.ipynb (Clean the Dataset from meta and combine it with the sentiment and also Image Dataset)
6) ig_stories_training.ipynb