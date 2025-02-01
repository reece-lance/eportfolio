# My Role and Contributions

---

- **Data Preparation and Preprocessing:** Loaded the CIFAR-10 dataset, normalised the image data, and implemented data augmentation techniques such as rotations, flips, and zooming to enhance model generalisation.
- **Model Architecture Design:** Built a convolutional neural network (CNN) architecture using convolutional, batch normalisation, max pooling, dropout, and dense layers. Selected appropriate activation functions like ReLU and SoftMax to optimise performance.
- **Model Training and Evaluation:** Partitioned the dataset into training, validation, and testing sets. Trained the model using categorical cross-entropy as the loss function and SGD with momentum as the optimiser. Evaluated the model using metrics such as accuracy, precision, recall, and F1-score.
- **Hyperparameter Tuning:** Adjusted learning rates, batch sizes, and implemented learning rate decay and early stopping to prevent overfitting and improve model convergence.
- **Visualisation and Reporting:** Generated visualisations including accuracy/loss curves and confusion matrices to interpret model performance. Compiled findings and reflections into a comprehensive report.
 
---

# Specific Examples of My Work

## 1. Data Augmentation Techniques

```python
# Define data augmentation
datagen = ImageDataGenerator(
    rotation_range=15,
    width_shift_range=0.1,
    height_shift_range=0.1,
    horizontal_flip=True,
    fill_mode='nearest'
)

image_index = 0
original_image = x_train[image_index]

fig, axes = plt.subplots(3, 3, figsize=(9, 9))
axes[0, 0].imshow(original_image)
axes[0, 0].set_title("Original", color='#007d9c')
axes[0, 0].axis('off')

# Generate augmentations and plot
for i in range(8):
    batch = next(datagen.flow(np.expand_dims(x_train[image_index], axis=0), batch_size=1))
    augmented_image = (batch[0] * 255).astype(np.uint8)
    axes.flatten()[i + 1].imshow(augmented_image)
    axes.flatten()[i + 1].axis('off')
    axes.flatten()[i + 1].set_title(f"Augmentation {i+1}", color='#007d9c')

plt.suptitle("Example of Data Augmentation on a Single Image", fontsize=16, color='#007d9c')
plt.tight_layout(rect=[0, 0.03, 1, 0.95])
plt.show()
```

