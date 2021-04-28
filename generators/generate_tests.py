import re
import random
import csv
import string
# time_count = {}
#
# I/O and For-loop used to extract data from dataset containing data on GitHub commits
# with open("full.csv", "r") as file:
#     for row in file.readlines():
#         match = re.search("[0-9][0-9]+:[0-9][0-9]:[0-9][0-9]",row)
#         if match:
#             print(match.group(0))
#             entry = match.group(0)[:5]
#             if entry in time_count:
#                 print("Time found in dictionary, incrementing")
#                 time_count[entry] += 1
#             else:
#                 print("Time not found, adding entry")
#                 time_count[entry] = 1
#
# print(time_count)
# Results from the GitHub dataset extraction
result = {'12:27': 3444, '01:23': 2141, '01:21': 2134, '01:01': 2688, '23:58': 2785, '15:56': 4797, '15:55': 5011, '15:54': 4892, '00:51': 2450, '00:50': 2445, '00:49': 2479, '15:48': 4735, '00:47': 2405, '06:12': 1345, '08:52': 2331, '09:56': 3237, '16:21': 5019, '20:38': 3239, '11:54': 3882, '22:52': 3367, '09:23': 2811, '07:10': 1450, '16:02': 4529, '07:01': 1401, '15:00': 4726, '06:53': 1362, '06:51': 1490, '06:41': 1413, '06:38': 1343, '17:55': 4476, '12:08': 3571, '12:02': 3529, '20:42': 3530, '18:43': 3809, '17:54': 4266, '18:24': 4043, '18:14': 4078, '11:57': 3886, '18:11': 4228, '18:09': 4383, '18:07': 4140, '02:06': 1664, '02:03': 1947, '02:46': 1495, '17:21': 4651, '18:49': 3940, '19:49': 3551, '18:27': 3953, '20:27': 3463, '10:31': 3684, '10:56': 3857, '09:50': 3155, '06:16': 1380, '07:25': 1520, '16:12': 4795, '06:05': 1285, '06:04': 1342, '05:58': 1369, '05:56': 1236, '08:55': 2503, '05:53': 1239, '01:22': 2123, '01:19': 2138, '13:55': 4083, '10:16': 3438, '13:12': 3602, '11:50': 3822, '17:26': 4638, '08:25': 2144, '08:24': 2081, '07:17': 1711, '16:16': 4723, '16:15': 4936, '16:09': 4698, '06:21': 1361, '13:31': 3959, '14:24': 4405, '13:13': 3747, '13:53': 3950, '04:36': 1215, '20:29': 3708, '16:49': 5040, '16:41': 4733, '10:27': 3342, '15:31': 4620, '14:35': 4397, '13:17': 3564, '12:56': 3661, '09:25': 2982, '09:11': 2736, '18:32': 3920, '15:01': 4719, '08:39': 2325, '02:02': 2352, '18:25': 3945, '17:20': 4692, '20:46': 3458, '12:42': 3455, '18:29': 4104, '18:28': 3820, '10:51': 3784, '08:45': 2226, '08:53': 2539, '20:33': 3581, '02:41': 1516, '04:40': 1248, '01:52': 1856, '19:04': 3747, '00:16': 6911, '00:15': 2811, '13:16': 3615, '15:43': 4699, '21:36': 3656, '06:40': 1323, '05:55': 1229, '05:47': 1363, '05:46': 1302, '05:26': 1261, '17:53': 4322, '13:47': 3886, '13:02': 3460, '13:00': 3365, '15:45': 4827, '12:44': 3400, '17:39': 4394, '15:44': 4817, '21:18': 3550, '23:38': 3044, '21:21': 3743, '21:04': 3661, '21:03': 3408, '20:55': 3445, '13:18': 3683, '09:22': 2955, '09:19': 2757, '16:24': 4735, '07:56': 1762, '06:09': 1345, '14:08': 4301, '22:57': 3319, '19:07': 3643, '11:49': 3900, '08:35': 2117, '18:41': 4066, '23:37': 2976, '13:20': 3621, '21:09': 3764, '11:18': 3947, '19:15': 3517, '08:18': 1963, '16:11': 4936, '17:09': 4784, '15:50': 4663, '18:52': 3782, '18:51': 3869, '18:47': 3739, '18:37': 3935, '17:50': 4585, '15:36': 4808, '15:35': 4686, '00:28': 2478, '23:24': 3081, '20:17': 3213, '11:55': 3727, '09:15': 2663, '09:12': 2662, '05:57': 1219, '05:52': 1255, '20:36': 3584, '18:05': 4143, '18:03': 4384, '18:02': 4270, '18:01': 4226, '14:21': 4330, '23:18': 3169, '15:57': 4904, '06:17': 1291, '09:17': 2674, '06:13': 1339, '05:51': 1378, '19:27': 3831, '11:41': 3919, '11:28': 3911, '17:24': 4581, '07:55': 1814, '07:42': 1703, '10:21': 3397, '14:52': 4622, '14:50': 4655, '06:27': 1343, '22:46': 3382, '17:46': 4485, '23:03': 3212, '10:46': 3841, '09:36': 2919, '06:10': 1369, '09:28': 2910, '18:53': 3836, '21:51': 3703, '20:09': 3609, '19:37': 3482, '00:13': 2766, '16:10': 4906, '15:23': 4791, '14:06': 4227, '15:08': 4972, '08:28': 2111, '16:31': 4956, '16:30': 4924, '16:29': 4951, '13:28': 3926, '11:02': 3679, '11:01': 3747, '17:47': 4449, '09:47': 3124, '09:35': 2957, '16:23': 4794, '17:14': 4666, '17:13': 4659, '19:12': 3586, '12:11': 3423, '12:10': 3391, '17:08': 4729, '11:17': 3968, '08:16': 2056, '14:46': 4512, '01:33': 1983, '21:24': 3518, '18:06': 4278, '07:32': 1642, '06:11': 1341, '13:08': 3534, '06:07': 1346, '06:03': 1455, '13:59': 4069, '05:43': 1320, '10:49': 3922, '17:12': 4783, '22:08': 3509, '17:01': 4784, '17:00': 4955, '08:41': 2158, '19:34': 3388, '18:18': 4109, '02:17': 1741, '02:15': 1735, '02:14': 1928, '18:10': 4198, '18:15': 4238, '17:51': 4691, '09:46': 3153, '14:47': 4597, '11:09': 4102, '02:01': 2073, '08:40': 2210, '17:17': 4609, '22:10': 3540, '21:08': 3926, '03:39': 1331, '03:05': 1489, '03:00': 1427, '08:22': 1937, '17:02': 4684, '14:31': 4379, '13:30': 4037, '12:52': 3658, '09:59': 3509, '09:55': 3215, '08:36': 2236, '08:32': 2168, '15:34': 4873, '06:49': 1522, '06:48': 1426, '06:18': 1321, '12:14': 3678, '11:59': 3719, '11:32': 3954, '16:14': 4850, '15:05': 4788, '22:00': 3695, '04:35': 1252, '00:44': 2417, '17:52': 4418, '01:30': 2067, '01:04': 2269, '17:03': 4718, '19:55': 3502, '16:45': 4970, '00:43': 2437, '16:43': 4943, '16:42': 4767, '16:33': 4787, '15:47': 4809, '01:58': 1789, '10:55': 4073, '15:42': 4830, '05:34': 1271, '14:33': 4345, '22:07': 3643, '23:06': 3262, '23:05': 3198, '22:48': 3303, '17:10': 4966, '14:10': 4004, '01:03': 2557, '02:33': 1680, '16:25': 4721, '02:04': 1871, '00:33': 2631, '19:17': 3349, '11:11': 3799, '01:38': 2050, '01:27': 2235, '13:44': 4050, '08:54': 2374, '05:13': 1255, '11:26': 4160, '10:50': 3686, '14:28': 4599, '02:50': 1459, '14:14': 4277, '14:07': 4201, '16:06': 4505, '12:17': 3473, '09:05': 2396, '05:32': 1238, '17:36': 4630, '10:11': 3423, '17:11': 4785, '07:59': 1827, '15:32': 4629, '09:31': 2886, '14:29': 4518, '14:23': 4336, '05:27': 1221, '14:13': 4049, '14:04': 3919, '05:00': 1243, '20:12': 3469, '00:29': 2696, '16:37': 4739, '22:39': 3455, '20:40': 3608, '12:50': 3555, '17:48': 4483, '10:38': 3660, '19:01': 3557, '23:07': 3258, '22:34': 3597, '19:00': 3548, '17:35': 4371, '06:22': 1466, '08:02': 1862, '08:17': 2047, '14:16': 4135, '09:29': 3020, '20:28': 3564, '02:36': 1621, '17:34': 4493, '02:32': 1599, '02:31': 1583, '17:29': 4657, '01:28': 2259, '01:09': 2297, '01:55': 1863, '00:39': 2608, '19:09': 3613, '17:45': 4510, '21:53': 3723, '16:28': 4993, '20:02': 3554, '12:57': 3650, '19:26': 3472, '19:24': 3596, '21:22': 3512, '03:01': 1414, '20:45': 3407, '10:41': 3671, '05:09': 1307, '05:08': 1337, '05:07': 1209, '05:06': 1224, '09:38': 3012, '20:04': 3486, '22:06': 3422, '19:05': 3777, '15:25': 4865, '00:21': 2579, '13:14': 3496, '09:27': 2902, '18:26': 4031, '18:23': 4000, '18:22': 3982, '16:51': 4833, '12:26': 3559, '00:10': 2976, '07:30': 1719, '15:10': 4680, '13:41': 3904, '19:32': 3500, '11:27': 3965, '07:14': 1399, '14:37': 4540, '22:54': 3391, '14:51': 4516, '05:44': 1312, '00:38': 2621, '20:44': 3575, '11:15': 3848, '11:14': 3969, '03:10': 1499, '11:08': 3809, '10:59': 4088, '10:34': 3710, '10:33': 3797, '00:01': 2698, '10:24': 3610, '10:23': 3703, '12:15': 3560, '10:13': 3232, '19:58': 3362, '16:00': 4898, '23:53': 2972, '23:11': 3105, '15:09': 4695, '14:26': 4436, '14:25': 4515, '19:16': 3453, '06:46': 1549, '06:45': 1410, '06:44': 1421, '15:22': 4640, '14:54': 4793, '05:40': 1252, '22:05': 3599, '16:54': 4824, '16:46': 5196, '19:42': 3457, '16:40': 4795, '01:39': 2064, '16:38': 4952, '16:36': 4820, '21:45': 3571, '00:53': 2444, '00:25': 2643, '10:09': 3431, '10:08': 3353, '13:05': 3454, '18:55': 3676, '09:52': 3276, '11:03': 3720, '11:39': 3825, '13:36': 3944, '06:26': 1371, '19:39': 3424, '01:37': 2119, '19:19': 3462, '05:25': 1245, '11:13': 3887, '03:25': 1306, '18:54': 3689, '05:21': 1216, '16:20': 5228, '00:00': 3823, '23:59': 2927, '14:58': 4888, '14:57': 4605, '23:30': 3050, '13:25': 3742, '05:22': 1257, '10:14': 3282, '19:03': 3610, '12:33': 3379, '12:32': 3486, '09:26': 2911, '09:21': 2774, '09:20': 2835, '09:18': 2755, '09:16': 2784, '23:46': 3041, '10:32': 3492, '01:11': 2157, '02:10': 1684, '17:04': 4855, '20:50': 3407, '14:56': 4570, '12:09': 3583, '10:37': 3535, '17:33': 4366, '20:30': 3557, '01:16': 2260, '00:58': 2364, '18:35': 3966, '15:26': 4929, '18:08': 4194, '23:55': 2803, '14:55': 4558, '18:34': 3892, '08:59': 2612, '15:41': 4846, '13:52': 4218, '03:51': 1242, '16:19': 4684, '15:53': 4765, '15:52': 4995, '18:50': 3809, '15:49': 4946, '16:32': 4733, '18:20': 4073, '14:43': 4477, '23:42': 2843, '17:37': 4544, '22:31': 3344, '14:17': 4320, '14:15': 4196, '20:06': 3436, '18:17': 3946, '23:43': 2991, '02:16': 1872, '21:33': 3503, '12:13': 3470, '12:12': 3576, '18:45': 4091, '09:40': 3008, '11:37': 3958, '04:04': 1344, '17:27': 4628, '17:22': 4656, '08:43': 2318, '08:42': 2291, '13:40': 3866, '02:43': 1552, '00:48': 2325, '15:13': 4602, '12:35': 3388, '10:43': 3618, '18:58': 3580, '15:40': 4532, '15:29': 4930, '01:57': 1813, '12:41': 3487, '00:20': 2670, '14:45': 4724, '14:44': 4436, '16:47': 4880, '11:36': 4052, '05:50': 1261, '05:49': 1486, '14:42': 4657, '13:39': 3954, '10:02': 3244, '15:16': 4825, '12:28': 3374, '18:12': 4231, '08:58': 2569, '16:44': 5074, '17:42': 4448, '16:35': 4753, '11:24': 4145, '12:24': 3690, '17:41': 4439, '09:53': 3202, '22:15': 3530, '19:11': 3708, '14:40': 4687, '16:55': 4925, '07:12': 1458, '17:59': 4537, '02:52': 1364, '01:51': 1881, '16:50': 4949, '16:04': 4655, '13:48': 3965, '05:37': 1366, '17:31': 4469, '17:30': 4542, '01:36': 2115, '19:29': 3551, '15:33': 4777, '23:14': 3204, '05:36': 1293, '05:35': 1235, '05:33': 1278, '13:19': 3601, '18:42': 3811, '02:59': 1438, '02:42': 1520, '20:39': 3626, '07:27': 1565, '15:46': 4898, '14:32': 4249, '13:06': 3533, '21:15': 3597, '11:05': 3778, '08:49': 2457, '05:45': 1282, '23:15': 3109, '01:06': 2373, '12:40': 3407, '21:26': 3496, '06:50': 1406, '03:12': 1507, '21:10': 3679, '03:04': 1614, '21:02': 3445, '21:11': 3594, '16:07': 4779, '07:05': 1481, '15:04': 4626, '21:59': 3568, '03:37': 1341, '03:34': 1365, '01:59': 1821, '15:03': 4593, '00:32': 2666, '18:31': 3824, '23:47': 2931, '21:46': 3604, '15:15': 4619, '11:40': 3851, '00:40': 2561, '08:33': 2105, '06:24': 1496, '23:01': 3072, '15:28': 4935, '23:26': 3356, '22:42': 3357, '09:00': 2985, '15:59': 4910, '15:58': 4902, '15:39': 4899, '18:59': 3665, '12:46': 3527, '11:33': 3760, '16:53': 4787, '07:19': 1528, '07:16': 1705, '07:15': 1519, '07:13': 1532, '11:21': 3827, '11:23': 4058, '10:57': 3870, '21:52': 3587, '13:23': 3927, '09:44': 3209, '01:40': 1973, '14:36': 4619, '21:44': 3631, '03:23': 1356, '15:20': 4669, '10:10': 3231, '08:21': 2041, '17:19': 4861, '07:53': 1736, '09:33': 2908, '10:22': 3552, '15:19': 4768, '19:08': 3675, '12:59': 3615, '15:17': 4585, '15:21': 4858, '17:18': 4757, '01:12': 2039, '01:10': 2192, '18:30': 3921, '15:14': 4658, '23:27': 3289, '12:48': 3544, '19:18': 3419, '23:34': 2945, '16:56': 4933, '06:23': 1332, '21:20': 3683, '13:03': 3530, '09:30': 3134, '20:52': 3378, '14:41': 4635, '05:18': 1250, '20:15': 3454, '19:59': 3514, '02:58': 1379, '17:07': 4732, '09:06': 2639, '06:01': 1306, '05:59': 1342, '20:21': 3429, '20:00': 3486, '12:34': 3489, '03:38': 1348, '04:59': 1281, '02:39': 1617, '21:39': 3685, '01:41': 2022, '21:34': 3534, '16:22': 4786, '21:17': 3558, '21:16': 3679, '00:17': 4115, '00:09': 2985, '16:58': 5149, '19:47': 3377, '09:14': 2611, '08:08': 1942, '23:56': 2897, '00:06': 2805, '10:35': 3588, '20:32': 3645, '14:27': 4476, '03:52': 1269, '01:35': 1890, '20:57': 3487, '05:23': 1194, '09:41': 3153, '03:27': 1406, '03:02': 1487, '19:45': 3422, '14:34': 4427, '11:20': 3771, '22:55': 3225, '22:35': 3492, '20:26': 3454, '09:13': 2646, '02:11': 1618, '19:50': 3434, '00:22': 2623, '23:22': 3157, '21:05': 3504, '19:44': 3594, '22:47': 3247, '09:03': 2576, '12:01': 3670, '17:56': 4409, '11:56': 3683, '08:48': 2323, '18:00': 4401, '15:02': 4618, '03:16': 1421, '21:38': 3617, '21:43': 3554, '12:38': 3575, '03:11': 1451, '19:48': 3645, '10:44': 3613, '03:41': 1256, '17:40': 4362, '17:25': 4578, '07:51': 1850, '10:28': 3653, '04:08': 1440, '17:49': 4374, '18:38': 3918, '22:24': 3457, '20:58': 3498, '11:58': 3686, '13:43': 3877, '11:42': 3864, '19:31': 3334, '20:37': 3460, '13:49': 4073, '14:30': 4231, '04:27': 1224, '12:29': 3416, '18:56': 3699, '06:30': 1264, '14:05': 4194, '22:18': 3514, '17:23': 4724, '19:51': 3408, '00:08': 2871, '11:52': 3739, '10:19': 3484, '21:55': 3537, '09:48': 3121, '23:02': 3148, '23:57': 2741, '06:54': 1355, '05:19': 1173, '11:25': 4078, '23:16': 3071, '13:57': 4143, '03:40': 1254, '12:30': 3486, '20:03': 3848, '09:49': 3321, '08:50': 2273, '02:08': 1811, '15:30': 4680, '12:36': 3317, '12:05': 3671, '11:35': 4094, '13:50': 3970, '16:48': 4980, '06:36': 1448, '09:34': 3239, '06:29': 1452, '06:08': 1325, '21:06': 3539, '12:39': 3437, '13:33': 3885, '21:32': 3483, '20:22': 3538, '18:39': 3745, '10:36': 3819, '09:10': 2731, '09:07': 2487, '22:02': 3458, '20:16': 3384, '16:08': 4963, '21:14': 3542, '14:02': 4157, '13:15': 3416, '09:09': 2638, '09:08': 2420, '08:38': 2163, '08:03': 1908, '20:19': 3535, '06:47': 1374, '09:43': 3170, '18:21': 4201, '03:14': 1469, '18:13': 4151, '00:07': 2808, '00:05': 2763, '10:29': 3790, '07:40': 1739, '07:06': 1439, '03:18': 1392, '20:23': 3549, '21:48': 3741, '18:36': 4010, '18:46': 3845, '06:58': 1492, '04:02': 1318, '00:55': 2439, '12:37': 3549, '12:58': 3647, '06:28': 1336, '09:24': 2922, '20:07': 3566, '21:01': 3548, '20:59': 3465, '12:22': 3506, '00:31': 2561, '00:03': 3148, '23:00': 3265, '23:54': 2892, '00:36': 2534, '04:34': 1324, '23:49': 2980, '05:38': 1203, '03:15': 1403, '14:59': 4729, '11:43': 3870, '11:07': 3675, '10:58': 3905, '13:29': 3762, '12:31': 3465, '02:22': 1738, '05:11': 1205, '00:41': 2452, '11:30': 3862, '07:38': 1582, '05:29': 1297, '13:46': 3984, '21:57': 3605, '07:45': 1773, '00:30': 2561, '13:58': 4457, '06:25': 1379, '15:24': 4813, '11:22': 3903, '06:20': 1347, '06:19': 1434, '10:00': 3639, '06:37': 1444, '19:38': 3437, '23:40': 3028, '04:43': 1232, '04:11': 1246, '04:10': 1535, '13:09': 3526, '04:09': 1432, '04:03': 1398, '22:14': 3516, '11:12': 4080, '02:48': 1372, '02:47': 1454, '00:27': 2844, '17:05': 4744, '21:37': 3618, '10:53': 3662, '10:12': 3404, '01:14': 2211, '02:53': 1423, '08:30': 2176, '14:20': 4249, '10:15': 3537, '01:45': 2557, '17:06': 4735, '16:59': 5073, '09:42': 3058, '15:27': 4914, '21:12': 3498, '20:13': 3547, '09:57': 3367, '08:20': 2012, '16:18': 4948, '08:05': 1804, '01:31': 1942, '13:01': 3689, '04:18': 1413, '22:59': 3329, '19:14': 3438, '20:49': 3627, '07:34': 1690, '05:28': 1272, '06:00': 1334, '23:23': 3150, '23:21': 3040, '13:45': 3956, '22:09': 3696, '13:37': 3800, '19:46': 3414, '01:15': 2244, '12:47': 3462, '20:01': 3403, '18:40': 3889, '12:07': 3458, '00:34': 2566, '19:35': 3657, '13:21': 3634, '14:53': 4732, '14:01': 4039, '04:57': 1205, '04:56': 1272, '06:55': 1429, '07:02': 1577, '17:28': 4466, '02:26': 1644, '02:21': 1632, '17:16': 4760, '02:05': 1796, '09:02': 2527, '04:48': 1202, '00:12': 2782, '23:50': 2989, '21:13': 3403, '11:38': 3809, '08:56': 2388, '17:15': 4709, '02:20': 1692, '05:20': 1160, '14:09': 4530, '12:45': 3534, '20:47': 3515, '07:29': 1672, '20:18': 3308, '00:23': 2558, '23:20': 3090, '12:49': 3668, '01:26': 2129, '07:41': 1711, '21:49': 3570, '19:36': 3380, '19:21': 3421, '04:20': 1291, '22:20': 3390, '13:10': 3574, '21:27': 3559, '01:56': 1922, '04:52': 1176, '12:51': 3662, '19:30': 3447, '04:07': 1335, '04:01': 1492, '03:59': 1229, '18:04': 4259, '16:34': 5079, '16:26': 4921, '19:40': 3485, '11:53': 3788, '10:52': 4047, '14:22': 4162, '23:09': 3224, '04:00': 1303, '03:21': 1390, '22:58': 3283, '12:55': 3497, '05:30': 1214, '23:13': 3122, '14:39': 4521, '13:26': 3882, '05:39': 1312, '01:42': 1941, '16:27': 4971, '07:31': 1636, '07:00': 1555, '12:18': 3527, '22:11': 3505, '19:57': 3459, '19:52': 3529, '13:51': 4089, '08:34': 2150, '08:12': 1879, '11:00': 3963, '22:50': 3377, '00:11': 3058, '09:04': 2573, '11:51': 3721, '21:47': 3678, '08:51': 2346, '01:17': 2138, '17:58': 4309, '17:57': 4395, '13:04': 3623, '13:38': 3865, '19:43': 3444, '15:51': 4923, '13:27': 3693, '05:12': 1214, '05:10': 1225, '05:04': 1250, '00:18': 3305, '20:14': 3293, '03:06': 1580, '21:56': 3649, '14:38': 4333, '22:21': 3500, '22:41': 3392, '10:18': 3632, '08:37': 2154, '22:16': 3569, '07:18': 1582, '07:08': 1476, '15:11': 4639, '15:37': 4747, '19:54': 3314, '19:02': 3497, '09:51': 3177, '23:51': 2989, '22:37': 3370, '03:30': 1371, '08:01': 1798, '07:58': 1754, '10:54': 3818, '12:04': 3577, '06:43': 1349, '02:07': 1653, '10:17': 3496, '02:30': 1590, '02:23': 1534, '08:27': 2087, '02:28': 1599, '11:19': 3838, '00:54': 2527, '05:14': 1269, '23:35': 2959, '08:31': 2090, '08:19': 1999, '14:00': 3922, '16:01': 4983, '09:32': 3100, '04:21': 1281, '19:25': 3556, '07:07': 1485, '18:33': 3882, '23:32': 3093, '23:29': 3167, '04:41': 1230, '13:24': 3980, '10:48': 3791, '10:42': 3627, '10:40': 3617, '10:39': 3638, '21:30': 3664, '12:06': 3618, '10:47': 3635, '14:12': 4170, '04:14': 1277, '01:24': 2125, '08:10': 1983, '08:00': 1870, '07:33': 1555, '20:24': 3367, '05:15': 1314, '04:42': 1262, '21:40': 3633, '03:44': 1251, '15:06': 4824, '20:08': 3489, '19:06': 3785, '19:41': 3477, '16:05': 4771, '23:39': 3079, '20:05': 3417, '04:38': 1254, '00:02': 2817, '04:29': 1215, '22:13': 3392, '13:35': 3813, '20:31': 3350, '18:19': 4086, '23:19': 3036, '13:22': 3721, '07:37': 1637, '07:22': 1584, '21:23': 3530, '19:13': 3658, '03:32': 1354, '18:57': 3714, '14:11': 4308, '03:22': 1284, '03:19': 1349, '06:57': 1354, '01:47': 2067, '00:42': 2401, '09:58': 3468, '08:44': 2296, '06:14': 1348, '07:20': 1592, '12:16': 3456, '00:24': 2795, '18:16': 4049, '07:54': 1861, '14:49': 4665, '15:07': 4889, '05:05': 1183, '22:29': 3476, '01:25': 2195, '20:54': 3581, '04:13': 1146, '20:56': 3546, '15:18': 4506, '04:39': 1202, '21:31': 3658, '10:06': 3320, '23:28': 3179, '19:10': 3523, '22:28': 3566, '07:44': 1751, '05:31': 1233, '03:54': 1235, '23:33': 3008, '22:17': 3628, '03:55': 1300, '08:29': 2178, '09:45': 3118, '02:51': 1462, '20:41': 3527, '01:49': 1989, '13:11': 3649, '10:05': 3349, '16:03': 4632, '22:33': 3589, '20:11': 3414, '23:10': 3181, '03:56': 1434, '22:03': 3602, '19:56': 3508, '12:19': 3542, '09:39': 3094, '11:06': 3845, '13:42': 3908, '17:32': 4325, '04:47': 1244, '02:40': 1640, '05:01': 1272, '00:57': 2238, '10:26': 3447, '08:57': 2434, '22:12': 3528, '07:24': 1569, '01:50': 2011, '22:26': 3621, '16:52': 4815, '02:24': 1675, '22:22': 3451, '13:54': 4136, '08:11': 1918, '13:32': 3741, '12:21': 3415, '16:57': 5036, '23:52': 2962, '14:18': 4101, '14:03': 4019, '00:46': 2473, '04:45': 1304, '19:20': 3405, '10:45': 3740, '00:19': 2922, '03:43': 1290, '04:15': 1239, '02:12': 1670, '08:14': 1992, '03:45': 1360, '12:20': 3367, '18:48': 3838, '23:44': 2962, '17:43': 4643, '08:04': 1833, '22:51': 3297, '22:36': 3456, '04:51': 1225, '06:33': 1463, '05:16': 1260, '05:24': 1244, '01:34': 2044, '06:06': 1402, '22:38': 3408, '11:47': 3821, '14:19': 4228, '17:44': 4703, '10:07': 3425, '07:57': 1792, '20:25': 3424, '20:43': 3477, '09:01': 2551, '16:13': 4706, '13:34': 3837, '02:37': 1660, '00:35': 2624, '23:25': 3075, '23:36': 3091, '21:28': 3634, '19:33': 3490, '11:16': 4063, '23:08': 3348, '08:47': 2330, '22:19': 3478, '07:21': 1599, '21:58': 3570, '02:27': 1586, '23:31': 3209, '02:45': 1511, '21:07': 3620, '07:28': 1631, '11:04': 3770, '00:04': 2840, '20:48': 3405, '03:42': 1228, '19:28': 3705, '02:00': 1898, '13:56': 4246, '01:08': 2293, '00:52': 2420, '15:12': 4601, '10:20': 3459, '09:54': 3220, '04:58': 1232, '08:46': 2258, '07:52': 1640, '11:10': 3836, '22:43': 3315, '08:13': 1915, '22:44': 3478, '08:07': 1963, '10:04': 3395, '00:26': 2691, '22:01': 3469, '12:54': 3618, '21:50': 3513, '03:57': 1299, '23:04': 3224, '23:48': 2872, '07:36': 1674, '07:35': 1703, '10:25': 3432, '11:34': 3775, '04:05': 1284, '05:54': 1366, '08:09': 1958, '04:19': 1359, '07:09': 1549, '14:48': 4673, '22:25': 3556, '12:23': 3470, '17:38': 4466, '22:30': 3394, '04:31': 1160, '07:47': 1687, '15:38': 5002, '02:38': 1605, '04:53': 1265, '12:43': 3526, '03:24': 1322, '03:07': 1494, '03:17': 1293, '21:41': 3643, '12:53': 3623, '19:53': 3338, '18:44': 3966, '20:20': 3573, '06:39': 1419, '20:53': 3505, '06:59': 1470, '11:29': 4090, '04:23': 1179, '21:42': 3486, '07:23': 1549, '01:13': 2133, '07:50': 1665, '10:01': 3313, '02:19': 1554, '03:09': 1569, '01:44': 1977, '20:35': 3542, '22:40': 3385, '21:19': 3512, '04:33': 1238, '02:25': 1701, '02:09': 1774, '12:25': 3334, '20:10': 3451, '01:07': 2376, '03:33': 1377, '19:23': 3602, '19:22': 3374, '08:15': 2051, '01:54': 1815, '01:48': 1926, '04:30': 1178, '06:31': 1394, '04:24': 1196, '03:26': 1284, '03:48': 1314, '03:36': 1373, '21:00': 3394, '00:56': 2428, '03:49': 1297, '03:47': 1273, '02:55': 1371, '03:53': 1254, '03:35': 1286, '06:32': 1406, '13:07': 3601, '08:06': 1910, '07:43': 1723, '09:37': 2915, '16:39': 4784, '04:44': 1289, '01:05': 2361, '01:46': 2034, '00:45': 2379, '04:50': 1281, '01:32': 2008, '22:27': 3583, '11:45': 3917, '22:53': 3576, '22:49': 3474, '23:41': 3059, '07:49': 1747, '01:02': 2842, '08:23': 2074, '11:46': 3884, '04:06': 1252, '02:29': 1659, '03:31': 1224, '01:00': 2395, '02:49': 1527, '06:52': 1397, '01:29': 2147, '12:00': 3802, '20:34': 3540, '04:12': 1234, '01:53': 1899, '05:17': 1219, '02:18': 1741, '06:02': 1307, '04:55': 1280, '04:54': 1271, '04:49': 1211, '23:12': 3180, '11:44': 4083, '07:04': 1444, '05:02': 1195, '06:15': 1319, '03:58': 1257, '16:17': 4697, '22:23': 3608, '02:56': 1399, '03:28': 1389, '11:31': 3921, '21:35': 3537, '05:48': 1419, '05:42': 1265, '02:54': 1552, '01:18': 2170, '05:03': 1267, '07:39': 1702, '21:54': 3550, '04:26': 1266, '00:37': 2649, '22:04': 3640, '06:56': 1402, '03:13': 1420, '06:34': 1484, '04:17': 1299, '02:44': 1450, '10:03': 3290, '04:46': 1244, '05:41': 1210, '02:34': 1557, '20:51': 3645, '22:32': 3403, '04:32': 1248, '03:08': 1553, '21:29': 3504, '02:13': 1960, '11:48': 3818, '22:56': 3193, '06:42': 1364, '03:03': 1553, '08:26': 2060, '04:22': 1246, '21:25': 3448, '03:29': 1303, '22:45': 3415, '12:03': 3524, '23:45': 3078, '07:48': 1785, '06:35': 1421, '23:17': 3212, '03:46': 1315, '04:25': 1165, '03:50': 1249, '02:35': 1614, '10:30': 3538, '07:26': 1602, '00:59': 2436, '04:16': 1236, '04:28': 1176, '07:11': 1472, '01:43': 2073, '07:03': 1386, '03:20': 1355, '01:20': 2165, '04:37': 1342, '02:57': 1380, '00:14': 2695, '07:46': 1822,}

