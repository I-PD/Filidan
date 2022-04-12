import os
import glob


# get the last file of the folder
def get_latest_file(_folder):
    folder = _folder
    list_of_files = glob.glob(folder + '/m*')
    latest_file = max(list_of_files, key=os.path.getctime)
    return latest_file


def get_latest_cspfile(_folder):
    folder = _folder
    list_of_files = glob.glob(folder + '/L*')
    latest_file = max(list_of_files, key=os.path.getctime)
    return latest_file


# check if file is a "FITA"
def file_approval(_latest_file):
    latest_file = _latest_file
    if latest_file[0] == 'm' or 'M':
        result = True
    else:
        result = False
    return result


# Find the ORI of the file
def find_ori(_file, _folder):
    file = _file
    folder = _folder
    file_props = file.split('/')
    filename = file_props[len(file_props) - 1].split('_')
    for i in range(len(filename)):
        if filename[i][0:3] == 'ORI':
            ori_in_filename = i
            break
        else:
            continue
    ori_name = '/NEW_ORI_' + filename[ori_in_filename][3:len(filename[ori_in_filename])]
    ori_path = folder + ori_name + '.txt'
    ori_file = glob.glob(ori_path)
    open_file = open(ori_file[0], 'r')
    read_file = open_file.read().splitlines()
    ori_list = []
    for i in range(len(read_file)):
        split_ori = read_file[i].split('\t')
        ori_list.append([split_ori[0], split_ori[1], split_ori[2], split_ori[3]])

    return ori_list, ori_name


# Return the LPV's and Signals for ploting the graphs

def order_file(_file):
    file = _file
    open_file = open(file, 'r')
    read_file = open_file.read().splitlines()
    values_list = []

    for i in range(len(read_file)):
        aux_string = read_file[i].replace(" ", "")
        aux_list = aux_string.split(';')
        values_list.append(aux_list)
        i += 1

    first_row = -1
    first_channel = -1
    # and int(values_list[i][0]) == 0
    # finding first row of a cycle and changing channel numbers(+1)
    for i in range(len(values_list)):
        if first_row == -1:
            if int(values_list[i][1]) <= 100:
                first_row = i
                first_channel = str(1 + int(values_list[i][0]))
            else:
                continue
        values_list[i][0] = str(1 + int(values_list[i][0]))
        i += 1

    cut_list = values_list[first_row:len(values_list)]
    lpv_aux = cut_list[0][5]
    lpv_1 = []
    lpv_2 = []
    lpv_3 = []
    lpv_4 = []
    lpv_5 = []
    lpv_6 = []
    lpv_7 = []
    lpv_8 = []
    signal_1 = []
    signal_2 = []
    signal_3 = []
    signal_4 = []
    signal_5 = []
    signal_6 = []
    signal_7 = []
    signal_8 = []
    channel_aux = first_channel
    list_aux = []
    list_aux2 = []

    for j in range(len(cut_list)):
        if j == len(cut_list) - 1:
            if len(cut_list[j]) < 6:
                continue

        if cut_list[j][0] == channel_aux:

            list_aux2.append(int(cut_list[j][1]))
            list_aux.append(int(cut_list[j][2]))
        else:
            lpv_aux = cut_list[j][5]
            if channel_aux == '1':
                signal_1.append([list_aux2, list_aux])
                lpv_1.append(int(lpv_aux))

            elif channel_aux == '2':
                signal_2.append([list_aux2, list_aux])
                lpv_2.append(int(lpv_aux))

            elif channel_aux == '3':
                signal_3.append([list_aux2, list_aux])
                lpv_3.append(int(lpv_aux))

            elif channel_aux == '4':
                signal_4.append([list_aux2, list_aux])
                lpv_4.append(int(lpv_aux))

            elif channel_aux == '5':
                signal_5.append([list_aux2, list_aux])
                lpv_5.append(int(lpv_aux))

            elif channel_aux == '6':
                signal_6.append([list_aux2, list_aux])
                lpv_6.append(int(lpv_aux))

            elif channel_aux == '7':
                signal_7.append([list_aux2, list_aux])
                lpv_7.append(int(lpv_aux))

            elif channel_aux == '8':
                signal_8.append([list_aux2, list_aux])
                lpv_8.append(int(lpv_aux))
            list_aux2 = [int(cut_list[j][1])]
            list_aux = [int(cut_list[j][2])]
            channel_aux = cut_list[j][0]
            continue

        if j == len(cut_list) - 1:
            if len(cut_list[j]) < 6:
                continue
        # if j == len(cut_list) - 1:
        #     lpv_aux = cut_list[j][5]
        #     if 32000 <= int(cut_list[j][1]) <= 38000:
        #         if channel_aux == '1':
        #             signal_1.append([list_aux2, list_aux])
        #             lpv_1.append(int(lpv_aux))
        #
        #         elif channel_aux == '2':
        #             signal_2.append([list_aux2, list_aux])
        #             lpv_2.append(int(lpv_aux))
        #         elif channel_aux == '3':
        #             signal_3.append([list_aux2, list_aux])
        #             lpv_3.append(int(lpv_aux))
        #
        #         elif channel_aux == '4':
        #             signal_4.append([list_aux2, list_aux])
        #             lpv_4.append(int(lpv_aux))
        #
        #         elif channel_aux == '5':
        #             signal_5.append([list_aux2, list_aux])
        #             lpv_5.append(int(lpv_aux))
        #
        #         elif channel_aux == '6':
        #             signal_6.append([list_aux2, list_aux])
        #             lpv_6.append(int(lpv_aux))
        #
        #         elif channel_aux == '7':
        #             signal_7.append([list_aux2, list_aux])
        #             lpv_7.append(int(lpv_aux))
        #
        #         elif channel_aux == '8':
        #             signal_8.append([list_aux2, list_aux])
        #             lpv_8.append(int(lpv_aux))

        j += 1

    data_signal = [signal_1, signal_2, signal_3, signal_4, signal_5, signal_6, signal_7, signal_8]
    data_lpv = [lpv_1, lpv_2, lpv_3, lpv_4, lpv_5, lpv_6, lpv_7, lpv_8]
    return data_lpv, data_signal


