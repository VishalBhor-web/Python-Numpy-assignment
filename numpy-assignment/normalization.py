import numpy as  np

og_array=np.array([10,20,30,40])
print("Original Array:", og_array)

mean=np.mean(og_array)
print("Mean:", mean)

standard__deviation=np.std(og_array)
print("Standard Deviation:", standard__deviation)

normalized=(og_array-mean)/standard__deviation
print("Normalized Array:", normalized)


resize=normalized.reshape(2,2)
print("Reshaped Array:", resize)
