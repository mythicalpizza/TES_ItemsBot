import config
import forge
from log import FatalLoggingException, FileLogger, NullLogger
from sites import SocialMediaSitePostingException, SocialMediaSiteCredentialsException, Twitter, BlueSky
from os import getenv


def main():
    # Get a bunch of env vars for running / testing locally. Default to the hardcoded paths so everything
    # works the same way in prod
    about_file = getenv("ABOUT_FILE", "about.json")
    flags_file = getenv("FLAGS_FILE", "flags.json")
    twitter_credentials_file = getenv("TWITTER_CREDENTIALS_FILE", "../../credentials/twitter.json")
    bluesky_credentials_file = getenv("BLUESKY_CREDENTIALS_FILE", "../../credentials/bluesky.json")
    log_dir = getenv("LOG_DIR", "logs")
    log_file = getenv("LOG_FILE", "teslog.txt")

    flags = config.get_json(flags_file)

    if not config.is_disabled(flags["logs"]):
        try:
            logger = FileLogger(directory=log_dir, filename=log_file)
        except FatalLoggingException:
            logger = NullLogger()
            logger.create_entry("Could not create log file, using NullLogger")
    else:
        logger = NullLogger()

    item = forge.item() if not config.is_disabled(flags['crosspostingconstraint']) else None

    try:
        twitter = Twitter(twitter_credentials_file)
        twitter.items_bot_post(item)
    except (SocialMediaSiteCredentialsException, SocialMediaSitePostingException) as e:
        logger.handle_error(e, "Twitter Error")
    try:
        bluesky = BlueSky(bluesky_credentials_file)
        bluesky.items_bot_post(item)
    except (SocialMediaSiteCredentialsException, SocialMediaSitePostingException) as e:
        logger.handle_error(e, "BlueSky Error")


if __name__ == "__main__":
    main()
