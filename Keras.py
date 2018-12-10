# Imports
import numpy as np
import pandas as pd
from keras.layers import Dense, Activation, Dropout
from sklearn.preprocessing import LabelBinarizer
from keras.models import Sequential
from keras.preprocessing import text

# Import training Data
train_data = pd.read_csv("/home/alberto/PycharmProjects/p3/data/cleantextlabels7.csv")

# Extract training and validation data
train_size = int(len(train_data) * .75)
train_text = train_data['text'][:train_size]
train_class = train_data['class'][:train_size]
test_text = train_data['text'][train_size:]
test_class = train_data['class'][train_size:]

# Set up dictionary
vocab_size = 10000
tokenize = text.Tokenizer(num_words=vocab_size)
tokenize.fit_on_texts(train_text)

# Set up categories
encoder = LabelBinarizer()
encoder.fit(train_class)

# Set up data to become a dictionary vector
x_train = tokenize.texts_to_matrix(train_text)
y_train = encoder.transform(train_class)
x_test = tokenize.texts_to_matrix(test_text)
y_test = encoder.transform(test_class)

# File to save Machine Learning Meta Data

metaFile = open("metaFile.csv", "w+")
metaFile.write("Model,Score,Accuracy\n")


# Model 1
model1 = Sequential()
model1.add(Dense(512))
model1.add(Activation('relu'))
model1.add(Dropout(0.5))
model1.add(Dense(64))
model1.add(Activation('relu'))
model1.add(Dense(3))
model1.add(Activation('softmax'))

model1.compile(loss='categorical_crossentropy',
              optimizer='adam',
              metrics=['accuracy'])

model1.fit(x_train, y_train, epochs=3)

model1score = model1.evaluate(x_test, y_test)

print('Test score:', model1score[0])
print('Test accuracy:', model1score[1])

metaFile.write("Model1," + str(model1score[0])+ ","+str(model1score[1]) + "\n")

# Model 2
model2 = Sequential()
model2.add(Dense(512))
model2.add(Activation('relu'))
model2.add(Dense(3))
model2.add(Activation('softmax'))

model2.compile(loss='categorical_crossentropy',
              optimizer='adam',
              metrics=['accuracy'])

model2.fit(x_train, y_train, epochs=3)

model2score = model2.evaluate(x_test, y_test)

print('Test score:', model2score[0])
print('Test accuracy:', model2score[1])

metaFile.write("Model2," + str(model2score[0])+ ","+str(model2score[1]) + "\n")

# Model 3
model3 = Sequential()
model3.add(Dense(32))
model3.add(Activation('relu'))
model3.add(Dropout(0.5))
model3.add(Dense(124))
model3.add(Activation('relu'))
model3.add(Dropout(0.5))
model3.add(Dense(512))
model3.add(Activation('relu'))
model3.add(Dropout(0.5))
model3.add(Dense(3))
model3.add(Activation('softmax'))

model3.compile(loss='categorical_crossentropy',
              optimizer='adam',
              metrics=['accuracy'])

model3.fit(x_train, y_train, epochs=3)

model3score = model3.evaluate(x_test, y_test)

print('Test score:', model3score[0])
print('Test accuracy:', model3score[1])

metaFile.write("Model3," + str(model3score[0]) + ","+str(model3score[1]) + "\n")


# Prepare to test predictions
text_labels = encoder.classes_
prediction_data = pd.read_csv("/home/alberto/PycharmProjects/p3/data/keywords.csv", error_bad_lines=False)

prediction_text = prediction_data['text'][:]
x_prediction = tokenize.texts_to_matrix(test_text)

modelFile = open("modelDataOut.csv", "w+")
modelFile.write("\'text\',\'model1prediction\',\'model2prediction\',\'model3prediction\'\n")

model1count = [0,0,0]
model2count = [0,0,0]
model3count = [0,0,0]

for i in range(0,len(x_prediction)):
    modelFile.write("\'" + str(prediction_text[i]))
    model1Prediction = model1.predict(np.array([x_prediction[i]]))
    model1Predicted_label = text_labels[np.argmax(model1Prediction)]
    modelFile.write("\',\'" + str(model1Predicted_label))
    if model1Predicted_label == 0:
        model1count[0] = model1count[0] + 1
    if model1Predicted_label == 1:
        model1count[1] = model1count[1] + 1
    if model1Predicted_label == 2:
        model1count[2] = model1count[2] + 1

    model2Prediction = model2.predict(np.array([x_prediction[i]]))
    model2Predicted_label = text_labels[np.argmax(model2Prediction)]
    modelFile.write("\',\'" + str(model2Predicted_label))
    if model2Predicted_label == 0:
        model2count[0] = model2count[0] + 1
    if model2Predicted_label == 1:
        model2count[1] = model2count[1] + 1
    if model2Predicted_label == 2:
        model2count[2] = model2count[2] + 1

    model3Prediction = model3.predict(np.array([x_prediction[i]]))
    model3Predicted_label = text_labels[np.argmax(model3Prediction)]
    modelFile.write("\',\'" + str(model3Predicted_label) + "\'\n")
    if model1Predicted_label == 0:
        model3count[0] = model3count[0] + 1
    if model1Predicted_label == 1:
        model3count[1] = model3count[1] + 1
    if model1Predicted_label == 2:
        model3count[2] = model3count[2] + 1


metaFile.write("\nModel,0-NotRelated,1-Related,2-Ambiguous,Total\n")
metaFile.write("Model1," + str(model1count[0]) + ","+str(model1count[1]) + "," + str(model1count[2]) + "," + str(model1count[0] + model1count[1] + model1count[2]) + "\n")
metaFile.write("Model2," + str(model2count[0]) + ","+str(model2count[1]) + "," + str(model2count[2]) + "," + str(model2count[0] + model2count[1] + model2count[2]) + "\n")
metaFile.write("Model3," + str(model3count[0]) + ","+str(model3count[1]) + "," + str(model3count[2]) + "," + str(model3count[0] + model3count[1] + model3count[2]) + "\n")
metaFile.close()
modelFile.close()

print(model1count[:])
print(model2count[:])
print(model3count[:])

