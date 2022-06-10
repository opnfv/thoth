.. This work is licensed under a Creative Commons Attribution 4.0 International License.
.. http://creativecommons.org/licenses/by/4.0
.. (c) Anuket, The Linux Foundation, BIT Mesra, VTU and Others.


==============================
AI/ML Models for NFV Usecases.
==============================

This document describes all the models created by Anuket-Thoth project.

*********************************
1. Failure prediction (FP) models
*********************************

a. Summary of the VM Failure-Prediction models.
===============================================
We have developed Neural Network models for predicting failures in
virtual machines (VMs) used in network function virtualization (NFV)
environments by analysing VNF data. The data used to build these models
are provided by Orange Labs, and the VMs are based on project Clearwater.

The links for the data are:

* Processed Data: https://drive.google.com/drive/folders/1crrVZMJwf00MP5qM7nmVEqFsatOAShla
* Raw: https://drive.google.com/file/d/1QVipyoWPD1_4W_QXWzxEla4b88EWo5X5/view?usp=drivesdk
* Raw Source: https://www.kaggle.com/datasets/imenbenyahia/clearwatervnf-virtual-ip-multimedia-ip-system


These models are found under *models* directory. In the below table, only the jupyter-notebooks reference is given, which can be found in *models/failure_prediction/jnotebooks* folder . The corresponding python file can be found in *models/failure_prediction/python* folder.

.. list-table:: Summary of Failure Prediction Models.
   :widths: 25 25 25 100
   :header-rows: 1

   * - Model Name
     - Failure type
     - Source-File
     - Comments
   * - Decision Tree
     - Virtual Machine
     - Decision_Tree.ipynb
     - Simplest (implementation-wise) case.
   * - CNN
     - Virtual Machine
     - CNN.ipynb
     - Convolutional Neural Network. Poorest among the Neural-network based models.
   * - LSTM
     - Virtual Machine
     - LSTM.ipynb
     - Basic Long Short-Term Memory. Better than CNN.
   * - Attention LSTM
     - Virtual Machine
     - LSTM_attention.ipynb
     - The attention mechanism distributes weights accordingly. Performance is similar to correlation LSTM.
   * - Correlation LSTM
     - Virtual Machine
     - LSTM_correlation.ipynb
     - Performs the best.
   * - Correlation with Stacked LSTM
     - Virtual Machine
     - stacked_LSTM_correlation.ipynb
     - Second best performance.
   * - Correlation with Bi-LSTM
     - Virtual Machine
     - Bi_LSTMstacked_LSTM_Correlation.ipynb
     - Third best performance.
