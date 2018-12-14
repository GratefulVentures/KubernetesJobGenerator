import argparse
from datetime import date, timedelta

import yaml


def main(tool, report_type):
    if tool.lower() in ['google_analytics', 'analytics', 'ga', 'googleanalytics', 'google-analytics']:
        tool = 'ga'
    elif tool.lower() in ['ad-manager', 'admanager', 'am', 'ad-manager', 'gam']:
        tool = 'ad-manager'

    with open('job.yaml', 'r') as jobs:
        test = yaml.load(jobs)

    d1 = date(2018, 1, 1)  # start date
    d2 = date.today()  # end date

    delta = d2 - d1  # timedelta

    for i in range(delta.days + 1):
        start_date = d1 + timedelta(i)

        test['metadata']['name'] = f'{tool}-{report_type}-{start_date}'
        test['spec']['template']['metadata']['name'] = f'{tool}-{report_type}-{start_date}'
        test['spec']['template']['spec']['containers'][0]['args'][2] = start_date
        test['spec']['template']['spec']['containers'][0]['name'] = f'{tool}-{report_type}-{start_date}'

        with open(f'./{tool}/{report_type}/{tool}-{report_type}-{str(start_date)}.yaml', 'w') as outfile:
            yaml.dump(test, outfile)


if __name__ == '__main__':
    arg_parser = argparse.ArgumentParser()
    arg_parser.add_argument('tool', help='ad-manager or ga')
    arg_parser.add_argument('report_type', help='hourly, daily, bid-landscape(only for ad manager)')
    args = arg_parser.parse_args()

    main(args.tool, args.report_type)
