import numpy as np
from lightfm.datasets import fetch_movielens
from lightfm import LightFM 

#fetch data and format it
data=fetch_movielens(min_rating=4.0)

#print training and testing data
print(repr(data['train']))
print(repr(data['test']))

#create Model
model=LightFM(loss='warp')
#train Model
model.fit(data['train'], epochs=30,num_threads=2)

def sampleRecom(model,data,user_ids):

	#no of users and movies in train dataset
	n_users,n_items=data['train'].shape

	#generate recommendationds for each user we input
	for user_id in user_ids:

		#movies they already like
		known_positives=data['item_labels'][data['train'].tocsr()[user_id].indices]

		#movies our model predict the user likes
		scores=model.predict(user_id,np.arange(n_items))
		#rank them in order of most liked to least
		top_items=data['item_labels'][np.argsort(-scores)]

		print("user %s" % user_id)
		print(" know positives :" )

		for x in known_positives[:3]:
			print("    %s"%x)

		print("   Recommended")
		
		for x in top_items[:3]:
		    print ("      %s" % x)


sampleRecom(model,data,[24,22])