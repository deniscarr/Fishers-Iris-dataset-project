# Program Name: fishers.py
# Programmer: Denis Carr
# Date: April 2019

# Importing the Pandas and Numpy libaries for this project.
# Pandas is an open source, BSD-licensed library providing easy-to-use data structures and data analysis tools.
# Numpy is a package for scientific computing with Python
import numpy as np
import pandas as pd
import seaborn as sb

from matplotlib import pyplot as plot

def import_csv():
	""" Import the data from iris.csv using the panda library """

	iris_data = pd.read_csv('iris.csv')
	iris_data.columns = ['sepal_length', 'sepal_width' , 'petal_length', 'petal_width', 'species']

	# Uncomment this to examine the first few rows of the data set
	#iris_data.head(11)

	return iris_data



def show_summary_stats():
	""" Show summary statistics of the iris data set (including min, max, mean, median and std) """

	iris_data = import_csv()

	# Get the shape of the table
	iris_data.shape

	#Find out unique classification/type of iris flower and the amount
	iris_data['species'].unique()
	print(iris_data.groupby('species').size())

	# Get the minimum value of all the column in python pandas
	iris_data.min()

	# Get the maximum value of all the column in python pandas
	iris_data.max()

	# Get the mean value of all the column in python pandas
	iris_data.mean()

	# Get the median value of all the column in python pandas
	iris_data.median()

	# Get the standard deviation value of all the column in python pandas
	iris_data.std()

	# Present the stats in tabular format
	iris_summary = iris_data.describe()
	iris_summary = iris_summary.transpose()
	print(iris_summary)



def show_boxplots(): 
	""" Compare the distributions of sepal length, sepal width, petal length and petal width using boxplots """

	iris_data = import_csv()

	# Compare the distribution of sepal length using a boxplot
	sb.set(style="whitegrid", palette="GnBu_d", rc={'figure.figsize':(11.7,8.27)})
	title="Compare the Distribution of Sepal Length"
	sb.boxplot(x="species", y="sepal_length", data=iris_data)
	plot.title(title, fontsize=30)	# increasing font size
	plot.show()	# Show the plot

	# Compare the distribution of sepal width using a boxplot
	sb.set(style="whitegrid", palette="GnBu_d", rc={'figure.figsize':(11.7,8.27)})
	title="Compare the Distribution of Sepal Width"
	sb.boxplot(x="species", y="sepal_width", data=iris_data)
	# increasing font size
	plot.title(title, fontsize=30)	# increasing font size
	plot.show()	# Show the plot

	# Compare the distribution of petal length using a boxplot
	sb.set(style="whitegrid", palette="GnBu_d", rc={'figure.figsize':(11.7,8.27)})
	title="Compare the Distribution of Petal Length"
	sb.boxplot(x="species", y="petal_length", data=iris_data)
	plot.title(title, fontsize=30)	# increasing font size
	plot.show()	# Show the plot

	# # Compare the distribution of petal width using a boxplot
	sb.set(style="whitegrid", palette="GnBu_d", rc={'figure.figsize':(11.7,8.27)})
	title="Compare the distribution of Petal Width"
	sb.boxplot(x="species", y="petal_width", data=iris_data)
	plot.title(title, fontsize=30)	# increasing font size
	plot.show()	# Show the plot



# Display a number based menu to the usre on program start - user must choose 1, 2 or 3 or error is displayed.
def display_menu():       
	""" Display menu of choices and prompt user for input choice """
	print ("\n\n", 22 * "-" , "MENU" , 22 * "-")
	print ("1. Show summary statistics of the iris data set (including min, max, mean, median and std)") # run summary stats method
	print ("2. Compare the distributions of sepal length, sepal width, petal length and petal width using boxplots") # run diagramming methos
	print ("3. Exit") # exit program
	print ("Please enter your choice [1-3]: ")
	choice = input()
	return choice
	


if __name__ == "__main__":    

	while True:          # While loop which will keep going until user wants to exit
		choice = display_menu()    # Displays menu
		#print (type(choice))
     
		if choice == "1":     
			show_summary_stats()
		elif choice == "2":
			show_boxplots()
		elif choice == "3":
			exit()
		else:
        	# Any integer inputs other than values 1-5 - print an error message
			print("Invalid option selection!! Please try again..")
