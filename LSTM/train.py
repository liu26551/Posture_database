import configs
from DataProcess import *
from sklearn.model_selection import train_test_split
import model

opt = configs.set_args()
path = opt.dataset_path
timestep = opt.time_step
epochs = opt.epochs
output_size = opt.output_size
batch_size = opt.batch_size
saved_path = opt.save_model

print("loading data..............")
data,label = loadData(path)
feature_dim = data.shape[1]
data = Norm(data)
timeSeq_data,timeSeq_label = CreateTimeSeq(data,label,timestep)
print("training..................")
x_train, x_test, y_train, y_test = train_test_split(timeSeq_data, timeSeq_label, test_size=0.2, shuffle=False)
model = model.lstm(timestep,feature_dim,output_size)
model.compile(optimizer='adam', loss='sparse_categorical_crossentropy', metrics=['accuracy'])
history = model.fit(x=x_train, y=y_train, epochs=epochs, validation_data=(x_test, y_test), batch_size=batch_size, verbose=2)
print("saving model.............")
model.save(saved_path+'LSTM.h5')
print("complete!!!!")
# print(model.predict(x_test))