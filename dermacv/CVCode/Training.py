import getFeatures as GF
import numpy as np
from sklearn import svm
from sklearn.cross_validation import train_test_split
from sklearn.metrics import classification_report
from sklearn.metrics import confusion_matrix
from sklearn.metrics import mean_squared_error, accuracy_score

def train():
    features=[]
    
    for i in range(1,35):
        if i==6 or i==8:
            continue
        filename='SSM'+str(i)
        features.append(GF.getFeatures(filename))
        print i
        
    numpyfeatures=np.array(features)
    
    np.savetxt('TrainingData', numpyfeatures)
    
    print numpyfeatures.shape
    
def classify():
    mela=np.loadtxt('TrainingData_Melanoma')
    notmela=np.loadtxt('TrainingData_NotMelanoma')
    
    mela_labels=[1]*32
    notmela_labels=[-1]*26
    
    data=np.append(mela, notmela, axis=0)
    
    means=np.mean(data, axis=0)
    varis=np.var(data, axis=0)
    
    for i in range(len(data[0])-1):
        data[:,i]=(((data[:,i]-means[i])/3*varis[i])+1)/2
    
    labels_d=np.append(mela_labels, notmela_labels)
    X_train, X_test, y_train, y_test = train_test_split(data, labels_d, test_size=0.25)
    clf=svm.LinearSVC()
    clf=clf.fit(X_train, y_train)
    p_test=clf.predict(X_test)

    p_train=clf.predict(X_train)
    
    print clf.score(X_train, y_train)
    print clf.score(X_test, y_test)
    rmse_train=mean_squared_error(y_train, p_train)**0.5
    rmse_test=mean_squared_error(y_test, p_test)**0.5

    print rmse_train, rmse_test
    
if __name__ == "__main__":
    import sys
    classify()

