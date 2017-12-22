import argparse
import config

format_types = config.settings['formats']

parser: argparse.ArgumentParser = argparse.ArgumentParser(description='Twitch Chat Downloader')
parser.add_argument('-v', '--video', type=str, help='Video id', default='211636961')
parser.add_argument('--client_id', type=str, help='Twitch client id', default=None)
# parser.add_argument('--verbose', action='store_true')
# parser.add_argument('-q', '--quiet', action='store_true')
parser.add_argument('-o', '--output', type=str, help='Output folder', default='./')
parser.add_argument('-f', '--format', type=str, help='Message format', default='irc')
# parser.add_argument('--start', type=int, help='Start time in seconds from video start')
# parser.add_argument('--stop', type=int, help='Stop time in seconds from video start')
# parser.add_argument('--subtitle-duration', type=int, help='If using a subtitle format, subtitle duration in seconds')

arguments = parser.parse_args()

# Video ID
if arguments.video is None:
    answer: str = input('Video ID: ')
    arguments.video = answer.strip('v')

# Twitch client ID
if not config.settings['client_id'] and arguments.client_id is None:
    print('Twitch requires a client ID to use their API.'
          '\nRegister an application on https://dev.twitch.tv/dashboard to get yours.')
    config.settings['client_id'] = input('Client ID: ')
    answer: str = input('Save client ID? (Y/n): ')
    if answer.lower() != "n":
        config.save(config.SETTINGS_FILE, config.settings)
