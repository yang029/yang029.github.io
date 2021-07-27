---
title: mlIntro
date: 2021-07-19 21:08:56
tags: 
catagories:
---

* ReLU (rectified linear unit) function

* supervised learning
  | Input(x) | Output(y) | Application | Network
  | -| - | - | - |
  | Home Features | price | RealEstate | Standard NN (Neural Network)
  | Ad, user info | Click on ad?(0/1) | Online Advertising | Standard NN
  | Image | Object | photo tagging | CNN (convolutional)
  | Audio | text transcript | Speech | R(recurrent) NN
  | English | Chinese | Machine translation | RNN

* Structured Data: Database (well defined)
* Unstructured Data (Audio, Image, Text)


## Logistic Regression
  > an algorithm for binary classification

  * binary classification: Input x -> Output y (0 or 1)
  * Notation: 
  
    $$ 
    (x, y), x \isin \R^{n_x}, y\isin \{0, 1 \}
    $$ 
    for m training examples: 
    $
        \{( x^{(1)}, y^{(1)}), （x^{(2)}, y^{(2)}) ...,(x^{(m)}, y^{(m)})   \}
    $

  