def treat_signal(_signal_data):
    signal_data = _signal_data
    for i in range(len(signal_data)):
        for j in range(len(signal_data[i])):
            signal_data[i][j] = signal_data[i][j].tolist()

    return signal_data


def treat_ori_for_lpv(_ori, _lpv):
    ori = _ori
    lpv = _lpv
    ori_list = []
    for i in range(len(lpv)):
        ori_aux = []
        for j in range(len(lpv[i])):
            ori_aux.append(ori[i][3])

        ori_list.append(ori_aux)

    return ori_list


def listing_lpv(_lpv, _signal, _ori):
    lpv = _lpv
    signal = _signal
    ori = _ori
    approved_lpv = []
    rejected_lvp = []
    aux_length = 0
    list_cycles = []
    for i in range(len(lpv)):
        if len(lpv[i]) > aux_length:
            aux_length = len(lpv[i])
            continue
        continue
    for i in range(aux_length):
        list_cycles.append('cycle ' + str(i + 1))

    return list_cycles


def approved_corks(_lpv, _ori):
    lpv = _lpv
    ori = _ori
    reject_taxes = []
    ttl_rj = 0
    total_scans_by_channel = 0
    for i in range(len(lpv)):
        approved = 0
        rejected = 0
        for j in range(len(lpv[i])):
            if lpv[i][j] >= int(ori[i][3]):
                rejected += 1
            else:
                approved += 1
        total_scans_by_channel += (rejected + approved)
        ttl_rj += rejected
        channel_scans = rejected + approved
        if channel_scans == 0:
            rejection_tax = 0.0
        else:
            rejection_tax = (rejected / channel_scans) * 100
        reject_taxes.append(rejection_tax)
    if total_scans_by_channel == 0:
        gl_rj = 0.0
    else:
        gl_rj = (ttl_rj / total_scans_by_channel) * 100
    return reject_taxes, total_scans_by_channel, gl_rj


def cspFile(_file):
    rawFile = _file
    splitFile = open(rawFile, 'r').read().splitlines()
    valueList = []
    # separate the values into a list
    for i in range(len(splitFile)):
        valueList.append(splitFile[i].replace(' ', '').split(';'))
        continue

    # create signal and derivative lists
    signalList = []
    auxSignal = []
    auxTimes = []
    timesList = []
    channelList = []
    auxChannel = valueList[0][0]
    for i in range(len(valueList)):
        # if the channel changes the lists are saved
        if valueList[i][0] != auxChannel:
            signalList.append(auxSignal)
            timesList.append(auxTimes)
            channelList.append(int(auxChannel) + 1)
            auxSignal = [int(valueList[i][3])]
            auxTimes = [int(valueList[i][2])]
            auxChannel = valueList[i][0]
            continue
        # if end of file lists are saved
        if i == len(valueList) - 1:
            signalList.append(auxSignal)
            timesList.append(auxTimes)
            channelList.append(int(auxChannel) + 1)
            continue
        # fill lists with the values
        auxSignal.append(int(valueList[i][3]))
        auxTimes.append(int(valueList[i][2]))
        continue
    return signalList, channelList, timesList


def orderCSP(_signals, _channels, _times):
    signal_1 = []
    signal_2 = []
    signal_3 = []
    signal_4 = []
    signal_5 = []
    signal_6 = []
    signal_7 = []
    signal_8 = []
    for i in range(len(_channels)):
        if _channels[i] == 1:
            signal_1.append([_signals[i], _times[i]])

        elif _channels[i] == 2:
            signal_2.append([_signals[i], _times[i]])

        elif _channels[i] == 3:
            signal_3.append([_signals[i], _times[i]])

        elif _channels[i] == 4:
            signal_4.append([_signals[i], _times[i]])

        elif _channels[i] == 5:
            signal_5.append([_signals[i], _times[i]])

        elif _channels[i] == 6:
            signal_6.append([_signals[i], _times[i]])

        elif _channels[i] == 7:
            signal_7.append([_signals[i], _times[i]])

        elif _channels[i] == 8:
            signal_8.append([_signals[i], _times[i]])

    data_signal = [signal_1, signal_2, signal_3, signal_4, signal_5, signal_6, signal_7, signal_8]

    return data_signal


def listCSP(_signals):
    aux_length = 0
    list_cycles = []
    for i in range(len(_signals)):
        if len(_signals[i]) > aux_length:
            aux_length = len(_signals[i])
    for cycle in range(aux_length):
        list_cycles.append('cycle ' + str(cycle + 1))

    return list_cycles
