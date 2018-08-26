# Calculate the daily retention curve for users who used the app 
# for the first time on the following dates: Feb 4th, and Feb 10th. 

from collections import defaultdict
import json

import matplotlib.pyplot as plt


DAYS_IN_MONTH = 28  # february
DATA_FILE = 'data/pings.txt'
SUBSAMPLE_FILE = 'data/minipings.json'  # subset of users
MAKE_SUBAMPLE = False
USE_SUBSAMPLE = True


def make_subsample(whole_file, subsample_file):
    """ subsample 1/100 into separate file """
    line_counter = 0
    with open(whole_file, 'r') as rf, open(subsample_file, 'w') as wf:
        for line_txt in rf:
            try:
                uid = json.loads(line_txt)['attributed_to']
                if uid[-1] == '0' and uid[-2] == '0': # 1/100
                    wf.write(line_txt)
            except:
                print('Error parsing line_txt:', line_txt)
            line_counter += 1
            if line_counter % 10 ** 6 == 0:
                print('read %dM lines' % (line_counter // 10 ** 6))
    

def parse_lines(filename):
    """ Generator that opens the file and parses its JSON lines. 
    Return tuple:
        user id (str), 
        days since feb 1 (int), 
        is install day (bool, False if missing), 
        first_utm_source (str, 'unknown' if missing).
    """
    line_counter = 0
    with open(filename, 'r') as rf:
        for line_txt in rf:
            try:
                d = json.loads(line_txt)
                tup = (
                    d['attributed_to'],
                    int(d['date_time'][8:10]),
                    d.get('used_first_time_today', False),
                    d.get('first_utm_source', 'unknown') 
                    )
            except:
                print('Error parsing line_txt:', line_txt)
            line_counter += 1
            if line_counter % 10 ** 6 == 0:
                print('read %dM lines' % (line_counter // 10 ** 6))
            yield tup  # yield: https://stackoverflow.com/a/231855
    
    
def main():
    users_days = defaultdict(set)  # map user to days seen 
    users_referrals = {}  # map user to referral of first visit
    cohorts = defaultdict(set)  # map day to users born that day
      
    # make subsample
    if MAKE_SUBAMPLE:
        make_subsample(DATA_FILE, SUBSAMPLE_FILE)
          
    # parse the whole file
    filename = SUBSAMPLE_FILE if USE_SUBSAMPLE else DATA_FILE
    print('parsing file %s' % filename)
    for (uid, day, isnew, referral) in parse_lines(filename):
        users_days[uid].add(day)  # TODO: bitmask instead of set? days[uid] |= 1 << day
        if isnew:
            users_referrals[uid] = referral
            cohorts[day].add(uid)
      
    # compute d1-d14 retention for 2 cohorts
    print('computing retention')
    rets = {}
    for bday in [4, 10]:
        users_seen = [0 for _ in range(14 + 1)]  # from bday to bday + 14 days
        for uid in cohorts[bday]:
            for dayofmonth in users_days[uid]:
                if dayofmonth <= bday + 14:
                    users_seen[dayofmonth - bday] += 1
        ret = [n * 1.0 / users_seen[0] for n in users_seen]
        rets[bday] = ret
    
    # plot
    for bday, ret in rets.items():
        plt.plot(range(len(ret)), ret, label=('Feb %d cohort ' % bday))
    plt.xlabel('days since birth')
    plt.ylabel('% of cohort still using product')
    plt.grid(True)
    plt.legend()
    plt.show()
    
    
    
if __name__ == "__main__":
    main()
