import TwitterAPI

import settings
import twitter


def main():
    api = TwitterAPI.TwitterAPI(** settings.get_app_settings())

    twitter.fetch(api, 'search/tweets', 'coccoc', {'q': 'kenh14'})


if __name__ == '__main__':
    main()
