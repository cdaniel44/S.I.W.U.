#deep learning model in five steps

#1. Network Definition: in this phase we need to define the layers.Thanks to Keras this step is easy because it defines neural networks as sequences and to define layers we just need to create a sequence instance with mentioning the number of outputs

#2. Network Compiling: Now we need to compile the network including choosing the optimizing technique like Stochastic Gradient Descent (sgd) and a Loss function (Loss function is used to measure the degree of fit) to evaluate the model we can use Mean Squared Error (mse)

#3. Network Fitting:a Back-Propagation algorithm is used during this step based on the parameters specified in the compiling step.

#4. Network Evaluation : After fitting the network an evaluation operation is needed to evaluate the performance of the model

#5. Prediction: Finally after training the deep learningmodel we now can use it to predict a new malware sample using a testing dataset
