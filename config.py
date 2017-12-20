#Define paths for files
spectrogramsInputPath = "Predict/Spectrograms/"
spectrogramsPath = "Data/Spectrograms/"		  
slicesPath = "Data/Slices/"		  
slicesInputPath = "Predict/Slices/"
datasetPath = "Data/Dataset/"		  
inputDatasetPath = "Predict/Dataset/"
rawDataPath = "Data/Raw/"		 
inputDataPath = "Predict/Raw/"

#Spectrogram resolution
pixelPerSecond = 50

#Slice parameters
sliceSize = 128

#Dataset parameters
filesPerGenre = 100
validationRatio = 0.3
testRatio = 0.1

#Model parameters
batchSize = 128
learningRate = 0.001
nbEpoch = 20
