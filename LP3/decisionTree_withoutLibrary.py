import pandas as pd
import numpy as np
from pprint import pprint
dataset = pd.read_csv('dataset.csv',
					names = ['ID','Age','Income','Gender','Maritial Status','Buys'])
dataset = dataset.drop('ID',axis = 1)

def entropy(target_col):
	elements,counts = np.unique(target_col,return_counts = True)
	entropy = np.sum([( -counts[i]/np.sum(counts))*np.log2(counts[i]/np.sum(counts))for i in range(len(elements))])
	return entropy

def InfoGain(data,split_attribute_name,target_name="Buys"):
	total_entropy = entropy(data[target_name])
	vals,counts= np.unique(data[split_attribute_name],return_counts=True)
	Weighted_Entropy = np.sum([(counts[i]/np.sum(counts))*entropy(data.where(data[split_attribute_name]==vals[i]).dropna()[target_name]) for i in range(len(vals))])
	Information_Gain = total_entropy - Weighted_Entropy
	return Information_Gain

def ID3(data,originaldata,features,target_attribute_name="Buys",parent_node_class = None):
#If all target_values have the same value, return this value
	  if len(np.unique(data[target_attribute_name])) <= 1:
	  	return np.unique(data[target_attribute_name])[0]
	  	#If the dataset is empty, return the mode target feature value in the original dataset
	  elif len(data)==0:
	  	return np.unique(originaldata[target_attribute_name])[np.argmax(np.unique(originaldata[target_attribute_name],return_counts=True)[1])]
	  	#If the feature space is empty, return the mode target feature value of the direct parent node --> Note that
	  	#the direct parent node is that node which has called the current run of the ID3 algorithm and hence
	  	#the mode target feature value is stored in the parent_node_class variable.
	  elif len(features) ==0:
	  	return parent_node_class
	  	#If none of the above holds true, grow the tree!
	  else:
	  #Set the default value for this node --> The mode target feature value of the current node
	  	parent_node_class = np.unique(data[target_attribute_name])[np.argmax(np.unique(data[target_attribute_name],return_counts=True)[1])]
	  	#Select the feature which best splits the dataset
	  	item_values = [InfoGain(data,feature,target_attribute_name) for feature in features] #Return the information gain values for the features in the dataset
	  	best_feature_index = np.argmax(item_values)
	  	best_feature = features[best_feature_index]
	  	#Create the tree structure. The root gets the name of the feature (best_feature) with the maximum information
	  	#gain in the first run
	  	tree = {best_feature:{}}
	  	#Remove the feature with the best inforamtion gain from the feature space
	  	features = [i for i in features if i != best_feature]
	  	#Grow a branch under the root node for each possible value of the root node feature
	  	for value in np.unique(data[best_feature]):
	  		value = value
	  		#Split the dataset along the value of the feature with the largest information gain and therwith create sub_datasets
	  		sub_data = data.where(data[best_feature] == value).dropna()
	  		#Call the ID3 algorithm for each of those sub_datasets with the new parameters --> Here the recursion comes in!
	  		subtree = ID3(sub_data,dataset,features,target_attribute_name,parent_node_class)
	  		#Add the sub tree, grown from the sub_dataset to the tree under the root node
	  		tree[best_feature][value] = subtree
	  return(tree)    

def predict(query,tree,default = 1):
	for key in list(query.keys()):
		if key in list(tree.keys()):
		#2.
			try:
				result = tree[key][query[key]]
			except:
				return default
				#3.
			result = tree[key][query[key]]
			#4.
			if isinstance(result,dict):
				return predict(query,result)
			else:
				return result


training_data = dataset.iloc[:8].reset_index(drop=True)
testing_data = dataset.iloc[8:].reset_index(drop=True)


def test(data,tree):
#Create new query instances by simply removing the target feature column from the original dataset and 
#convert it to a dictionary
	queries = data.iloc[:,:-1].to_dict(orient = "records")
	#Create a empty DataFrame in whose columns the prediction of the tree are stored
	predicted = pd.DataFrame(columns=["predicted"]) 
	#Calculate the prediction accuracy
	for i in range(len(data)):
		predicted.loc[i,"predicted"] = predict(queries[i],tree,1.0) 
	print('The prediction accuracy is: ',(np.sum(predicted["predicted"] == data["Buys"])/len(data))*100,'%')

"""
Train the tree, Print the tree and predict the accuracy
"""
tree = ID3(training_data,training_data,training_data.columns[:-1])
pprint(tree)
test(testing_data,tree)
