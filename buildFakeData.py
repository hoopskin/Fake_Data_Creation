import csv, random, datetime
from faker import Faker

#Currently not used. buildRandomDate could be improved to utilize these.
companyStartDate = datetime.datetime.strptime("2015-01-01", "%Y-%m-%d")
companyEndDate = datetime.datetime.strptime("2019-12-31", "%Y-%m-%d")
hiringStartDate = companyStartDate
hiringEndDate = companyEndDate


fake = Faker()

#If needed for consistency
#fake.seed_instance(42)
#random.seed(42)

appCatList, devSteps, engagementRoleList, projNameList, regionList, revenueSourceList = [], [], [], [], [], []

def buildManualLists(appsToBuild, folder="manualLists/"):
    global appCatList, devSteps, engagementRoleList, projNameList, regionList, revenueSourceList
    #appCatList
    appCatList = [v.strip() for v in open(folder+"appCategoryList.txt", "rt")]

    #devSteps
    devSteps = [v.strip() for v in open(folder+"developmentSteps.txt", "rt")]

    #engagementRoleList
    engagementRoleList = [v.strip() for v in open(folder+"engagementRoleList.txt", "rt")]

    #regionList
    regionList = [v.strip() for v in open(folder+"regionList.txt", "rt")]

    #revenueSourceList
    revenueSourceList = [v.strip() for v in open(folder+"revenueSources.txt", "rt")]

    #projNameList
    #Just in case a number larger than our list is picked, extend it with slug
    projNameList = [v.strip() for v in open(folder+"projectNameList.txt", "rt")]
    if appsToBuild > len(projNameList):
        projNameList.extend([fake.slug().title() for _ in range(appsToBuild-len(projNameList))])

def guessExpectedRevenue(region, appCategory, revenueSource, baseMu=100000, baseSigma=10000):
    muMultiplier = 1
    sigmaMultiplier = 1

    regionMuDict = {"Worldwide": 0.25, "USA": 0, "Europe": -0.25, "China": 0.5}

    appCatMuDict = {"Business": 0, "Food & Drink": -0.25, "Health & Fitness": 0, \
                    "Photo & Video": 0.25, "Shopping": 0, "Social Networking": 0.25, \
                    "Games": 0.50}

    revSrcMuDict = {"In-App Ads": 0.5, "In-App Ads with Paid Ability to Remove Ads": .55, \
                    "Paid App": .25, "Subscription - Daily": -0.5, \
                    "Subscription - Weekly": 0, "Subscription - Monthly": 0.25, \
                    "Subscription - Yearly": 0}


    regionSigmaDict = {"Worldwide": -0.1, "USA": 0.25, "Europe": -0.25, "China": -0.5}

    appCatSigmaDict = {"Business": -0.5, "Food & Drink": 0.5, "Health & Fitness": -0.25, \
                    "Photo & Video": 0.75, "Shopping": -0.75, "Social Networking": -0.25, \
                    "Games": 0}

    revSrcSigmaDict = {"In-App Ads": -0.5, "In-App Ads with Paid Ability to Remove Ads": -0.45, \
                    "Paid App": -0.25, "Subscription - Daily": 0.75, \
                    "Subscription - Weekly": 0, "Subscription - Monthly": -0.25, \
                    "Subscription - Yearly": 0}

    for option, optionDict in zip([region, appCategory, revenueSource], [regionMuDict, appCatMuDict, revSrcMuDict]):
        muMultiplier += optionDict[option]

    for option, optionDict in zip([region, appCategory, revenueSource], [regionSigmaDict, appCatSigmaDict, revSrcSigmaDict]):
        sigmaMultiplier += optionDict[option]


    return int(random.normalvariate(baseMu*muMultiplier, baseSigma*sigmaMultiplier))

def buildRandomDate(initialSeedDev=False, years=[2015, 2016, 2017, 2018, 2019], weights=[13,15,18,23,31]):
    if initialSeedDev:
        return "%i-01-01" % (years[0])
    year = random.choices(years, weights=weights)[0]

    #If run in a leap year, there's a small (1/366) chance that you try
    #to convert Feb. 29th to a non-Leap Year year. In that case, just get a new date.
    while True:
        randDT = fake.date_this_year(before_today=True, after_today=True)
        try:
            dt = datetime.date(year,randDT.month, randDT.day)
            break
        except(ValueError):
            continue

    return datetime.datetime.strftime(dt, "%Y-%m-%d")

def buildDevelopers(numToMake=60):
    #fake.csv(header=None, data_columns=('{{name}}', '{{address}}'), num_rows=10, include_row_ids=False)
    #fake.profile(fields=None, sex=None)
    devHeader = ["Dev_ID", "First Name", "Last Name", "Home State", \
                "Employment Start Date", "Username", "Email", "DOB"]

    devData = []
    for i in range(numToMake):
        developerID = i+1
        dev_fn = fake.first_name()
        dev_ln = fake.last_name()
        dev_st = fake.state()
        #dev_start_date = fake.date_between_dates(hiringStartDate, hiringEndDate)
        #What if we use the same function as app dates so the build up is similar?
        if i < 6:
            dev_start_date = buildRandomDate(initialSeedDev=True)
        else:
            dev_start_date = buildRandomDate()
        dev_un = fake.user_name()
        dev_mail = fake.safe_email()
        dev_dob = fake.date_of_birth(tzinfo=None, minimum_age=18, maximum_age=45)

        oRow = [developerID, dev_fn, dev_ln, dev_st, dev_start_date, dev_un, dev_mail, dev_dob]
        devData.append(oRow)

    writer = csv.writer(open("_developers.csv", "wt"), lineterminator='\n')
    writer.writerow(devHeader)
    writer.writerows(devData)

