"""
The 7 Steps of Machine Learning:

    1) Data Collection
    2) Data Preparation
    3) Choose a Model
    4) Train the Model
    5) Evaluate the Model
    6) Parameter Tuning
    7) Make Predictions

"""
import tensorflow as tf
from matplotlib import pyplot as plt


def main():
    mnist = tf.keras.datasets.mnist

    (x_train, y_train), (x_test, y_test) = mnist.load_data()
    x_train, x_test = x_train / 255.0, x_test / 255.0

    print(x_train.shape, y_train.shape)
    print(x_test.shape, y_test.shape)

    for i in range(9):
        plt.subplot(3, 3, i + 1)
        plt.tight_layout()
        plt.imshow(x_train[i], cmap='Greys')
        plt.title("Label: {}".format(y_train[i]))
        plt.xticks([])
        plt.yticks([])

    plt.show()

    model = tf.keras.models.Sequential([
        tf.keras.layers.Flatten(input_shape=(28, 28)),
        tf.keras.layers.Dense(128, activation='relu'),
        tf.keras.layers.Dropout(0.2),
        tf.keras.layers.Dense(10, activation='softmax')
    ])

    model.compile(optimizer='adam',
                  loss='sparse_categorical_crossentropy',
                  metrics=['accuracy'])

    model.fit(x_train, y_train, epochs=5)
    model.evaluate(x_test, y_test)


if __name__ == '__main__':
    main()
