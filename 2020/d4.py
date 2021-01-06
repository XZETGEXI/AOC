# d4
import re

def logger(verbose = False):
    def log(*arg):
        if verbose:
            print(*arg)
    return log

data = []
with open("input.txt", "r") as f:
    for i in f.readlines():
        data.append(i.rstrip())

valid_data = []
with open("valid.txt", "r") as f:
    for i in f.readlines():
        valid_data.append(i.rstrip())

invalid_data = []
with open("invalid.txt", "r") as f:
    for i in f.readlines():
        invalid_data.append(i.rstrip())


def score(data):
    i = 0
    score = 0
    point = 0
    number = 0
    while i < len(data):
        if "byr" in data[i]:
            index = data[i].find("byr")
            temp = data[i][index+4:index+8]
            log("Year:",temp)
            try:
                if 1920 <= int(temp) <= 2002:
                    point +=1
                    log("Year OK")
                else:
                    log("Year failed")
            except:
                log("Conversion byr")
        if "iyr" in data[i]:
            index = data[i].find("iyr")
            temp = data[i][index+4:index+8]
            log("Issue:",temp)
            try:
                if 2010 <= int(temp) <= 2020:
                    point +=1
                    log("Issue OK")
                else:
                    log("Issue failed")
            except:
                log("Conversion iyr")
            
        if "eyr" in data[i]:
            index = data[i].find("eyr")
            temp = data[i][index+4:index+8]
            log("Expiration:",temp)
            try:
                if 2020 <= int(temp) <= 2030:
                    point +=1
                    log("Expiration OK")
                else:
                    log("Expiration failed")
            except:
                log("Conversion eyr")
                
        if "hgt" in data[i]:
            index = data[i].find("hgt")
            if "cm" in data[i]:
                system = "cm"
                temp = data[i][index+4:index+7]
            else:
                system = "in"
                temp = data[i][index+4:index+6]
            log("Height", temp, system)
            try:
                if system == "cm" and 150 <= int(temp) <= 193:
                    point +=1
                    log("Height OK")
                elif system == "in" and 59 <= int(temp) <= 76:
                    point +=1
                    log("Height OK")
                else:
                    log("Height failed")
            except:
                log("Conversion failed")
        if "hcl" in data[i]:
            test = re.search("#" + "[0-9, a-f]"*6, data[i])
            log("Hair: ", test)
            if not test == None:
                log("Hair OK", test.group())
                point +=1
            else:
                log("Hair failed")
        if "ecl" in data[i]:
            index = data[i].find("ecl")
            temp = data[i][index+4:index+7]
            log("Eye: ", temp)
            if temp in ["amb", "blu", "brn", "gry", "grn", "hzl", "oth"]:
                log("Eye OK")
                point +=1
            else:
                log("Eye failed")
        if "pid" in data[i]:
            index = data[i].find("pid")
            temp = data[i][index+4:index+13]
            log("Passport ID:", temp)
            test = re.search("[0-9]"*9, temp)
            if not test == None:
                point +=1
                log("Passport OK")
            else:
                log("Passport failed")
        if data[i] == "":
            if point == 7:
                score += 1
                log("OFF BY ONE !!!!!!!!!!!!!")
                log("Score is {}".format(score))
            point = 0
            log("End of number {}\n".format(number))
            number += 1
        i += 1
    if point == 7:
        score +=1
        log("OFF BY ONE !!!!!!!!!!!!!")
        log("Score is {}".format(score))
    return score


log = logger(True)
print(sum([1 if i == "" else 0 for i in data]))
print(len(data))
print(data[:10])
print(score(data))