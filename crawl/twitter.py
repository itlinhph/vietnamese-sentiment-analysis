import TwitterAPI
import yaml

import utils


def fetch(api, resource, search_term, query):
    filename = '{0}/{1}.yaml'.format(resource.replace('/', '_'), search_term)

    utils.ensure_dir(filename)
    count = 0
    try:
        with open(filename, 'a') as output_file:
            r = TwitterAPI.TwitterPager(api, resource, query)

            for tweet in r.get_iterator():
                if not 'retweeted_status' in tweet and not ("Tôi đã thích video" or "Tôi đã thêm video") in tweet['text']:
                    yaml.dump([tweet['text']], output_file,
                                default_flow_style=False)
                    count += 1
                    print(count, tweet['text'])
    except KeyboardInterrupt:
        pass


def fetch_one(api, resource, search_term, query):
    filename = '{0}/{1}.yaml'.format(resource.replace('/', '_'), search_term)

    utils.ensure_dir(filename)

    r = api.request(resource, query)
    items = [item for item in r]

    with open(filename, 'w') as output_file:
        yaml.dump(items, output_file, default_flow_style=False)
