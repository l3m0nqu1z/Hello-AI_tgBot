import os, argparse, logging, subprocess

logging.basicConfig(format='%(levelname)s - %(message)s',
                    level=logging.INFO)

parser = argparse.ArgumentParser()
parser.add_argument('name', help="how you want to call you image")
parser.add_argument('-m', '--method', help="do docker push after build or not",
                    choices=["push", "buildonly"], default="buildonly")
parser.add_argument('--tgbot-key', help="your Telegram bot API key")
parser.add_argument('--gpt-key', help="your GPT API key")
args = parser.parse_args()

try:
    TGBOT_KEY = os.environ['TGBOT_KEY'] if args.tgbot_key is None else args.tgbot_key
except Exception:
    logging.info('TGBOT_KEY isn\'t defined. Setting to None')
    TGBOT_KEY = None

try:
    GPT_KEY = os.environ['GPT_KEY'] if args.gpt_key is None else args.gpt_key
except Exception:
    logging.info('GPT_KEY isn\'t defined. Setting to None')
    GPT_KEY = None


subprocess.run(["docker", "build", "-t", args.name, ".", "--build-arg", f"TGBOT_KEY={TGBOT_KEY}", "--build-arg", f"GPT_KEY={GPT_KEY}"]) 
if args.method is "push":
    subprocess.run(["docker", "push", args.name])
