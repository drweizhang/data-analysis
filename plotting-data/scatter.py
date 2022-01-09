# Import plotting modules
import matplotlib.pyplot as plt
import seaborn as sns

# Make a scatter plot
plt.plot(versicolor_petal_length, versicolor_petal_width, marker='.', linestyle='none')


# Label the axes
_ = plt.xlabel('species')
_ = plt.ylabel('petal length (cm)')


# Show the result
plt.show()
