## Task Overview

In this task, I explored the ethical and social implications of Convolutional Neural Networks (CNN) technology, as discussed in Wall (2019). I also ran a CNN model using the CIFAR-10 dataset to perform object recognition. The practical component involved modifying the input image index to assess the model's predictive accuracy.

---

## Code

```python
import numpy as np
import matplotlib.pyplot as plt

# Display 4x4 grid of images with predictions
LABEL_NAMES = ['airplane', 'automobile', 'bird', 'cat', 'deer', 'dog', 'frog', 'horse', 'ship', 'truck']

fig, axes = plt.subplots(4, 4, figsize=(10, 10))
fig.suptitle('Predictions vs Actual Labels', fontsize=16)

for i, ax in enumerate(axes.flat):
    img = x_test[i]
    actual_label = LABEL_NAMES[y_test[i][0]]
    prediction = model.predict(img.reshape(1, 32, 32, 3))
    predicted_label = LABEL_NAMES[np.argmax(prediction)]

    ax.imshow(img)
    ax.axis('off')
    ax.set_title(f'Pred: {predicted_label}\nActual: {actual_label}', fontsize=10)

plt.tight_layout()
plt.subplots_adjust(top=0.9)
plt.show()
```

![image](https://github.com/user-attachments/assets/305200ee-2fc6-4472-a0cc-40c1a7173b87)

**12 Correct Predictions**

**4 Incorrect Predictions**

**75% Correct**

---

## Reflection

**Your knowledge of the different machine learning algorithms you have covered in this module:**

This exercise deepened my understanding of Convolutional Neural Networks, particularly in their application for image recognition tasks. The layered structure of CNNs, incorporating convolutional, pooling, and dense layers, showcased the importance of feature extraction and dimensionality reduction in improving model performance. Comparing CNNs to other algorithms we've explored in this module, like decision trees or linear regression, highlighted their superiority in handling complex data like images.

**Your individual contributions to the team activities:**

Although this was an individual task, the knowledge I gained from team discussions on machine learning techniques informed my approach. Sharing insights with peers helped refine my understanding of model architecture and troubleshooting techniques, especially when fine-tuning hyperparameters for improved accuracy.

**Your experience as a member of a development team:**

Working independently on this task allowed me to reflect on the collaborative skills honed during group projects. The importance of clear documentation, consistent coding practices, and iterative testing became evident, mirroring the best practices adopted in team settings.

**The impact on your professional/personal development:**

This task reinforced my interest in deep learning and its practical applications. The hands-on experience with CNNs not only enhanced my technical skills but also sparked a deeper appreciation for the ethical implications of AI technologies. Wall (2019) emphasized concerns like bias in training data and the potential misuse of image recognition technologies, which I now consider critical in my future work.
