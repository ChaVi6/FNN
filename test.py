import numpy as np
from matplotlib import pyplot as plt
import main
import render
from sklearn.model_selection import train_test_split

if __name__ == '__main__':
    x, y = render.load_data('C:/FNN/dataset/')
    x_train, x_test, y_train, y_test = train_test_split(x, y, test_size=0.2, random_state=1)
    layers = 1
    model = main.build_model(layers, x_train.shape)
    print("Количество слоев:", layers)
    model.compile(optimizer='adam', loss='binary_crossentropy',
                  metrics=['accuracy'])
    H = model.fit(x_train, y_train, batch_size=10, epochs=10, validation_split=0.2)
    plt.style.use("ggplot")
    plt.figure()
    plt.plot(np.arange(0, 10), H.history["loss"], label="потери во время тренировки")
    plt.plot(np.arange(0, 10), H.history["val_loss"], label="потери при тестировании")
    plt.plot(np.arange(0, 10), H.history["accuracy"], label="точность во время тренировки")
    plt.plot(np.arange(0, 10), H.history["val_accuracy"], label="точность при тестировании")
    plt.title('sigmoid')
    plt.xlabel("Эпохи")
    plt.ylabel("Коэф.точности/потерь")
    plt.legend()
    plt.show()

    #testing
    y_pred = model.predict(x_test, batch_size=10)
    for i in range(16):
        ax = plt.subplot(4, 4, i + 1)
        plt.imshow(x_test[i])
        plt.title(main.normalize_prediction(y_pred[i]))
        plt.axis("off")
    plt.show()
