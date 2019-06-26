#Question Number One 

import numpy as np

ArrayQuestionOne = np.arange(10) 
ArrayQuestionOne = np.where(ArrayQuestionOne % 2 == 0, ArrayQuestionOne, -1)
print("\n",ArrayQuestionOne)

#Question Number Two 

ArrayQuestionTwo = np.arange(10)
NewTwoDimentionalArray = ArrayQuestionTwo.reshape(2,5)
print("\n",NewTwoDimentionalArray)

#Question Number Three

ArrayForQuestionThree = np.array([1,2,3])
arr1 = np.repeat(ArrayForQuestionThree,3)
arr2 = np.tile(ArrayForQuestionThree,3)
arr3 = np.r_[arr1,arr2]
print("\n",arr3)

#Question Number Four

ArrayQuestionFourOne = np.array([1,2,3,2,3,4,3,4,5,6])
ArrayQuestionFourTwo = np.array([7,2,10,2,7,4,9,4,9])
print(np.intersect1d(ArrayQuestionFourOne,ArrayQuestionFourTwo))

#Question Number Five 

ArrayForQuestionFiveOne = np.array([1,2,3,2,3,4,3,4,5,6])
ArrayForQuestionFiveTwo = np.array([7,2,10,2,7,4,9,4,9,8])
indices = np.where(ArrayForQuestionFiveOne==ArrayForQuestionFiveTwo)
print("\n",indices)

#Question Number Six

#Formula to generate random float samples within a particular range 

#(b - a) * np.random.random_sample() + a


ArrayForQuestionSix = 5 * np.random.random_sample((3, 5)) +5
print("\n",ArrayForQuestionSix)

#Question Number Seven

#Set the threshold using the function np.set_printoptions(threshold = Number)

np.set_printoptions(threshold = 6)
ArrayForQuestionSeven = np.arange(15)
print("\n",ArrayForQuestionSeven)

#Question Number Eight 
#using numpy function np.set_printoptions(suppress=,precision=)
np.random.seed(100)
rand_arr = np.random.random_sample([3,3]) / 1e3
np.set_printoptions(precision = 6)
np.set_printoptions(suppress = True)
print("\n",rand_arr)

#Question Number Nine 

ArrayForQuestionNine = np.arange(9).reshape(3,3)
print("\n",ArrayForQuestionNine)
ArrayForQuestionNine[:,[0,1]] = ArrayForQuestionNine[:,[1,0]]
print("\n",ArrayForQuestionNine)

#Question Number Ten 

ArrayForQuestionTen = np.arange(9).reshape(3,3)
print("\n",ArrayForQuestionTen)
ArrayForQuestionTen[[0,1],:] = ArrayForQuestionTen[[1,0],:]
print("\n",ArrayForQuestionTen)