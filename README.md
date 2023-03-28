# Phonotactics

 

This folder includes the codes for hosting the phonotactics experiment on firebase and generating audio stimuli from IPA through Amazon Polly. A Demo can be played here: https://scarlettwwx.github.io/ 

  
## Installation

  

Before you start running the codes you need to set up an account on Amazon Web Server, and obtain your `aws_access_key_id` and `aws_secret_access_key`. You will need these two for generating speech from text with Amazon Polly. We will need to use `boto3` , an Amazon Web Services (AWS) SDK for Python, to synthesize the audios. Use the package manager pip to install boto3.  
```bash
pip install boto3
```
To see more details go to [Amazon Polly]([https://aws.amazon.com/polly/](https://aws.amazon.com/polly/)). 

Other package that you might need to install is [ipapy]([https://pypi.org/project/ipapy/0.0.1.0/](https://pypi.org/project/ipapy/0.0.1.0/)). 
```bash
pip install ipapy
```
You will also need to register an account on [Firebase]([https://firebase.google.com/](https://firebase.google.com/)). This is the platform that we will be using for hosting our experiment. For step-by-step walkthroughs help you get started using Firebase, please consult the documentation. 
  
 

## Audio Generation Guide

1. Format list of IPA that you wish to synthesize to the correct [Speech Synthesis Markup Language (SSML)]([https://docs.aws.amazon.com/polly/latest/dg/ssml.html](https://docs.aws.amazon.com/polly/latest/dg/ssml.html)) that will gives us the desired audio output.  This is because we are creating sound files for nonce words, and we need to specify their phonetic pronunciations, which is done by using the **\<phoneme>** tag
Take a real English word that can be pronounced in different ways for example, for the word *pecan* you can get the two pronunciations by inputting the following SSML: 
```python
<speak>
	 You say, <phoneme alphabet="ipa" ph="pɪˈkɑːn">pecan</phoneme>. 
	 I say, <phoneme alphabet="ipa" ph="ˈpi.kæn">pecan</phoneme>. 
</speak>
```
This conversion from IPA to SSML is done by a simple python script `pollysciprtipa.py` in the folder **stimuli**, and the list of SSML is saved in the text file `1000_Polly.txt`

2. After obtaining the list of SSML `1000_Polly`,  use the python script `synthesizeSpeech.py` in the folder **stimuli** to generate the audio files. This is readily provided by Amazon Polly. It requires you to fill in your `aws_access_key_id` and `aws_secret_access_key`, so make sure you have them ready. Note that the IPAs are ordered in the original list,  the audio files are named with the indexes of their corresponding IPAs. 
3. After obtaining the audio files, generate a stimulus list `1000stimlist.js` using the python script `simlist_generator.py`. The JSON file is a dictionary with stings to be displayed as values and addresses of the corresponding audios as keys. We need this file to preload the audio files faster.  The file is moved to be under the folder `1000stimlist.js`
	> **_NOTE:_**  The file  `1000stimlist.js`  is moved to be under the folder js in **static**

In the next step we play to replace strings to be displayed by the proposed spellings of the nonce words. What needs to be done is when generating the stimuli list, change the values in the dictionary to be the spellings. 

## Hosting Experiment Locally

Firebase has a very detailed documentation with YouTube videos on how to set up a server. Please see [Firebase Hosting]([https://firebase.google.com/docs/hosting](https://firebase.google.com/docs/hosting)) .

The configuration at initialization used previously was 
![image info](https://phonotactics.s3.ca-central-1.amazonaws.com/Screen+Shot+2020-05-10+at+1.58.06+AM.png)

Firebase has an option to test the experiment locally for debugging before you officially.  A previous version of this experiment can be viewed [here]([https://phonotactics-5b847.firebaseapp.com/](https://phonotactics-5b847.firebaseapp.com/))

You can also directly open the experiment HTML in a browser such as chrome, but you might need to [disable the same origin policy Chrome] (https://stackoverflow.com/questions/3102819/disable-same-origin-policy-in-chrome). 
  

## Miscellaneous
* The results previous data exploration and preprocessing are stored in the folder **scores**, and the raw stimuli and scores are stored in a dropbox folder by Vanna due to the sizes of the files. 
* We initially wanted to directly host the experiment through [psiTurk]([https://psiturk.org/](https://psiturk.org/)) instead of using the GUIs provided by Amazon, for which the manipulation of the pipeline can be cumbersome.  PsiTurk can be used as a wrapper that communicate with Amazon Turk. The setup of the psiTurk relatively more complicated, and we were having connectivity issues with the web server on psiTurk. So, we decided to go with a template on MTurk that could take the participants to a web server hosted by us and verify payments through identification codes. The previous version of the the experiment is available at [Seara Chen's gitHub](https://github.com/SearaChen/productivity_psiturk_experiment). 