# Creates a new dictionary for processing times that will replace ":" with "."
new_dictionary = {}

for x,y in result.items():
    x = x.replace(":",".")
    new_dictionary[x] = y


# Sorting the dictionary based on the time
dictionary_items = new_dictionary.items()
sorted_items = sorted(dictionary_items)
sorted_items = list(sorted_items)

# A new dictionary that will contain the tests throughout a day based on the statistics from the GitHub dataset
chance_dic = {}

# Creates a list based on the times from the dictionary of sorted items
population = [x for x,y in sorted_items]
# Creates a list of the different "weights" that are used to pick a time later
weights = [y for x,y in sorted_items]
# Iteratation used to create the tests. The bigger number fo iterate more often tests will come.
for _ in range(round(len(population)/2)):
    # Picks a time of day to send a test, based on the weights (can also be known as "odds")
    pick = random.choices(population,weights)[0]
    # Checks if the time is already in the dictionary, if so then add a random character to have it be unique
    if pick in chance_dic:
        # write "pass" for ignoring duplicates
        while pick in chance_dic:
            # While the test is in the dictionary, a new character will be added to make it unique.
            new_pick = pick[:5] + string.ascii_uppercase[random.randint(0,len(string.ascii_uppercase)-1)]
            break
        # Adds the characteristics on how long the test will take.
        chance_dic[new_pick] = 1 + round(random.uniform(0.25,1.50),2)
    else:
        # If the time is not already in the dictionary, it will be added.
        chance_dic[pick] = 1 + round(random.uniform(0.25,1.50),2)

# Sorts the test based on time.
chance_dic_items = chance_dic.items()
new_sort_items = sorted(chance_dic_items)

# CSV FILE
with open("reduced_tests.csv","w") as csv_file:
    test_writer = csv.writer(csv_file, quotechar='"', quoting=csv.QUOTE_MINIMAL)
    counter = 1
    test_writer.writerow(["TestID","ScheduledTime","TestTime"])
    for x,y in new_sort_items:
        test_writer.writerow(["T"+str(counter).zfill(4),x,round(y,2)])
        counter += 1