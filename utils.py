# # 800 - 2030
# list = []
# days = ["sat", "sun", "mon", "tue", "wed", "thu", "fri"]
# for day in days:
#     for i in range(800, 2040, 10):
#         if int(str(i)[-2:]) == 00 or int(str(i)[-2:]) == 30:
#             list.append(f"gen_avail_{day}___{i}")
# print(list)
available_field_options = ['gen_avail_sat___800', 'gen_avail_sat___830', 'gen_avail_sat___900', 'gen_avail_sat___930',
                           'gen_avail_sat___1000', 'gen_avail_sat___1030', 'gen_avail_sat___1100',
                           'gen_avail_sat___1130', 'gen_avail_sat___1200', 'gen_avail_sat___1230',
                           'gen_avail_sat___1300', 'gen_avail_sat___1330', 'gen_avail_sat___1400',
                           'gen_avail_sat___1430', 'gen_avail_sat___1500', 'gen_avail_sat___1530',
                           'gen_avail_sat___1600', 'gen_avail_sat___1630', 'gen_avail_sat___1700',
                           'gen_avail_sat___1730', 'gen_avail_sat___1800', 'gen_avail_sat___1830',
                           'gen_avail_sat___1900', 'gen_avail_sat___1930', 'gen_avail_sat___2000',
                           'gen_avail_sat___2030', 'gen_avail_sun___800', 'gen_avail_sun___830', 'gen_avail_sun___900',
                           'gen_avail_sun___930', 'gen_avail_sun___1000', 'gen_avail_sun___1030',
                           'gen_avail_sun___1100', 'gen_avail_sun___1130', 'gen_avail_sun___1200',
                           'gen_avail_sun___1230', 'gen_avail_sun___1300', 'gen_avail_sun___1330',
                           'gen_avail_sun___1400', 'gen_avail_sun___1430', 'gen_avail_sun___1500',
                           'gen_avail_sun___1530', 'gen_avail_sun___1600', 'gen_avail_sun___1630',
                           'gen_avail_sun___1700', 'gen_avail_sun___1730', 'gen_avail_sun___1800',
                           'gen_avail_sun___1830', 'gen_avail_sun___1900', 'gen_avail_sun___1930',
                           'gen_avail_sun___2000', 'gen_avail_sun___2030', 'gen_avail_mon___800', 'gen_avail_mon___830',
                           'gen_avail_mon___900', 'gen_avail_mon___930', 'gen_avail_mon___1000', 'gen_avail_mon___1030',
                           'gen_avail_mon___1100', 'gen_avail_mon___1130', 'gen_avail_mon___1200',
                           'gen_avail_mon___1230', 'gen_avail_mon___1300', 'gen_avail_mon___1330',
                           'gen_avail_mon___1400', 'gen_avail_mon___1430', 'gen_avail_mon___1500',
                           'gen_avail_mon___1530', 'gen_avail_mon___1600', 'gen_avail_mon___1630',
                           'gen_avail_mon___1700', 'gen_avail_mon___1730', 'gen_avail_mon___1800',
                           'gen_avail_mon___1830', 'gen_avail_mon___1900', 'gen_avail_mon___1930',
                           'gen_avail_mon___2000', 'gen_avail_mon___2030', 'gen_avail_tue___800', 'gen_avail_tue___830',
                           'gen_avail_tue___900', 'gen_avail_tue___930', 'gen_avail_tue___1000', 'gen_avail_tue___1030',
                           'gen_avail_tue___1100', 'gen_avail_tue___1130', 'gen_avail_tue___1200',
                           'gen_avail_tue___1230', 'gen_avail_tue___1300', 'gen_avail_tue___1330',
                           'gen_avail_tue___1400', 'gen_avail_tue___1430', 'gen_avail_tue___1500',
                           'gen_avail_tue___1530', 'gen_avail_tue___1600', 'gen_avail_tue___1630',
                           'gen_avail_tue___1700', 'gen_avail_tue___1730', 'gen_avail_tue___1800',
                           'gen_avail_tue___1830', 'gen_avail_tue___1900', 'gen_avail_tue___1930',
                           'gen_avail_tue___2000', 'gen_avail_tue___2030', 'gen_avail_wed___800', 'gen_avail_wed___830',
                           'gen_avail_wed___900', 'gen_avail_wed___930', 'gen_avail_wed___1000', 'gen_avail_wed___1030',
                           'gen_avail_wed___1100', 'gen_avail_wed___1130', 'gen_avail_wed___1200',
                           'gen_avail_wed___1230', 'gen_avail_wed___1300', 'gen_avail_wed___1330',
                           'gen_avail_wed___1400', 'gen_avail_wed___1430', 'gen_avail_wed___1500',
                           'gen_avail_wed___1530', 'gen_avail_wed___1600', 'gen_avail_wed___1630',
                           'gen_avail_wed___1700', 'gen_avail_wed___1730', 'gen_avail_wed___1800',
                           'gen_avail_wed___1830', 'gen_avail_wed___1900', 'gen_avail_wed___1930',
                           'gen_avail_wed___2000', 'gen_avail_wed___2030', 'gen_avail_thu___800', 'gen_avail_thu___830',
                           'gen_avail_thu___900', 'gen_avail_thu___930', 'gen_avail_thu___1000', 'gen_avail_thu___1030',
                           'gen_avail_thu___1100', 'gen_avail_thu___1130', 'gen_avail_thu___1200',
                           'gen_avail_thu___1230', 'gen_avail_thu___1300', 'gen_avail_thu___1330',
                           'gen_avail_thu___1400', 'gen_avail_thu___1430', 'gen_avail_thu___1500',
                           'gen_avail_thu___1530', 'gen_avail_thu___1600', 'gen_avail_thu___1630',
                           'gen_avail_thu___1700', 'gen_avail_thu___1730', 'gen_avail_thu___1800',
                           'gen_avail_thu___1830', 'gen_avail_thu___1900', 'gen_avail_thu___1930',
                           'gen_avail_thu___2000', 'gen_avail_thu___2030', 'gen_avail_fri___800', 'gen_avail_fri___830',
                           'gen_avail_fri___900', 'gen_avail_fri___930', 'gen_avail_fri___1000', 'gen_avail_fri___1030',
                           'gen_avail_fri___1100', 'gen_avail_fri___1130', 'gen_avail_fri___1200',
                           'gen_avail_fri___1230', 'gen_avail_fri___1300', 'gen_avail_fri___1330',
                           'gen_avail_fri___1400', 'gen_avail_fri___1430', 'gen_avail_fri___1500',
                           'gen_avail_fri___1530', 'gen_avail_fri___1600', 'gen_avail_fri___1630',
                           'gen_avail_fri___1700', 'gen_avail_fri___1730', 'gen_avail_fri___1800',
                           'gen_avail_fri___1830', 'gen_avail_fri___1900', 'gen_avail_fri___1930',
                           'gen_avail_fri___2000', 'gen_avail_fri___2030']
weekday_converter = {"mon": 0,
                     "tue": 1,
                     "wed": 2,
                     "thu": 3,
                     "fri": 4,
                     "sat": 5,
                     "sun": 6

}

timezone_converter = {
    "eastern": "US/Eastern",
    "central": "US/Central",
    "mountain": "US/Mountain",
    "western": "US/Pacific",
    "alaskan": "US/Alaska",
    "hawaiian": "US/Hawaii"
}

interviewer_email_converter = {
    "Hannah": "hmglenn@wisc.edu",
    "hannah": "hmglenn@wisc.edu",
    "Rachel": "rldyer@wisc.edu",
    "rachel": "rldyer@wisc.edu",
    "Camille": "cywilliams@wisc.edu",
    "camille": "cywilliams@wisc.edu",
    "Zoua": "zlor@wisc.edu",
    "zoua": "zlor@wisc.edu",
    "Zishan": "zjiwani@wisc.edu",
    "zishan": "zjiwani@wisc.edu",
    "Testing": "pskukreja@wisc.edu",
    "Sin" : "lam26@wisc.edu"
}