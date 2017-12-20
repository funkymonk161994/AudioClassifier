This project was developed while I took a graduate course under Prof. Josh Gordon called 
Introduction to DeepLearning. In the begining of the course I found out that there will be a project
and hence this project idea came to existence.

We can hear a song and possibly predict it's genre within 3-5 seconds so why not apply AI to do the same.

For that to work after a little bit of research on the web this was the pipeline which seemed possible to
do this task:

1. Read .mp3 files from a folder 
2. Check if it's stereo or mono (because stereo is same data twice)
3. Convert it into frequency-time graph (called Spectrograph) and label it (genre)
4. Conver these graphs into .png divide those into smaller slices (128 X 128 pixels in this case).
5. Feed these slice into CNN model to train validate and test (70-20-10 Split)
6. Once done can be repeated but this time to predict

It was a big task in terms of computational power, I was ambitious to imagine I can use million songs
dataset from UCI unfortunately couldn't get my hand on it but I started off with some music .mp3 file
(roughly 100 each genre) and started off with the process.

Took around 4-5 hours to train and additionally same time to prepare the dataset.
The dataset contains songs in even distribution across 4 genres: Electronic, Metal, Hip-Hop and Classical

Recommendation: for anyone replicating the project, please perform this in linux environment.


In this project it was done using the following python libraries:

1. eyed3 (or eyeD3) on MacOS case-senstivity can be an issue
2. sox --with-lame (recommend to use linuxbrew or brew installer)
3. libsox-fmt-mp3 (mp3 handler for sox) (Optional if you run into issues)
3. tensorflow
4. tflearn

To train your own model:
1. Collect your .mp3 files labelled (meaning in it's properties the genre should be labelled)
2. Place it in Data/Raw folder (adding to previous data or can be deleted)
3. Run slice -> train -> test
4. Accuracy can be checked on command line right after train and test as well

To make a prediction:
1. Place your .mp3 file in Predict/Raw
2. Run sliceInput -> predict
3. Two outputs will be provided one giving probability of song falling into each category
another giving final category depending upong the highest probability

The project is executed from main.py which takes 5 arguments e.g. "python main.py slice:
1. slice (prepare dataset can be expanded)
2. train
3. test
4. sliceInput (prepare data for prediction)
5. predict

Notes: step 1 was too long sometimes because there is no order in which files are read and if there's
some issues in reading the encoding of file (UTF-8 or ASCII) the process will stop leading to rebuilding
the spectrograms (redundant) hence the part where the intermediate .mp3 files are deleted is commented but
can be uncommented with more moderated dataset.
Step 2 and 3 takes roughly 5-6 hours but could be that my machine was slower running i7 and 8gb ram.