![image](https://github.com/user-attachments/assets/d17b2b38-2192-436e-8e10-a06d0588bb62)

## 3. Data Normalisation Techniques

```python
# Visualise images before and after normalisation
fig, axes = plt.subplots(2, 5, figsize=(12, 6))
plt.subplots_adjust(hspace=0.8)  # Increase vertical space between rows
print(y_train[:5])  # Check first 5 labels

for i in range(5):
    axes[0, i].imshow(x_train[i])  # Before normalisation
    axes[0, i].set_title(f"Original {class_labels[y_train[i]].title()}", color='#007d9c')
    axes[0, i].axis('off')

    axes[1, i].imshow((x_train[i] * 255))  # After normalisation
    axes[1, i].set_title(f"Normalized {class_labels[y_train[i]].title()}", color='#007d9c')
    axes[1, i].axis('off')

plt.suptitle("Images Before and After Normalization", fontsize=16, color='#007d9c')
plt.tight_layout(rect=[0, 0.03, 1, 0.95])
plt.show()
```

![image](https://github.com/user-attachments/assets/47c184d7-78bd-4d22-b69e-b19e5ac6fdc5)

## 2. Defining Model

```python
model = Sequential([
    Conv2D(32, (3, 3), activation='relu', input_shape=(32, 32, 3), kernel_regularizer=l2(0.001)),
    BatchNormalization(),
    MaxPooling2D((2, 2)),
    Conv2D(64, (3, 3), activation='relu', kernel_regularizer=l2(0.001)),
    BatchNormalization(),
    MaxPooling2D((2, 2)),
    Conv2D(128, (3, 3), activation='relu', kernel_regularizer=l2(0.001)),
    BatchNormalization(),
    MaxPooling2D((2, 2)),
    Flatten(),
    Dense(256, activation='relu'),
    Dropout(0.3),
    Dense(10, activation='softmax')
])

model.compile(optimizer=SGD(learning_rate=0.005, momentum=0.9),
              loss='categorical_crossentropy',
              metrics=['accuracy'])

lr_reduction = ReduceLROnPlateau(monitor='val_loss', patience=3, factor=0.5, min_lr=1e-6, verbose=1)

early_stopping = EarlyStopping(
    monitor='val_accuracy',  # Can switch to 'val_accuracy'
    patience=10,         # Increase patience to allow more epochs before stopping
    min_delta=0.001,     # Require a small improvement to continue training
    restore_best_weights=True,  # Load the best weights after stopping
    verbose=1
)
history = model.fit(datagen.flow(x_train, y_train, batch_size=64),
                    validation_data=(x_val, y_val),
                    epochs=100,
                    callbacks=[lr_reduction, early_stopping])
```

![image](https://github.com/user-attachments/assets/7a859711-96e9-489a-86dc-da1bd5e02eae)

## 3. Model Performance

**This timeline we created shows the training process from the above model:**

![image](https://github.com/user-attachments/assets/db9964d1-80de-48f9-96e6-435c998e1354)

**This is how the Learning Rate decayed throughout:**

![image](https://github.com/user-attachments/assets/b42ca2c7-b1eb-457b-8d48-40630fe86bf0)

```python
# Training Accuracy Plot
plt.subplot(1, 2, 1)
plt.plot(history.history['accuracy'], label='Training Accuracy', color='#007d9c', linewidth=2)
plt.plot(history.history['val_accuracy'], label='Validation Accuracy', color='#85cce2', linewidth=2)
plt.xlabel('Epochs', fontsize=12, color='#007d9c')
plt.ylabel('Accuracy', fontsize=12, color='#007d9c')
plt.title('Training and Validation Accuracy', fontsize=14, color='#007d9c')
plt.legend()
plt.grid(True, linestyle='--', alpha=0.7)

# Training Loss Plot
plt.plot(history.history['loss'], label='Training Loss', color='#007d9c', linewidth=2)
plt.plot(history.history['val_loss'], label='Validation Loss', color='#85cce2', linewidth=2)
plt.xlabel('Epochs', fontsize=12, color='#007d9c')
plt.ylabel('Loss', fontsize=12, color='#007d9c')
plt.title('Training and Validation Loss', fontsize=14, color='#007d9c')
plt.legend()
plt.grid(True, linestyle='--', alpha=0.7)

plt.tight_layout()
plt.show()
```

**This is the Training and Validation Accuracy and Loss:**

![image](https://github.com/user-attachments/assets/01778f8b-a74a-47ca-8a2d-6cdcc2c23a12)

```python
# Use the trained model to predict on test data
y_pred = model.predict(x_test)

# Convert one-hot encoded test labels to class indices
y_true = np.argmax(y_test, axis=1)

# Convert predicted probabilities to class indices
y_pred_classes = np.argmax(y_pred, axis=1)

# Generate classification report
report_dict = classification_report(y_true, y_pred_classes, target_names=class_labels, output_dict=True)

# Create a summary DataFrame for visualisation
summary_df = pd.DataFrame(report_dict).transpose()
summary_df = summary_df[['precision', 'recall', 'f1-score', 'support']]

# Create a table with updated background and text colors
table = ax.table(cellText=summary_df.round(4).values,
                 colLabels=summary_df.columns,
                 rowLabels=summary_df.index,
                 cellLoc='center',
                 loc='center')
```

![image](https://github.com/user-attachments/assets/82e3492b-2d53-45bb-9a81-4e685c7eb729)

**Overall Accuracy Achieved: 79%**

## 4. Misclassification:

```python
# Generate confusion matrix
cm = confusion_matrix(y_true, y_pred_classes)
disp = ConfusionMatrixDisplay(confusion_matrix=cm, display_labels=class_labels)

fig, ax = plt.subplots(figsize=(10, 10))
disp.plot(ax=ax, cmap=plt.cm.Blues, xticks_rotation='vertical')  # Added cmap and rotation
plt.title('Confusion Matrix', fontsize=16, color='#007d9c')
plt.grid(False)
plt.show()
```

![image](https://github.com/user-attachments/assets/61f3a385-fec6-4f5d-b509-a5128527928d)

```python
# Visualise Misclassified Images
misclassified_idx = np.where(y_pred_classes != y_true)[0]
num_misclassified = len(misclassified_idx)
print(f"Number of misclassified images: {num_misclassified}")

# Display a maximum of 9 misclassified images
num_to_display = min(9, num_misclassified)
if num_to_display > 0:  # Only display if there are misclassified images
    fig, axes = plt.subplots(int(np.ceil(num_to_display/3)), 3, figsize=(10, 10))
    axes = axes.ravel()
    for i in range(num_to_display):
        idx = misclassified_idx[i]
        axes[i].imshow(x_test[idx])
        axes[i].set_title(f"True: {class_labels[y_true[idx]].title()}, Predicted: {class_labels[y_pred_classes[idx]].title()}")
        axes[i].axis('off')

    plt.suptitle("Examples of Misclassified Images", fontsize=16)
    plt.tight_layout(rect=[0, 0.03, 1, 0.95])
    plt.show()
else:
    print("No misclassified images to display.")
```

> **Number of misclassified images: 2132**

**The confusion matrix highlights which classes were correctly classified and where the model struggled, such as distinguishing between cats and dogs.**

![image](https://github.com/user-attachments/assets/9644c5c4-d647-4e48-938a-250dcb2b068e)

### Conclusion

This project enhanced my understanding of convolutional neural networks, data augmentation, and model evaluation techniques. By developing and refining the model, I gained valuable insights into hyperparameter tuning, regularisation methods, and the challenges of distinguishing between visually similar classes. The results will guide future improvements, making this a key step in my professional growth in machine learning and data science.
