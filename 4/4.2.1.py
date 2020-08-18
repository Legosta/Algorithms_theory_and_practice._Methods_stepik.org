def sort_chars_func(ch1, ch2):
    concat_chrs = "".join((ch1,ch2))
    sorted_chrs = sorted(concat_chrs)
    result = "".join(sorted_chrs)
    return result

string = input()
dict_with_char_freq_instr = {}
lst_vers_of_dict, srtd_lst_wth_prblts = [], []
summ = 0
final_huf_code = ""
huf_code_dict = {}

if not len(string): # if [] given as input() [duct tape]
    print([])
elif string == string[0]*len(string): # if repeated char given as input() [duct tape]
    res = "0"*len(string)
    print(len(string[0]), len(res))
    print(f"{string[0]}: 0")
    print(res)
else:
    for i in string:
        dict_with_char_freq_instr[i] = string.count(i) # make dict with chars and their counts in string
    # sort dict above by count value
    dict_with_char_freq_instr = {k:v for k,v in sorted(dict_with_char_freq_instr.items(), key = lambda item:item[1])}
    lst_vers_of_dict = list(dict_with_char_freq_instr.items())   
    # calculate sum of counts 
    for i in range(len(lst_vers_of_dict)):
        summ += lst_vers_of_dict[i][1]
    # replace counts for possibilities in list
    for j in range(len(lst_vers_of_dict)):
        srtd_lst_wth_prblts.append((lst_vers_of_dict[j][0], lst_vers_of_dict[j][1]/summ))    
    srtd_lst_wth_prblts.reverse() # descended order
    tmp_lst = []
    while len(srtd_lst_wth_prblts)!= 1: # make chars and sustrings encoded by 0/1, from the end
        tmp_lst.append((srtd_lst_wth_prblts[-1][0],'0'))
        tmp_lst.append((srtd_lst_wth_prblts[-2][0],'1'))
        srtd_lst_wth_prblts.insert(-2, (sort_chars_func(srtd_lst_wth_prblts[-1][0],srtd_lst_wth_prblts[-2][0]),srtd_lst_wth_prblts[-1][1]+srtd_lst_wth_prblts[-2][1]))
        del srtd_lst_wth_prblts[-2]
        del srtd_lst_wth_prblts[-1]
        srtd_lst_wth_prblts.sort(key = lambda x:x[1]) # [duct tape]
        srtd_lst_wth_prblts.reverse()
    for i in string: # compile final huffman code
        substr_tmp = ''
        for j in range(len(tmp_lst)):
            if i in tmp_lst[j][0]:
                substr_tmp += tmp_lst[j][1]
        huf_code_dict[i] = substr_tmp[::-1] # otherwise huffman code with prefixes generated
        final_huf_code += substr_tmp[::-1]# the same as above
    print(len(dict_with_char_freq_instr.keys()),len(final_huf_code))    
    for k, v in huf_code_dict.items():
        print(k,v)
    print(final_huf_code)