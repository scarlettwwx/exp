import boto3
import os

'''
polly_client = boto3.Session(
    aws_access_key_id= 'AKIAJU2KLWD4O3UAM62A',
    aws_secret_access_key= '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',
    region_name='us-west-2').client('polly')

f= open("/Users/xuwenwen/OneDrive - McGill University/static/stimuli/1000_Polly.txt","r")
count = 0
for line in f :
    response = polly_client.synthesize_speech(VoiceId='Joanna',
                OutputFormat='mp3',
                Text = line,
                TextType = 'ssml')
    file = open(str(count)+'.mp3', 'wb')
    file.write(response['AudioStream'].read())
    file.close()
    count = count +1
'''


