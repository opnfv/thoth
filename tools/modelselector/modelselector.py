# Copyright 2022 Linux Foundation.
# srao@linuxfoundation.org
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#   http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.

"""
Tool to suggest which ML approach is more applicable for
a particular data and usecase.
TODO:
1. Minimize code.
2. Add Informative data to the user.
3. Check for Size Entry - 1G/K ..
"""

from __future__ import print_function
import signal
import sys
from pypsi import wizard as wiz
from pypsi.shell import Shell

# pylint: disable=line-too-long,too-few-public-methods,too-many-instance-attributes, too-many-nested-blocks, too-many-return-statements, too-many-branches

class Bcolors:
    """
    For Coloring
    """
    HEADER = '\033[95m'
    OKBLUE = '\033[94m'
    OKGREEN = '\033[92m'
    WARNING = '\033[93m'
    FAIL = '\033[91m'
    ENDC = '\033[0m'
    BOLD = '\033[1m'
    UNDERLINE = '\033[4m'

class AlgoSelectorWizard():
    """
    Class to create wizards
    """
    def __init__(self):
        """
        Perform Initialization.
        """
        self.shell = Shell()
        # Set of all values from the user
        self.main_values = {}
        self.main_l1_values = {}
        self.main_l2a_values = {}
        self.main_l2b_values = {}
        self.main_l3_values = {}
        self.main_l4_values = {}
        self.unsup_values = {}
        self.ri_values = {}
        self.gen_values = {}
        self.gen_choice_values = {}
        self.gen_metrics_values = {}
        self.gen_data_main_values = {}
        self.gen_data_text_values = {}
        self.gen_data_features_values = {}
        self.gen_data_signal_values = {}
        self.gen_about_data_basic_values = {}
        self.gen_about_data_adv_values = {}
        self.gen_about_data_output_values = {}
        self.gans_values = {}
        # Set of Wizards.
        self.wiz_main = None
        self.wiz_main_l1 = None
        self.wiz_main_l2_a = None
        self.wiz_main_l2_b = None
        self.wiz_main_l3 = None
        self.wiz_main_l4 = None
        self.wiz_generic = None
        self.wiz_generic_choice = None
        self.wiz_geneirc_metric = None
        self.wiz_generic_data_main = None
        self.wiz_generic_data_signal = None
        self.wiz_generic_data_features = None
        self.wiz_generic_data_text = None
        self.wiz_generic_data_basic = None
        self.wiz_generic_data_adv = None
        self.wiz_generic_data_output = None
        self.wiz_unsupervised = None
        self.wiz_reinforcement = None
        self.wiz_gans = None
        # Some Inferences
        self.ml_needed = False
        self.ml_gans = False
        self.supervised = False
        self.unsupervised = False
        self.reinforcement = False
        self.data_size = 'high'
        self.interpretability = False
        self.faster = False
        self.ftod_ratio = 'low'
        self.reproducibility = False


    ############# All the Wizards ##################################

    ### GENERIC Wizards - Need for ML ##############################
    def main_wizard_l1(self):
        """
        The Main Wizard L1
        """
        self.wiz_main_l1 = wiz.PromptWizard(
            name=Bcolors.OKBLUE+"Do you Need ML - Data Availability"+Bcolors.ENDC,
            description="",
            steps=(
                # The list of input prompts to ask the user.
                wiz.WizardStep(
                    # ID where the value will be stored
                    id="data_availability",
                    # Display name
                    name=Bcolors.HEADER+"Do you have access to data about different situations, or that describes a lot of examples of situations"+Bcolors.ENDC,
                    # Help message
                    help="Y/N - Yes/No",
                    validators=(wiz.required_validator, wiz.boolean_validator),
                    default='Y',
                ),
            )
        )
    
    def gans_wizard(self):
        """
        The GANs Wizard
        """
        self.wiz_gans = wiz.PromptWizard(
            name=Bcolors.OKBLUE+"Synthetic Data Genration using GANs"+Bcolors.ENDC,
            description="",
            steps=(
                # The list of input prompts to ask the user.
                wiz.WizardStep(
                    # ID where the value will be stored
                    id="gans_data_type",
                    # Display name
                    name=Bcolors.HEADER+"Is the sample data you have is time-series? Answer Y/N - Yes/No"+Bcolors.ENDC,
                    # Help message
                    help="Y/N - Yes/No",
                    validators=(wiz.required_validator, wiz.boolean_validator),
                    default='Y',
                ),
                wiz.WizardStep(
                    # ID where the value will be stored
                    id="gans_data_variables",
                    # Display name
                    name=Bcolors.HEADER+"Is the sample data you have is multi-variate (more than one features/columns) ? Answer Y/N - Yes/No"+Bcolors.ENDC,
                    # Help message
                    help="Y/N - Yes/No",
                    validators=(wiz.required_validator, wiz.boolean_validator),
                    default='Y',
                ),
            )
        )


    def main_wizard_l2_a(self):
        """
        The Main Wizard L2-A
        """
        self.wiz_main_l2_a = wiz.PromptWizard(
            name=Bcolors.OKBLUE+"Do you Need ML - Data Creation"+Bcolors.ENDC,
            description="",
            steps=(
                # The list of input prompts to ask the user.
                wiz.WizardStep(
                    # ID where the value will be stored
                    id="data_creativity",
                    # Display name
                    name=Bcolors.HEADER+"Will a system be able to gather a lot of data by trying sequences of actions in many different situations and seeing the results"+Bcolors.ENDC,
                    # Help message
                    help="Y/N - Yes/No",
                    validators=(wiz.required_validator, wiz.boolean_validator),
                    default='Y',
                ),
            )
        )

    def main_wizard_l2_b(self):
        """
        The Main Wizard L2-B
        """
        gan = """ Synthetic data generation is an important use-case for Telco-scenarios, due to difficulty in getting good dataset."""
        label = """ One or more meaningful and informative 'tag' to provide context so that a machine learning model can learn from it. For example, labels might indicate whether a photo contains a bird or car, which words were uttered in an audio recording, or if an x-ray contains a tumor. Data labeling is required for a variety of use cases including computer vision, natural language processing, and speech recognition."""
        self.wiz_main_l2_b = wiz.PromptWizard(
            name=Bcolors.OKBLUE+"Do you Need ML - Data Programmability"+Bcolors.ENDC,
            description="",
            steps=(
                # The list of input prompts to ask the user.
                wiz.WizardStep(
                    # ID where the value will be stored
                    id="data_generation",
                    # Display name
                    name=Bcolors.HEADER+" Do you want to generate Synthetic Data from the existing data (Type Y/N - Yes/No). Type helfp for the description"+Bcolors.ENDC,
                    # Help message
                    help=gan,
                    validators=(wiz.required_validator, wiz.boolean_validator),
                    default='N',
                ),
                wiz.WizardStep(
                    # ID where the value will be stored
                    id="data_label",
                    # Display name
                    name=Bcolors.HEADER+" Do you have Labelled data? (Type Y/N - Yes/No). Type help for description of label. "+Bcolors.ENDC,
                    # Help message
                    help=label,
                    validators=(wiz.required_validator, wiz.boolean_validator),
                    default='Y',
                ),
                wiz.WizardStep(
                    # ID where the value will be stored
                    id="data_programmability",
                    # Display name
                    name=Bcolors.HEADER+"Can a program or set of rules decide what actions to take based on the data you have about the situations"+Bcolors.ENDC,
                    # Help message
                    help="Y/N - Yes/No",
                    validators=(wiz.required_validator, wiz.boolean_validator),
                    default='N',
                ),
            )
        )


    def main_wizard_l3(self):
        """
        The Main Wizard L3
        """
        self.wiz_main_l3 = wiz.PromptWizard(
            name=Bcolors.OKBLUE+"Do you Need ML - Data Knowledge"+Bcolors.ENDC,
            description="",
            steps=(
                # The list of input prompts to ask the user.
                wiz.WizardStep(
                    # ID where the value will be stored
                    id="data_knowledge",
                    # Display name
                    name=Bcolors.HEADER+"Could a knowledgeable human decide what actions to take based on the data you have about the situations"+Bcolors.ENDC,
                    # Help message
                    help="Y/N - Yes/No",
                    validators=(wiz.required_validator, wiz.boolean_validator),
                    default='Y',
                ),
            )
        )

    def main_wizard_l4(self):
        """
        The Main Wizard - L4
        """
        self.wiz_main_l4 = wiz.PromptWizard(
            name=Bcolors.OKBLUE+"Do you Need ML - Data Pattern"+Bcolors.ENDC,
            description="",
            steps=(
                # The list of input prompts to ask the user.
                wiz.WizardStep(
                    # ID where the value will be stored
                    id="data_pattern",
                    # Display name
                    name=Bcolors.HEADER+"Could there be patterns in these situations that the humans haven't recognized before"+Bcolors.ENDC,
                    # Help message
                    help="Y/N - Yes/No.",
                    validators=(wiz.required_validator, wiz.boolean_validator),
                    default='Y'
                ),
            )
        )
    ### GENERIC Wizards - GOAL, METRICS, DATA ##############################
    def gen_choice_wizard(self):
        """
        Generic Wizard - Goal, metrics, data
        """
        self.wiz_generic_choice = wiz.PromptWizard(
            name=Bcolors.OKBLUE+"Understanding Goal, and Preferences"+Bcolors.ENDC,
            description="",
            steps=(
                # The list of input prompts to ask the user.
                wiz.WizardStep(
                    # ID where the value will be stored
                    id="data_goal",
                    # Display name
                    name=Bcolors.HEADER+" What is your goal with the data? Predict, Describe or Explore"+Bcolors.ENDC,
                    # Help message
                    help="Enter one of Predict/Describe/Explore",
                    validators=(wiz.required_validator, wiz.choice_validator(['Predict',
                    	                                                      'predict',
                    	                                                      'Describe',
                    	                                                      'describe',
                    	                                                      'Explore',
                    	                                                      'explore'])),
                    default='Explore'
                ),
                wiz.WizardStep(
                    # ID where the value will be stored
                    id="data_metrics_pref",
                    # Display name
                    name=Bcolors.HEADER+" Do you know which metrics (speed, accuracy, etc.) are more important for you? "+Bcolors.ENDC,
                    # Help message
                    help="Y/N - Yes/No",
                    validators=(wiz.required_validator, wiz.boolean_validator),
                    default='Y'
                ),
                wiz.WizardStep(
                    # ID where the value will be stored
                    id="data_main",
                    # Display name
                    name=Bcolors.HEADER+" Do you know about the input data type (If its signal/features/text)  ?  "+Bcolors.ENDC,
                    # Help message
                    help="Y/N - Yes/No",
                    validators=(wiz.required_validator, wiz.boolean_validator),
                    default='Y'
                ),
                wiz.WizardStep(
                    # ID where the value will be stored
                    id="data_databasic_pref",
                    # Display name
                    name=Bcolors.HEADER+" Do you have basic information (size, count, etc.) about the input data? "+Bcolors.ENDC,
                    # Help message
                    help="Y/N - Yes/No",
                    validators=(wiz.required_validator, wiz.boolean_validator),
                    default='Y'
                ),
                wiz.WizardStep(
                    # ID where the value will be stored
                    id="data_dataadv_pref",
                    # Display name
                    name=Bcolors.HEADER+" Do you have advanced information (distribution, relation, independency, etc.) about the input data? "+Bcolors.ENDC,
                    # Help message
                    help="Y/N - Yes/No",
                    validators=(wiz.required_validator, wiz.boolean_validator),
                    default='Y'
                ),
                wiz.WizardStep(
                    # ID where the value will be stored
                    id="data_dataoutput_pref",
                    # Display name
                    name=Bcolors.HEADER+" Do you have basic information (size, count, etc.) about the output? "+Bcolors.ENDC,
                    # Help message
                    help="Y/N - Yes/No",
                    validators=(wiz.required_validator, wiz.boolean_validator),
                    default='Y'
                ),
            )
        )

    def gen_metrics_wizard(self):
        """
        Generic Wizard - Goal, metrics, data
        """
        self.wiz_generic_metrics = wiz.PromptWizard(
            name=Bcolors.OKBLUE+"Understanding Goal, Metrics, Data and Output Type"+Bcolors.ENDC,
            description="",
            steps=(
                # The list of input prompts to ask the user.
                wiz.WizardStep(
                    # ID where the value will be stored
                    id="metric_accuracy",
                    # Display name
                    name=Bcolors.HEADER+" How important the metric 'Accuracy' is for you? 1-5: 1- Least important 5- Most Important"+Bcolors.ENDC,
                    # Help message
                    help="Enter 1-5: 1 being least important, and 5 being most important",
                    validators=(wiz.required_validator, wiz.int_validator(1, 5)),
                    default='1'
                ),
                wiz.WizardStep(
                    # ID where the value will be stored
                    id="metric_speed",
                    # Display name
                    name=Bcolors.HEADER+" How important the metric 'Speed' is for you? 1-5: 1- Least important 5- Most Important"+Bcolors.ENDC,
                    # Help message
                    help="Enter 1-5: 1 being least important, and 5 being most important",
                    validators=(wiz.required_validator, wiz.int_validator(1, 5)),
                    default='1'
                ),
                wiz.WizardStep(
                    # ID where the value will be stored
                    id="metric_interpretability",
                    # Display name
                    name=Bcolors.HEADER+" How important the metric 'Interpretability' is for you? 1-5: 1- Least important 5- Most Important"+Bcolors.ENDC,
                    # Help message
                    help="Enter 1-5: 1 being least important, and 5 being most important",
                    validators=(wiz.required_validator, wiz.int_validator(1, 5)),
                    default='1'
                ),
                wiz.WizardStep(
                    # ID where the value will be stored
                    id="metric_reproducibility",
                    # Display name
                    name=Bcolors.HEADER+" How important the metric 'Reproducibility' is for you? 1-5: 1- Least important 5- Most Important"+Bcolors.ENDC,
                    # Help message
                    help="Enter 1-5: 1 being least important, and 5 being most important",
                    validators=(wiz.required_validator, wiz.int_validator(1, 5)),
                    default='1'
                ),
                wiz.WizardStep(
                    # ID where the value will be stored
                    id="metric_implementation",
                    # Display name
                    name=Bcolors.HEADER+" How important the metric 'Ease of Implementation and Maintenance' is for you? 1-5: 1- Least important 5- Most Important"+Bcolors.ENDC,
                    # Help message
                    help="Enter 1-5: 1 being least important, and 5 being most important",
                    validators=(wiz.required_validator, wiz.int_validator(1, 5)),
                    default='1'
                ),
            )
        )

    def gen_data_main_wizard(self):
        """
        Generic Wizard - Goal, metrics, data
        """
        self.wiz_generic_data_main = wiz.PromptWizard(
            name=Bcolors.OKBLUE+"Understanding Goal, and Preferences"+Bcolors.ENDC,
            description="",
            steps=(
                # The list of input prompts to ask the user.
                wiz.WizardStep(
                    # ID where the value will be stored
                    id="data_column",
                    # Display name
                    name=Bcolors.HEADER+" What does the data (columns) represent? Please type help and select the associated number"+Bcolors.ENDC,
                    # Help message
                    help="1. Well Defined Features\n 2. Signals - Timeseries, pixels, etc\n 3. Text - Unstructured\n 4. None of the above\n",
                    validators=(wiz.required_validator, wiz.int_validator(1, 4)),
                    default='1'
                ),
            )
        )

    def gen_data_signal_wizard(self):
        """
        Generic Wizard - Goal, metrics, data
        """
        self.wiz_generic_data_signal = wiz.PromptWizard(
            name=Bcolors.OKBLUE+"Understanding Goal, and Preferences"+Bcolors.ENDC,
            description="",
            steps=(
                # The list of input prompts to ask the user.
                wiz.WizardStep(
                    # ID where the value will be stored
                    id="data_signal_type",
                    # Display name
                    name=Bcolors.HEADER+" If Signals, can you choose any one from the below list? Please type help for list "+Bcolors.ENDC,
                    # Help message
                    help="1. Image\n 2. Audio\n 3. Timeseries\n 4. None of the above\n 5. Not Applicable\n  ",
                    validators=(wiz.required_validator, wiz.int_validator(1, 5)),
                    default='3'
                ),
            )
        )

    def gen_data_features_wizard(self):
        """
        Generic Wizard - Goal, metrics, data
        """
        self.wiz_generic_data_features = wiz.PromptWizard(
            name=Bcolors.OKBLUE+"Understanding Goal, and Preferences"+Bcolors.ENDC,
            description="",
            steps=(
                # The list of input prompts to ask the user.
                wiz.WizardStep(
                    # ID where the value will be stored
                    id="data_features",
                    # Display name
                    name=Bcolors.HEADER+" If features, are they well defined? i.e., are all the variables well understood? "+Bcolors.ENDC,
                    # Help message
                    help="Y/N",
                    validators=(wiz.required_validator, wiz.boolean_validator),
                    default='Y'
                ),
                wiz.WizardStep(
                    # ID where the value will be stored
                    id="data_features_count",
                    # Display name
                    name=Bcolors.HEADER+" If features, How many are there? "+Bcolors.ENDC,
                    # Help message
                    help="Number only - Approximate should be OK.",
                    validators=(wiz.required_validator, wiz.int_validator(1, 100000)),
                    default='10'
                ),
            )
        )

    def gen_data_text_wizard(self):
        """
        Generic Wizard - Goal, metrics, data
        """
        self.wiz_generic_data_text = wiz.PromptWizard(
            name=Bcolors.OKBLUE+"Understanding Goal, and Preferences"+Bcolors.ENDC,
            description="",
            steps=(
                # The list of input prompts to ask the user.
                wiz.WizardStep(
                    # ID where the value will be stored
                    id="data_text_type",
                    # Display name
                    name=Bcolors.HEADER+" If Text, can you choose any one from the below list? Please type help for list"+Bcolors.ENDC,
                    # Help message
                    help="1. Webpages\n 2. Emails\n 3. Social-Media Posts\n 4. Books\n 5. Formal Articles\n 6. Speech converted to text\n 7. None of the above\n 8. Not Applicable\n  ",
                    validators=(wiz.required_validator, wiz.int_validator(1, 8)),
                    default='3'
                ),

            )
        )

    def gen_about_data_basic_wizard(self):
        """
        Generic Wizard - Goal, metrics, data
        """
        self.wiz_generic_data_basic = wiz.PromptWizard(
            name=Bcolors.OKBLUE+"Understanding Basic Input Data Information"+Bcolors.ENDC,
            description="",
            steps=(
                # The list of input prompts to ask the user.
                wiz.WizardStep(
                    # ID where the value will be stored
                    id="data_missing",
                    # Display name
                    name=Bcolors.HEADER+" Are there any missing values in the data? "+Bcolors.ENDC,
                    # Help message
                    help="Y/N",
                    validators=(wiz.required_validator, wiz.boolean_validator),
                    default='N'
                ),
                wiz.WizardStep(
                    # ID where the value will be stored
                    id="data_size_bytes",
                    # Display name
                    name=Bcolors.HEADER+" How big is the data in terms of size? (Use K/M/G Bytes unit) "+Bcolors.ENDC,
                    # Help message
                    help="Number(integer) and unit: K for Kilo, M for Mega and G for Giga. Ex: 10G for 10 Giga bytes",
                    validators=(wiz.required_validator),
                    default='1G'
                ),
                wiz.WizardStep(
                    # ID where the value will be stored
                    id="data_size_samples",
                    # Display name
                    name=Bcolors.HEADER+" How big is the data in terms of samples? (Use T/M/B Samples) "+Bcolors.ENDC,
                    # Help message
                    help="Number(integer) and unit: T for Thousand, M for Million and B for Billion. Ex: 1M for 1 Million Samples",
                    validators=(wiz.required_validator),
                    default='1M'
                ),
            )
        )

    def gen_about_data_advanced_wizard(self):
        """
        Generic Wizard - Goal, metrics, data
        """
        self.wiz_generic_data_adv = wiz.PromptWizard(
            name=Bcolors.OKBLUE+"Understanding Advanced Input Data Information"+Bcolors.ENDC,
            description="",
            steps=(
                # The list of input prompts to ask the user.
                wiz.WizardStep(
                    # ID where the value will be stored
                    id="data_distribution",
                    # Display name
                    name=Bcolors.HEADER+" Are you aware of any 'Distribution' that is inherent to the data, we can take advantage of?"+Bcolors.ENDC,
                    # Help message
                    help="Y/N - Yes",
                    validators=(wiz.required_validator, wiz.boolean_validator),
                    default='Y'
                ),
                wiz.WizardStep(
                    # ID where the value will be stored
                    id="data_io_relation",
                    # Display name
                    name=Bcolors.HEADER+" Is the probability of 'Linear Relation' between input and the output is high?"+Bcolors.ENDC,
                    # Help message
                    help="Y/N - Yes/No",
                    validators=(wiz.required_validator, wiz.boolean_validator),
                    default='Y'
                ),
                wiz.WizardStep(
                    # ID where the value will be stored
                    id="data_correlation",
                    # Display name
                    name=Bcolors.HEADER+" Are you confident that there is NO high correlation among the independent variables in your day?"+Bcolors.ENDC,
                    # Help message
                    help="Y/N/ - Yes/No ",
                    validators=(wiz.required_validator, wiz.boolean_validator),
                    default='Y'
                ),
                wiz.WizardStep(
                    # ID where the value will be stored
                    id="data_cond_indep",
                    # Display name
                    name=Bcolors.HEADER+" Are you confident that the variables are conditionally independent?"+Bcolors.ENDC,
                    # Help message
                    help="Y/N/. If probability that it rains given lightining and thunder is same as probability that it rains given lightining, then rain and thunder are conditionally independent",
                    validators=(wiz.required_validator, wiz.boolean_validator),
                    default='Y'
                ),
            )
        )

    def gen_about_output_wizard(self):
        """
        Generic Wizard - Goal, metrics, data
        """
        self.wiz_generic_data_output = wiz.PromptWizard(
            name=Bcolors.OKBLUE+"Understanding Data Output"+Bcolors.ENDC,
            description="",
            steps=(
                # The list of input prompts to ask the user.        
                wiz.WizardStep(
                    # ID where the value will be stored
                    id="data_type_output",
                    # Display name
                    name=Bcolors.HEADER+" What is the expected output data type ? (Please type number associated with type in 'help') "+Bcolors.ENDC,
                    # Help message
                    help=" 1:Numerical-Discrete\n 2:Numerical-Continuous\n 3:Ordinal\n 4:Categorical-Binary\n 5:Categorical-Multiclass",
                    validators=(wiz.required_validator, wiz.int_validator(1, 5)),
                    default='1'
                ),
                wiz.WizardStep(
                    # ID where the value will be stored
                    id="data_output_prob",
                    # Display name
                    name=Bcolors.HEADER+" Is the expected output data a probability value ? "+Bcolors.ENDC,
                    # Help message
                    help="Y/N",
                    validators=(wiz.required_validator, wiz.boolean_validator),
                    default='N'
                ),
            )
        )


    def unsupervised_wizard(self):
        """
        The Un-Supervized Learning Wizard
        """
        self.wiz_unsupervised = wiz.PromptWizard(
            name=Bcolors.OKBLUE+"Understanding Goal, Metrics, Data and Output Type"+Bcolors.ENDC,
            description="",
            steps=(
                # The list of input prompts to ask the user.
                wiz.WizardStep(
                    # ID where the value will be stored
                    id="unsup_goal",
                    # Display name
                    name=Bcolors.HEADER+" What is the main goal? (Please type number associated with type in 'help')"+Bcolors.ENDC,
                    # Help message
                    help="1: Explore Similar Groups (clustering) \n 2: Perform Dimensionality Reduction\n 3: Others\n",
                    validators=(wiz.required_validator, wiz.int_validator(1, 3)),
                    default='1'
                ),
                wiz.WizardStep(
                    # ID where the value will be stored
                    id="unsup_dr_topic_mod",
                    # Display name
                    name=Bcolors.HEADER+" If dimensionality reduction, do you prefer topic modelling ? (Please type NA is you are not sure)"+Bcolors.ENDC,
                    # Help message
                    help="Y/N/NA",
                    validators=(wiz.required_validator, wiz.choice_validator(['Y','N','NA','Na',
                    	                                                      'y','n','na','nA'])),
                    default='NA'
                ),
                wiz.WizardStep(
                    # ID where the value will be stored
                    id="unsup_clus_dv",
                    # Display name
                    name=Bcolors.HEADER+" Are you aware of density variations in your data ? (Please type NA is you are not sure)"+Bcolors.ENDC,
                    # Help message
                    help="Y/N/NA",
                    validators=(wiz.required_validator, wiz.choice_validator(['Y','N','NA','Na',
                    	                                                      'y','n','na','nA'])),
                    default='NA'
                ),
                wiz.WizardStep(
                    # ID where the value will be stored
                    id="unsup_clus_outliers",
                    # Display name
                    name=Bcolors.HEADER+" Are there too many outliers in your data ? (Please type NA is you are not sure)"+Bcolors.ENDC,
                    # Help message
                    help="Y/N/NA",
                    validators=(wiz.required_validator, wiz.choice_validator(['Y','N','NA','Na',
                    	                                                      'y','n','na','nA'])),
                    default='NA'
                ),
                wiz.WizardStep(
                    # ID where the value will be stored
                    id="unsup_clus_groups",
                    # Display name
                    name=Bcolors.HEADER+" If clustering, do you know how many groups to form? (Please type NA is you are not sure)"+Bcolors.ENDC,
                    # Help message
                    help="Y/N/NA",
                    validators=(wiz.required_validator, wiz.choice_validator(['Y','N','NA','Na',
                    	                                                      'y','n','na','nA'])),
                    default='NA'
                ),

            )
        )

    def reinforcement_wizard(self):
        """
        The Reinforced Learning Wizard
        """
        message = """
            Reward  |--------|
            |-------| Agent  |  Action
            | |-----|        |-------|
            | |	    |--------|       |
            | |state                 |
            | |	                     |
            | |	   |-----------|     |
            | |----|Environment|     |
            |------|           |-----|
    	           |-----------|
            """
        self.wiz_reinforcement = wiz.PromptWizard(
            name=Bcolors.OKBLUE+"Reinforcement Specific"+Bcolors.ENDC,
            description="",
            steps=(
                # The list of input prompts to ask the user.
                wiz.WizardStep(
                    # ID where the value will be stored
                    id="ri_info",
                    # Display name
                    name=Bcolors.HEADER+" Type help for reference diagram for reinforcement-learning"+Bcolors.ENDC,
                    # Help message
                    help=message,
                    validators=(wiz.required_validator),
                    default='Type Help or Press Enter'
                ),
                wiz.WizardStep(
                    # ID where the value will be stored
                    id="ri_model_preference",
                    # Display name
                    name=Bcolors.HEADER+" Do you prefer model-based approach? (Type NA if you are not sure) "+Bcolors.ENDC,
                    # Help message
                    help="Y/N/NA",
                    validators=(wiz.required_validator, wiz.choice_validator(['Y','N','NA','Na',
                    	                                                      'y','n','na','nA'])),
                    default='Y'
                ),
                wiz.WizardStep(
                    # ID where the value will be stored
                    id="ri_model_availability",
                    # Display name
                    name=Bcolors.HEADER+" Do you have a model for model-based approach? (Type NA if not applicable) "+Bcolors.ENDC,
                    # Help message
                    help="Y/N/NA",
                    validators=(wiz.required_validator, wiz.choice_validator(['Y','N','NA','Na',
                    	                                                      'y','n','na','nA'])),
                    default='Y'
                ),
                wiz.WizardStep(
                    # ID where the value will be stored
                    id="ri_modelfree_value",
                    # Display name
                    name=Bcolors.HEADER+" In Model-Free approach, do you prefer value-based approach? (Type NA if not applicable) "+Bcolors.ENDC,
                    # Help message
                    help="Y/N/NA",
                    validators=(wiz.required_validator, wiz.choice_validator(['Y','N','NA','Na',
                    	                                                      'y','n','na','nA'])),
                    default='Y'
                ),
                wiz.WizardStep(
                    # ID where the value will be stored
                    id="ri_modelfree_value_state",
                    # Display name
                    name=Bcolors.HEADER+" In Model-Free Value-Based approach, do you prefer state-only model? (Type NA if not applicable) "+Bcolors.ENDC,
                    # Help message
                    help="Y/N/NA",
                    validators=(wiz.required_validator, wiz.choice_validator(['Y','N','NA','Na',
                    	                                                      'y','n','na','nA'])),
                    default='Y'
                ),
                wiz.WizardStep(
                    # ID where the value will be stored
                    id="ri_app_domain",
                    # Display name
                    name=Bcolors.HEADER+" What is the application domain ? (Please type number associated with type in 'help') "+Bcolors.ENDC,
                    # Help message
                    help=" 1:Computer Resource Mgmt.\n 2:Robotics\n 3:Traffic-Control\n 4:Reccommenders\n 5:Autonomous Vehicles\n 6:Games\n 7:Chemistry\n 8:Others\n",
                    validators=(wiz.required_validator, wiz.int_validator(1, 8)),
                    default='1'
                ),
            )
        )

    ############### All the Run Operations ######################
    def run_mainwiz(self):
        """
        Run the Main Wizard
        """
        self.main_wizard_l1()
        self.main_l1_values = self.wiz_main_l1.run(self.shell)
        if self.main_l1_values['data_availability']:
            print("OK-1")
            self.main_wizard_l2_b()
            self.main_l2b_values = self.wiz_main_l2_b.run(self.shell)
            if self.main_l2b_values['data_label']:
                self.supervised = True
            else:
                self.unsupervised = True
            if self.main_l2b_values['data_programmability']:
                print(Bcolors.FAIL+"ML is not required - Please consider alternate approaches\n"+Bcolors.ENDC)
            elif self.main_l2b_values['data_generation']:
                print(Bcolors.OKGREEN+"Looks like you need ML, let's continue"+Bcolors.ENDC)
                self.ml_needed = True
                self.ml_gans = True
            else:
                self.main_wizard_l3()
                self.main_l3_values = self.wiz_main_l3.run(self.shell)
                if self.main_l3_values['data_knowledge']:
                    print(Bcolors.OKGREEN+"Looks like you need ML, let's continue"+Bcolors.ENDC)
                    self.ml_needed = True
                else:
                    self.main_wizard_l4()
                    self.main_l4_values = self.wiz_main_l4.run(self.shell)
                    if self.main_l4_values['data_pattern']:
                        print(Bcolors.OKGREEN+"Looks like you need ML, let's continue"+Bcolors.ENDC)
                        self.ml_needed = True
                    else:
                        print(Bcolors.FAIL+"ML is not required - Please consider alternate approaches\n"+Bcolors.ENDC)
        else:
            self.main_wizard_l2_a()
            self.main_l2a_values = self.wiz_main_l2_a.run(self.shell)
            if self.main_l2a_values['data_creativity']:
                print(Bcolors.OKGREEN+"Looks like you need ML, let's continue"+Bcolors.ENDC)
                self.ml_needed = True
                self.reinforcement = True
            else:
                print(Bcolors.FAIL+"ML is not required - Please consider alternate approaches\n"+Bcolors.ENDC)
    
    def run_gans_wizard(self):
        """
        Run GANs wizard
        """
        self.gans_wizard()
        self.gans_values = self.wiz_gans.run(self.shell)
        if self.gans_values['gans_data_type']:
            if self.gans_values['gans_data_variables']:
                print("GANs technique to consider: TTS-GAN")
            else:
                print("GANs technique to consider: TimeGAN")
        else:
            print("Sorry. We need to discuss, please connect with Anuket Thoth Project <srao@linuxfoundation.org>")
                



    def run_generic_wizard(self):
        """
        Run Generic Wizard
        """
        self.gen_choice_wizard()
        self.gen_choice_values = self.wiz_generic_choice.run(self.shell)
        if self.gen_choice_values['data_metrics_pref']:
            self.gen_metrics_wizard()
            self.gen_metrics_values = self.wiz_generic_metrics.run(self.shell)
        if self.gen_choice_values['data_main']:
            self.gen_data_main_wizard()
            self.gen_data_main_values = self.wiz_generic_data_main.run(self.shell)
            if int(self.gen_data_main_values['data_column']) == 3:
                self.gen_data_text_wizard()
                self.gen_data_text_values = self.wiz_generic_data_text.run(self.shell)
            else:
                self.gen_data_text_values = {'data_text_type': '3'}
            if int(self.gen_data_main_values['data_column']) == 1:
                self.gen_data_features_wizard()
                self.gen_data_features_values = self.wiz_generic_data_features.run(self.shell)
            else:
                self.gen_data_features_values = {'data_features': 'Y',
                                                 'data_features_count': '10'}
            if int(self.gen_data_main_values['data_column']) == 2:
                self.gen_data_signal_wizard()
                self.gen_data_signal_values = self.wiz_generic_data_signal.run(self.shell)
            else:
                self.gen_data_signal_values = {'data_signal_type': '1'}
        else:
            self.gen_data_main_values = {'data_column': '1'}
            print("Unknown Data Type")
        if self.gen_choice_values['data_databasic_pref']:
            self.gen_about_data_basic_wizard()
            self.gen_about_data_basic_values = self.wiz_generic_data_basic.run(self.shell)
        else:
            self.gen_about_data_basic_values = {'data_missing':'N',
                                                'data_size_bytes': '1G',
                                                'data_size_samples': '1M'}
        if self.gen_choice_values['data_dataadv_pref']:
            self.gen_about_data_advanced_wizard()
            self.gen_about_data_adv_values = self.wiz_generic_data_adv.run(self.shell)
        else:
            self.gen_about_data_adv_values = {'data_distribution': 'N',
                                              'data_io_relation': 'N',
                                              'data_correlation': 'N',
                                              'data_cond_indep': 'N'}
        if self.gen_choice_values['data_dataoutput_pref']:
            self.gen_about_output_wizard()
            self.gen_about_data_output_values = self.wiz_generic_data_output.run(self.shell)
        else:
            self.gen_about_data_output_values = {'data_type_output': '1',
                                                 'data_output_prob': 'N'}


    def run_unsupervised_wizard(self):
        """
        Run UnSupervised Learning Wizard.
        """
        self.unsupervised_wizard()
        self.unsup_values = self.wiz_unsupervised.run(self.shell)

    def run_reinforcement_wizard(self):
        """
        Run Reinforced Learning Wizard
        """
        self.reinforcement_wizard()
        self.ri_values = self.wiz_reinforcement.run(self.shell)

    def decide_unsupervised(self):
        """
        Decide which Unsupervised-learning to use
        """
        repro = False
        clus_prob = False
        if int(self.unsup_values['unsup_goal']) == 1:
            # Clustering
            if 'high' in self.data_size:
                if not self.reproducibility:
                    clus_prob = True
                else:
                    repro = True
            else:
                if 'y' in self.unsup_values['unsup_clus_dv'].lower():
                    if 'y' in self.unsup_values['unsup_clus_groups'].lower():
                        clus_prob = True
                    else:
                        print("Unsupervised Learning model to consider: Hierarchical Clustering")
                        return
                else:
                    repro = True
            if repro:
                if 'y' in self.unsup_values['unsup_clus_outliers'].lower():
                    print("Unsupervised Learning model to consider: Hierarchical Clustering")
                else:
                    print("Unsupervised Learning model to consider: DBSCAN")
                return
            if clus_prob:
                if 'y' in self.gen_about_data_output_values['data_output_prob'].lower():
                    print("Unsupervised Learning model to consider: Gaussian Mixture")
                else:
                    print("Unsupervised Learning model to consider: KMeans")
                return
        elif int(self.unsup_values['unsup_goal']) == 2:
            # Dimensionality Reduction
            if 'y' in self.unsup_values['unsup_dr_topic_mod'].lower():
                if 'y' in self.gen_about_data_output_values['data_output_prob'].lower():
                    print("Unsupervised Learning model to consider: SVD")
                else:
                    print("Unsupervised Learning model to consider: LDA")
            else:
                print("Unsupervised Learning model to consider: PCA")
        else:
            print("Sorry. We need to discuss, please connect with Anuket Thoth Project <srao@linuxfoundation.org>")

    def decide_reinforcement(self):
        """
        Decide which reinforement learning to use.
        """
        if (int(self.gen_about_data_output_values['data_type_output']) == 2 or
                'y' in self.ri_values['ri_model_preference'].lower()):
            # Model Bsaed
            if 'y' in self.ri_values['ri_model_availability'].lower():
                print("Reinforcement Learning model to consider - AlphaZero")
            else:
                print("Reinforcement Learning models to consider - World Models, I2A, MBMF, and MBVE")
        elif 'n' in self.ri_values['ri_model_preference'].lower():
            # Model-Free based approach.
            if 'y' not in self.ri_values['ri_modelfree_value'].lower():
                print("Reinforcement Learning models to consider: Policy Gradient and Actor Critic")
            else:
                if 'y' in self.ri_values['ri_modelfree_value_state'].lower():
                    print("Reinforcement Learning models to consider - Monte Carlo, TD(0), and TD(Lambda)")
                else:
                    print("Reinforcement Learning models to consider - SARSA, QLearning, Deep Queue Nets")
        else:
            # Default
            print("Sorry. We need to discuss, please connect with Anuket Thoth Project <srao@linuxfoundation.org>")

    def perform_inference(self):
        """
        Perform Inferences. Used across all 3 types.
        """
        # Decide whether data is Low or High
        self.data_size = 'unknown'
        if ('k' in self.gen_about_data_basic_values['data_size_bytes'].lower() or
                't' in self.gen_about_data_basic_values['data_size_samples']):
            self.data_size = 'low'

        if int(self.gen_metrics_values['metric_interpretability']) >= 3 :
            self.interpretability = True
        if int(self.gen_metrics_values['metric_speed']) >= 3 :
            self.faster = True
        if int(self.gen_metrics_values['metric_reproducibility']) >= 3 :
            self.reproducibility = True

        # Decide Features relative to Data (ftod_ratio) - high/low
        if ('k' in self.gen_about_data_basic_values['data_size_bytes'].lower() or
                't' in self.gen_about_data_basic_values['data_size_samples']):
            if int(self.gen_data_features_values['data_features_count']) > 50:
                self.ftod_ratio = 'high'
        elif ('m' in self.gen_about_data_basic_values['data_size_bytes'].lower() or
                'm' in self.gen_about_data_basic_values['data_size_samples']):
            if int(self.gen_data_features_values['data_features_count']) > 5000:
                self.ftod_ratio = 'high'
        else:
            if int(self.gen_data_features_values['data_features_count']) > 500000:
                self.ftod_ratio = 'high'


    def decide_supervised(self):
        """
        Decide which Supervised learning to use.
        """
        if 'high' in self.data_size:
            # Cover: DT, RF, RNN, CNN, ANN and Naive Bayes
            if self.interpretability:
                if self.faster:
                    print("Supervised Learning model to consider  - Decision Tree")
                else:
                    print("Supervised Learning model to consider  - Random Forest")
            else:
                if int(self.gen_data_main_values['data_column']) == 3:
                    print("Supervised Learning model to consider  - RNN")
                elif (int(self.gen_data_main_values['data_column']) == 2 and
                        int(self.gen_data_signal_values['data_signal_type']) == 1):
                    print("Supervised Learning model to consider  - CNN")
                elif (int(self.gen_data_main_values['data_column']) == 2 and
                        (int(self.gen_data_signal_values['data_signal_type']) == 2 or
                            int(self.gen_data_signal_values['data_signal_type']) == 3)):
                    if 'y' in self.gen_about_data_output_values['data_output_prob'].lower():
                        print("Supervised Learning model to consider  - Naive Bayes")
                    else:
                        print("Supervised Learning model to consider  - ANN")
                else:
                    print("Supervised model to consider  Learning - ANN")
        elif 'low' in self.data_size:
            from_b = False
            # Cover: Regressions
            if 'high' in self.ftod_ratio:
                from_b = True
            else:
                print("Supervised Learning model to consider  - SVN with Gaussian Kernel")
                return
            if int(self.gen_about_data_output_values['data_type_output']) != 2:
                from_b = True
            else:
                if 'y' in self.gen_about_data_adv_values['data_io_relation'].lower():
                    print("Supervised Learning model to consider  - Linear Regression or Linear SVM")
                else:
                    print("Supervised Learning model to consider  - Polynomial Regression or nonLinear SVM")
                return
            if from_b:
                if int(self.gen_about_data_output_values['data_output_type']) == 4:
                    if 'y' in self.gen_about_data_output_values['data_output_prob'].lower():
                        if 'y' in self.gen_about_data_adv_values['data_cond_indep'].lower():
                            print("Supervised Learning model to consider  - Naive Bayes")
                        else:
                            if 'y' in self.gen_about_data_adv_values['data_correlation'].lower():
                                print("Supervised Learning model to consider  - LASSO or Ridge Regression")
                            else:
                                print("Supervised Learning model to consider  - Logistic Regression")
                    else:
                        print("Supervised Learning model to consider  - Polynomial Regression or nonLinear SVM")

                else:
                    print("Supervised Learning model to consider - KNN")
        else:
            # Default
            print("Sorry. We need to discuss, please connect with Anuket Thoth Project <srao@linuxfoundation.org>")

    def ask_and_decide(self):
        """
        THe Main Engine
        """
        self.run_mainwiz()
        if self.ml_gans:
            self.run_gans_wizard()
            return
        if self.ml_needed:
            self.run_generic_wizard()
            if self.supervised:
                self.decide_supervised()
            elif self.unsupervised:
                self.run_unsupervised_wizard()
                self.decide_unsupervised()
            elif self.reinforcement:
                self.run_reinforcement_wizard()
                self.decide_reinforcement()


def signal_handler(signum, frame):
    """
    Signal Handler
    """
    print("\n You interrupted, No Suggestion will be provided!")
    print(signum, frame)
    sys.exit(0)

def main():
    """
    The Main Function
    """
    try:
        algowiz = AlgoSelectorWizard()
        algowiz.ask_and_decide()
    except(KeyboardInterrupt, MemoryError):
        print("Some Error Occured - No Suggestion can be provided")

    print("Thanks for using the Algoselector-Wizard, " +
            "Hope our suggestion will be useful")

if __name__ == "__main__":
    signal.signal(signal.SIGINT, signal_handler)
    main()
