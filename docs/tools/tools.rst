.. This work is licensed under a Creative Commons Attribution 4.0 International License.
.. http://creativecommons.org/licenses/by/4.0
.. (c) Anuket, The Linux Foundation, BIT Mesra, VTU and Others.

***********************
Anuket Thoth: The Tools
***********************

Model Selector
==============

This is an interactive tool to suggest the best model a researcher can start with to solve a problem in hand.
The tool asks questions about the problem, the type and quantity of the dataset, the metrics preferences,
and the understanding of the dataset. Based on the responses, the tool will suggest the ML technique to start with.
The techniques suggested are broadly categorised into three groups - Supervised, Unsupervised and Reinforcement.

Data Extractor
==============

This tool, in phase-1, extracts monitoring data from Prometheus server.
It takes the prometheus server IP, the timestamp, and the time range as input.
Based on the input, the tool extracts CPU, Memory and Interface data from the server.
