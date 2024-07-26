# deep_learning_module.py
import numpy as np
import tensorflow as tf
from tensorflow.keras.applications import VGG16
from tensorflow.keras.preprocessing.image import ImageDataGenerator

class DeepLearningModule:
    def __init__(self, input_shape, num_classes):
        self.input_shape = input_shape
        self.num_classes = num_classes
        self.model = self._create_model()

    def _create_model(self):
        base_model = VGG16(weights='imagenet', include_top=False, input_shape=self.input_shape)
        x = base_model.output
        x = tf.keras.layers.GlobalAveragePooling2D()(x)
        x = tf.keras.layers.Dense(self.num_classes, activation='softmax')(x)
        model = tf.keras.models.Model(inputs=base_model.input, outputs=x)
        model.compile(optimizer='adam', loss='categorical_crossentropy', metrics=['accuracy'])
        return model

    def train(self, train_dir, validation_dir, epochs=10):
        train_datagen = ImageDataGenerator(rescale=1./255)
        validation_datagen = ImageDataGenerator(rescale=1./255)

        train_generator = train_datagen.flow_from_directory(
            train_dir,
            target_size=self.input_shape[:2],
            batch_size=32,
            class_mode='categorical'
        )

        validation_generator = validation_datagen.flow_from_directory(
            validation_dir,
            target_size=self.input_shape[:2],
            batch_size=32,
            class_mode='categorical'
        )

        self.model.fit(train_generator, epochs=epochs, validation_data=validation_generator)

    def predict(self, image_path):
        img = tf.keras.preprocessing.image.load_img(image_path, target_size=self.input_shape[:2])
        img_array = tf.keras.preprocessing.image.img_to_array(img)
        img_array = img_array / 255.
        img_array = np.expand_dims(img_array, axis=0)
        return self.model.predict(img_array)

    def evaluate(self, test_dir):
        test_datagen = ImageDataGenerator(rescale=1./255)
        test_generator = test_datagen.flow_from_directory(
            test_dir,
            target_size=self.input_shape[:2],
            batch_size=32,
            class_mode='categorical'
        )
        return self.model.evaluate(test_generator)
