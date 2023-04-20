# Telegram Bot with ChatGPT connector

Requirements:
* docker
* python310

Keep in mind -> There are two variables you must set as system variables or provide them directly in `build.py` \
`TGBOT_KEY` - is your Telegram Bot API key\
`GPT_KEY` - your ChatGPT API key 

## Build your image:
```py build.py bot-image``` \
or \
```py build.py --tgbot-key 'you_tgbot_api_key_here' --gpt-key 'you_gpt_api_key_here' bot-image ```

## Build and push into the Docker Hub:
```py build.py -m push user123/bot-image```