def buildApps(appsToBuild=300):
    appHeader = ["App_ID", "In Development Name", "Marketed Name", \
                "Region", "Category", "Expected Revenue Source", \
                "Expected Revenue Amount", "Current Development Step", \
                "Development Start Date", "Current Cost"]

    appData = []

    for i in range(appsToBuild):
        appId = i+1
        inDevName = projNameList[i]

        #NOTE: Choices allows for weights. [0] Necessary since it returns a list
        region = random.choices(regionList, weights=[50,25,20,5])[0]

        #Are there any Category / Rev Source combos we want to stop?
        appCat = random.choice(appCatList)
        revSrc = random.choice(revenueSourceList)
        expRevAmt = guessExpectedRevenue(region, appCat, revSrc)

        #TODO: Should we weight these so we can see a bottleneck?
        curDevStep = random.choice(devSteps)

        marketName = ""
        if devSteps.index(curDevStep) >= devSteps.index("Marketing"):
            marketName = random.choice(projNameList).lower()
            for vowel in ["a", "e", "i", "o", "u"]:
                marketName = marketName.replace(vowel,"")
                marketName = marketName.title()

        startDate = buildRandomDate()

        #TODO: Improve this. Currently $/Day * Step in Process * Random Number of Days
        #TODO: May want to build a Seed $ ROI so we may need to complicate this. Turn certain things into "golden eggs"?
        #Having 0 cost is ok. Maybe some contracts cause no add'l cost
        cost = random.randint(0,5)*devSteps.index(curDevStep)*random.randint(1,365*4)

        oRow = [appId, inDevName, marketName, region, appCat, revSrc, expRevAmt, \
                curDevStep, startDate, cost]
        appData.append(oRow)

    writer = csv.writer(open("_apps.csv", "wt"), lineterminator='\n')
    writer.writerow(appHeader)
    writer.writerows(appData)

def buildEngagements(appsToBuild):
    engagementHeader = ["Engagement ID", "Dev_ID", "App_ID"]

    devData = list(csv.reader(open("_developers.csv", "rt")))
    devHeader = devData[0]

    appData = list(csv.reader(open("_apps.csv", "rt")))
    appHeader = appData[0]

    engagementData = []
    for appId in range(1, appsToBuild+1):
        appRow = [row for row in appData if row[appHeader.index("App_ID")] == str(appId)][0]
        appStartDate = appRow[appHeader.index("Development Start Date")]
        potentialDevs = [row[devHeader.index("Dev_ID")] for row in devData if row[devHeader.index("Employment Start Date")] <= appStartDate]

        #Pick 1-5 devs. Unless there are < 5 devs, then 1-All Devs
        devsToEngage = random.choices(potentialDevs, k=random.randint(1,min(5,len(potentialDevs))))

        for devId in devsToEngage:
            engagementData.append([len(engagementData)+1,appId,devId])

    writer = csv.writer(open("_engagements.csv", "wt"), lineterminator='\n')
    writer.writerow(engagementHeader)
    writer.writerows(engagementData)

def addDeveloperBonuses(devsBonusToBuildCount):
    #TODO: This will basically randomly pick X developers and bonus anything they touch
    pass

def developerEngagementBeforeHire(devEngagementModCount):
    #TODO: We'll take X developers and mess with an engagement to be before their hire date
    pass

def centuryDateMessup(appCenturyMessupCount):
    #TODO: We'll take X apps and move their start date to 19xx
    pass

def extraZeroesIncome(extraZeroesAppCount):
    #TODO: We'll take X apps with a realized revenue and mess with their value to add 2 or 3 zeroes
    pass



def dirtyTheData(devEngagementModCount, appCenturyMessupCount, extraZeroesAppCount):
    #TODO: Here is where we're going to mess with / break some of the data
    developerEngagementBeforeHire(devEngagementModCount)
    centuryDateMessup(appCenturyMessupCount)
    extraZeroesIncome(extraZeroesAppCount)

def main(devsToBuild=60, devsPerAppMultiplier=5, appsToBuildOverride=None):
    if appsToBuildOverride == None:
        appsToBuild = devsToBuild*devsPerAppMultiplier
    else:
        appsToBuild = appsToBuildOverride
    buildManualLists(appsToBuild)
    buildDevelopers(devsToBuild)
    buildApps(appsToBuild)
    buildEngagements(appsToBuild)
    addDeveloperBonuses(devsToBuild//10)
    dirtyTheData(devsToBuild//20, appsToBuild//20//5, appsToBuild//20//5)

main()
