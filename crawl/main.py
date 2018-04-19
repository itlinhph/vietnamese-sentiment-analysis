import TwitterAPI

import settings
import twitter


def main():
    api = TwitterAPI.TwitterAPI(** settings.get_app_settings())

    # twitter.fetch(api, 'search/tweets', 'input', {'q': 'coccoc', 'lang': 'vi'})
    # twitter.fetch(api, 'search/tweets', 'input', {'q': '#coccoc', 'lang': 'vi'})
    # twitter.fetch(api, 'search/tweets', 'input', {'q': 'cntt', 'lang': 'vi'})
    # twitter.fetch(api, 'search/tweets', 'input', {'q': 'ifan', 'lang': 'vi'})
    # twitter.fetch(api, 'search/tweets', 'input', {'q': 'yêu', 'lang': 'vi'})
    twitter.fetch(api, 'search/tweets', 'input', {'q': 'ghét', 'lang': 'vi'})


if __name__ == '__main__':
    main()

#1. coc coc
#2. ifan
#3. cntt
#4. yêu, ghét