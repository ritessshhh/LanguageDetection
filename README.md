 # LinguaNet: A Neural Network Based Language Identification System

 ## Project Overview
 LinguaNet is a language identification model built on Deep Neural Networks (DNNs) using Python and TensorFlow. It employs character n-grams to classify the language of any given text input. The system is capable of ingesting user inputs and efficiently outputting the identified language.

 This project includes the visualization of learned features using techniques such as t-SNE and PCA to give insights into how the network differentiates between languages. The model has demonstrated a final accuracy of 89.2%, illustrating its effectiveness in language identification.

 ## Dependencies
 Python (>=3.7) <br>
 TensorFlow (>=2.4.0) <br>
 Scikit-learn (>=0.24.0) <br>
 Numpy (>=1.19.5) <br>
 Matplotlib (>=3.3.2) <br>

 ## Installation
 Clone the repo
 ```bash
 git clone https://github.com/ritessshhh/languageDetection
 ```

## Example

 #### 1. When you load the page, it is visible to you like this 

 <img width="1439" alt="Screenshot 2023-07-08 at 10 24 53 PM" src="https://github.com/mohamzamir/LinguaNet-A-Neural-Network-Based-Language-Identification-System/assets/91626899/3a389d8d-ac8f-4a5a-a083-14be1dc6e81b">

 #### 2. When you click on the languages, it gives you example of the languages you can use to recognize.
 
<img width="1433" alt="Screenshot 2023-07-08 at 10 26 04 PM" src="https://github.com/mohamzamir/LinguaNet-A-Neural-Network-Based-Language-Identification-System/assets/91626899/fdd7be25-75e3-4b29-b2b2-04c094283c26">

 #### 3. In this example, I have put one Spanish sentence in the Langauge box.

<img width="1440" alt="Screenshot 2023-07-08 at 10 27 57 PM" src="https://github.com/mohamzamir/LinguaNet-A-Neural-Network-Based-Language-Identification-System/assets/91626899/d8bcef62-ffb0-4999-b3e3-da7f9757a595">

#### 4. When 'Submit' button is clicked, it shows the identified langauge.

<img width="1440" alt="Screenshot 2023-07-08 at 10 28 56 PM" src="https://github.com/mohamzamir/LinguaNet-A-Neural-Network-Based-Language-Identification-System/assets/91626899/f2c4fa5b-3cd0-46f8-bc6c-2595af1b43c3">



 ## Model
 The model is a Deep Neural Network (DNN) implemented using Python and TensorFlow. It utilizes character n-grams to create distinct feature sets for different languages, and these features are used to classify the language of a given text input.

 To gain insights into the feature representation, we visualized the learned features of the model using techniques such as t-SNE and PCA.

 ## Performance
 The LinguaNet model achieved a final accuracy of 89.2%, highlighting its effectiveness in identifying and differentiating languages based on text input.

 ## Future Work
 We plan to refine the model further, aiming to increase its accuracy and expand its scope to include more languages. Contributions and feedback are welcome.

 ## License
 ```bash
 Copyright [2023] [Ritesh Chavan]

 Licensed under the Apache License, Version 2.0 (the "License");
 you may not use this file except in compliance with the License.
 You may obtain a copy of the License at

     http://www.apache.org/licenses/LICENSE-2.0

 Unless required by applicable law or agreed to in writing, software
 distributed under the License is distributed on an "AS IS" BASIS,
 WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
 See the License for the specific language governing permissions and
 limitations under the License.
 ```
