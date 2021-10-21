.. _thoth:

.. This work is licensed under a Creative Commons Attribution 4.0 International License.
.. http://creativecommons.org/licenses/by/4.0
.. SPDX-License-Identifier CC-BY-4.0
.. (c) Anuket and its contributors

*********************************
Anuket Thoth
*********************************

Title: Thoth Models

Introduction: AI has potential in creating value in terms of enhanced workload availability 
and improved performance and efficiency for NFV usecases. This work aims to build machine-Learning 
models and Tools that can be used by Telcos (typically by the operations team in Telcos). Each 
of these models aims to solve single problem within a particular category. For example, the first 
category we have chosen is Failure prediction, and we aim to create 6 models - failure prediction 
of VMs. Containers, Nodes,  Network-Links, Applications, and middleware services. This project 
also aims to define set of data models for each of the decision making problems, that will help 
both provider and consumer of the data to collaborate.

Section: Failure Prediction

.. list-table:: Failure Prediction
   :widths: 25 50 50 50
   :header-rows: 0
   
   * - Model Name
     - DataSet Tested With
     - Usage (possible modifications)
     - Additional Comments
   * - Decision Tree
     - Orange published IMS clearwater VNF data
     - NA
     - We considered it as our Baseline Machine Learning Model and later compared it's result with
       other Neural Networks models.
   * - LSTM
     - Orange published IMS clearwater VNF data
     - NA
     - The RMSE score is not good so we decided to go with other variants of LSTM.
   * - LSTM-Correlation
     - Orange published IMS clearwater VNF data
     - NA
     - NA
   * - Stacked-LSTM-Correlation
     - Orange published IMS clearwater VNF data
     - NA
     - NA
   * - LSTM-Attention
     - Orange published IMS clearwater VNF data
     - NA
     - NA
   * - CNN
     - Orange published IMS clearwater VNF data
     - NA
     - NA
   * - Bi-LSTM Stacked-LSTM-Correlation
     - Orange published IMS clearwater VNF data
     - NA
     - NA