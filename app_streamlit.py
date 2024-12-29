import streamlit as st

# writing a string
st.write('What is the mean ?')

# displaying a number
import numpy as np
binom_dist = np.random.binomial(1, .5, 100)
st.write(np.mean(binom_dist))

# plot histogram
import matplotlib.pyplot as plt

list_of_means = []
for i in range(0, 1000):
 list_of_means.append(np.random.choice(binom_dist, 100, replace=True).
mean())
fig, ax = plt.subplots()  # create a new figure window
ax = plt.hist(list_of_means)
st.pyplot(fig)

# plotting second figure
fig2, ax2 = plt.subplots()
ax2 = plt.hist([1,1,1,1])
st.pyplot(fig2)