## Task Overview

In this task, I experimented with different parameters in Support Vector Machine (SVM) models to assess their impact on model performance metrics such as AUC (Area Under the Curve) for classification tasks and R² error for regression tasks. This allowed me to understand how parameter tuning influences model accuracy and generalisability.

---

## Code and Results

### Classification Task: Impact of Kernel on AUC

```python
from sklearn.datasets import make_classification
from sklearn.model_selection import train_test_split
from sklearn.svm import SVC
from sklearn.metrics import roc_auc_score, confusion_matrix, ConfusionMatrixDisplay
import matplotlib.pyplot as plt

# Generate synthetic data
X_class, y_class = make_classification(random_state=0, n_samples=1000, n_features=20, n_informative=15)
X_train_class, X_test_class, y_train_class, y_test_class = train_test_split(X_class, y_class, random_state=0)

# Trying different kernels for SVM classification
kernels = ['linear', 'poly', 'rbf', 'sigmoid']
auc_scores = {}

for kernel in kernels:
    clf = SVC(kernel=kernel, probability=True, random_state=0)
    clf.fit(X_train_class, y_train_class)
    y_proba = clf.predict_proba(X_test_class)[:, 1]
    auc = roc_auc_score(y_test_class, y_proba)
    auc_scores[kernel] = auc

    # Plot confusion matrix
    y_pred = clf.predict(X_test_class)
    cm = confusion_matrix(y_test_class, y_pred)
    disp = ConfusionMatrixDisplay(confusion_matrix=cm, display_labels=clf.classes_)
    disp.plot()
    plt.title(f'Confusion Matrix - Kernel: {kernel}')
    plt.savefig(f'confusion_matrix_{kernel}.png')
    plt.close()

print(auc_scores)
```

> **{'linear': 0.763, 'poly': 0.893, 'rbf': 0.943, 'sigmoid': 0.583}**

**Confusion Matrices:**

![image](https://github.com/user-attachments/assets/8ca033fb-3680-431a-abe5-53224e5bec31)

![image](https://github.com/user-attachments/assets/cd00d9f8-7c55-4c09-a43b-1e70cb68a6dc)

![image](https://github.com/user-attachments/assets/f7c26c59-3683-445a-8561-7ff06c99e147)

![image](https://github.com/user-attachments/assets/b0f4a305-d1aa-4cb1-84cc-f70e01a845da)

### Regression Task: Impact of C Parameter on R² Error

```python
from sklearn.datasets import make_regression
from sklearn.svm import SVR
from sklearn.metrics import r2_score

# Generate synthetic regression data
X_reg, y_reg = make_regression(random_state=0, n_samples=1000, n_features=20, noise=0.1)
X_train_reg, X_test_reg, y_train_reg, y_test_reg = train_test_split(X_reg, y_reg, random_state=0)

# Trying different C values for SVR regression
C_values = [0.1, 1, 10, 100]
r2_scores = {}

for C in C_values:
    reg = SVR(C=C)
    reg.fit(X_train_reg, y_train_reg)
    y_pred = reg.predict(X_test_reg)
    r2 = r2_score(y_test_reg, y_pred)
    r2_scores[C] = r2

print(r2_scores)
```

> **{0.1: -0.024, 1: 0.040, 10: 0.562, 100: 0.915}**

---

## Reflection

### Knowledge of Machine Learning Algorithms
Through this task, I deepened my understanding of Support Vector Machines for both classification and regression tasks. Experimenting with different kernels revealed how non-linear transformations, such as the RBF kernel, significantly enhance model performance, as evidenced by the higher AUC score. Similarly, adjusting the regularisation parameter `C` in SVR demonstrated its impact on model flexibility and overfitting control, where higher `C` values led to better R² scores.

### Individual Contributions
This task required me to independently adjust model parameters, run experiments, and interpret the results. My focus was on systematically varying the kernel and regularisation parameters to observe their influence on model performance metrics. I ensured proper documentation of code and visual outputs to reflect a comprehensive understanding of the topic.

### Experience as a Development Team Member
While this was an individual task, the skills I applied and refined—such as model tuning, performance evaluation, and critical analysis—are directly transferable to team-based projects. Understanding how parameter adjustments affect performance will be invaluable when collaborating with others on machine learning projects, ensuring that models are both robust and interpretable.

### Impact on Professional/Personal Development
Completing this task has significantly enhanced my ability to evaluate machine learning models critically. It has also improved my coding proficiency, particularly in using `scikit-learn` for performance measurement. These skills are not only essential for academic success but also highly relevant to my future career in data science, where model optimisation is a key component of delivering actionable insights.
